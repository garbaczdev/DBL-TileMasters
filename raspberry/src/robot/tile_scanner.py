from datetime import datetime, timedelta

from .events import TimeoutEvent, TileEvent
from .tile_manager import TileManager

from .logs import LogComponent, Logs

from .config import Config as config
from .utils import Utils as utils


# class TileColorDecider:
#     PERFECT_COLORS = {
#         config.BLACK_TILE: {
#             "lux": 90,
#             "rgb": (16, 16, 16)
#         }
#     }

#     RGB_CHANNEL_THRESHOLD = 2
#     LUX_THRESHOLD = 20

#     @classmethod
#     def get_color(cls, rgb: tuple, lux: float) -> None:

#         diffs = []

#         for tile_color, properties in cls.PERFECT_COLORS.items():

#             perfect_rgb = properties["rgb"]
#             perfect_lux = properties["lux"]

#             rgb_diff = [abs(channel - perfect_channel) for channel, perfect_channel in zip(rgb, perfect_rgb)]
#             lux_diff = abs(lux - perfect_lux)

#             if cls.in_range(lux_diff, cls.LUX_THRESHOLD) and \
#                 all(cls.in_range(channel_diff, cls.RGB_CHANNEL_THRESHOLD) for channel_diff in rgb_diff):
                
#                 pass

#     @staticmethod
#     def in_range(num1: int, num2: int, range: int) -> bool:
#         return abs(num1 - num2) <= range



class TileScanner(LogComponent):

    """
    Class representing the scanner that scans the tiles. 
    
    It can add the tile events to the TileManager, which is equivalent to
    saying that "the tile of color x will be at your place at time x".
    """

    READINGS_THRESHOLD = 30

    def __init__(self, tile_manager: TileManager, logs: Logs = Logs(), use_pins: bool = True) -> None:
        super().__init__(logs)

        self.tile_manager = tile_manager
        # This is used for timing out the scanner.

        self.readings = []

        self.tile_color_methods = {
            config.WHITE_TILE: self.is_tile_white,
            config.BLACK_TILE: self.is_tile_black
        }

        if use_pins:

            from .sensor_driver import TCS3472
            import board

            i2c = board.I2C()  # uses board.SCL and board.SDA
            self.sensor = TCS3472(i2c)

        else:
            self.sensor = None

    @property
    def COMPONENT_NAME(self) -> str:
        return "TileScanner"

    def scan(self) -> None:
        """
        This method scans the current tile and if the scanner is not timed out,
        it adds the TileEvent to the tile manager.
        """

        # Get the current tile.
        tile = self.current_tile()
        
        # Check whether there is a tile.
        if tile != config.NO_TILE:
            # Add the event to the tile_manager
            self._log_tile(tile)
            self._register_tile_event(tile)

    def current_tile(self) -> int:
        """
        This should return the tile that is currently detected by the scanner.
        """

        if self.sensor is None:
            return config.NO_TILE
        
        rgb = self.sensor.color_rgb_bytes
        lux = self.sensor.lux

        self.readings.append((rgb, lux))
        if all(self.is_reading_background(reading) for reading in self.readings):
            self.readings.pop()

        if len(self.readings) > self.READINGS_THRESHOLD:
            self.readings.pop(0)

            if not self.finished_reading(self.readings):
                self.add_log("error", f"Something is blocking the scanner!")
                self.readings = []
                return config.NO_TILE


        # print(self.readings)

        if self.finished_reading(self.readings):

            for tile_color, method in self.tile_color_methods.items():
                
                if method(self.readings):
                    self.readings = []
                    return tile_color

            self.readings = []
            return config.UNDEFINED_TILE

        return config.NO_TILE

    @classmethod
    def is_tile_black(cls, readings: list):
        black_readings = [reading for reading in readings if cls.is_reading_black(reading)]
        return len(black_readings) >= 2

    @staticmethod
    def is_tile_white(readings: list):
        # print(readings)
        return any(lux > 750 for rgb, lux in readings)

    @classmethod
    def finished_reading(cls, readings: list) -> None:
        return len(readings) >= 5 and cls.is_reading_background(readings[-1])

    @staticmethod
    def is_reading_background(reading: tuple) -> bool:
        rgb, lux = reading
        return all(utils.is_in_range(channel, 16, 2) for channel in rgb) and utils.is_in_range(lux, 90, 5)
    
    @staticmethod
    def is_reading_black(reading: tuple) -> None:
        rgb, lux = reading

        return all(utils.is_in_range(channel, 8, 2) for channel in rgb) and utils.is_in_range(lux, 90, 5)

    def _log_tile(self, tile: int) -> None:
        """
        Notes the detected tile to the logs.

        If there is no tile, it will not inform the logs.
        """

        # Get the color name
        color = config.TILE_COLOR_DICT.get(tile)

        # If such color exists, log the action.        
        if color is not None:
            self.add_log(f"{color.lower()}-detected", f"{color} tile detected")


    def _register_tile_event(self, tile: int) -> None:
        """
        This registers the TileEvent to the TileManager.

        It is equivalent to saying: "Tile of color x will be at your place
        at the time of x".
        """

        # Get the time after config.SCANNER_TILE_EVENT_TIMEOUT has passed.
        time = utils.get_time_after_s(config.SCANNER_TILE_EVENT_TIMEOUT)

        # Create the TileEvent.
        tile_event = TileEvent(time, tile)
        
        # Add the TileEvent to the TileManager.
        self.tile_manager.add_tile_event(tile_event)


class TestingTileScanner(TileScanner):
    """
    This is the class that implements the functionality of TileScanner but does not implement any physical behavior.
    It can be used for ARTIFICIAL_ENVIRONMENT_TESTING mode.
    """

    def __init__(self, tile_events: list[TileEvent], tile_manager: TileManager, logs: Logs = Logs()) -> None:
        """
        The constructor takes the tile_events, which is the list of TileEvents, indicating when the tile will appear at the scanner.
        """
        super().__init__(tile_manager, logs, use_pins=False)
        self.tile_events = tile_events
        # If finishing the tile_events has been logged.
        self.tile_events_logged_finish = False
        # This indicates the color of the last tile detected by this scanner.
        self.last_tile_detected = config.NO_TILE

    @property
    def COMPONENT_NAME(self) -> str:
        return "TestingTileScanner"

    def current_tile(self) -> int:
        """
        This returns the current tile based on the tile events.
        """

        # If there are any tile events.
        if self.tile_events:

            # Get the first tile event.
            tile_event = self.tile_events[0]

            # If tile event is ready.
            if tile_event.is_ready():
                # Remove the tile event.
                self.tile_events.pop(0)
                # Save the returned tile.
                self.last_tile_detected = tile_event.tile
                # Return the tile color.
                return tile_event.tile
        else:
            # There are no tile events

            # If the end of tile events has not been logged yet.
            if not self.tile_events_logged_finish:
                self.add_log("testing-events-finished", "Tile events have been finished")
                self.tile_events_logged_finish = True

        # Return no tile.
        return config.NO_TILE
