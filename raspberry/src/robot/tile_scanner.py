from datetime import datetime, timedelta

from .events import TimeoutEvent, TileEvent
from .tile_manager import TileManager

from .logs import LogComponent, Logs

from .config import Config as config
from .utils import Utils as utils

class TileScanner(LogComponent):

    """
    Class representing the scanner that scans the tiles. 
    
    It can add the tile events to the TileManager, which is equivalent to
    saying that "the tile of color x will be at your place at time x".
    """

    def __init__(self, tile_manager: TileManager, logs: Logs = Logs()) -> None:
        super().__init__(logs)

        self.tile_manager = tile_manager
        # This is used for timing out the scanner.
        self.timeout_end_event = TimeoutEvent()

    @property
    def COMPONENT_NAME(self) -> str:
        return "TileScanner"

    def scan(self) -> None:
        """
        This method scans the current tile and if the scanner is not timed out,
        it adds the TileEvent to the tile manager.
        """
        
        # Check whether the timeout is over
        if self.timeout_end_event.is_ready():

            # Get the current tile.
            tile = self.current_tile()

            self._log_tile(tile)
            
            # Check whether there is a tile.
            if tile != config.NO_TILE:
                # Add the event to the tile_manager
                self._register_tile_event(tile)

                # Set timeout to the scanner so it doesnt scan the same tile several times.
                self.set_timeout()

    def current_tile(self) -> int:
        """
        This should return the tile that is currently detected by the scanner.
        """

        # This is only temporary and should be replaced by the code that gets
        # the currently scanned tile.
        return config.NO_TILE
    

    def set_timeout(self) -> None:
        """
        This sets the timeout to the scanner. It is like sleeping.
        """
        # Get the time after config.SCANNER_TIMEOUT has passed
        timeout_end_time = utils.get_time_after_ms(config.SCANNER_TIMEOUT)

        # Set the new timeout end
        self.timeout_end_event.update_time(timeout_end_time)

    def _log_tile(self, tile: int) -> None:
        """
        Notes the detected tile to the logs.

        If there is no tile, it will not inform the logs.
        """

        # Get the color name
        color = config.TILE_COLOR_DICT.get(tile)

        # If such color exists, log the action.        
        if color is not None:
            self._log_action(f"{color} tile detected")


    def _register_tile_event(self, tile: int) -> None:
        """
        This registers the TileEvent to the TileManager.

        It is equivalent to saying: "Tile of color x will be at your place
        at the time of x".
        """

        # Get the time after config.SCANNER_TILE_EVENT_TIMEOUT has passed.
        time = utils.get_time_after_ms(config.SCANNER_TILE_EVENT_TIMEOUT)

        # Create the TileEvent.
        tile_event = TileEvent(time, tile)
        
        # Add the TileEvent to the TileManager.
        self.tile_manager.add_tile_event(tile_event)


class TestTileScanner(TileScanner):

    def __init__(self, test_file_path: str, tile_manager: TileManager, logs: Logs = Logs()) -> None:
        super().__init__(tile_manager, logs)
        self.test_file_path = test_file_path

    def current_tile(self) -> int:
        """
        This should return the tile that is currently detected by the scanner.
        """
        return None
