
from datetime import datetime, timedelta

from .events import TileEvent


class Utils:
    
    @classmethod
    def create_tile_events(cls, tile_tuples: list[tuple[int, int]]) -> list[TileEvent]:
        """
        This returns the list of tile events given the list of tuples containing the seconds from the last tile when 
        the tile should appear at the scanner and tile_color.

        On top of that, some time (configurable in config.py) will be added to the given time.
        """

        # Change seconds to miliseconds
        tile_tuples = [(seconds*1000, tile) for seconds, tile in tile_tuples]

        # Make every miliseconds of the tuple be the sum of the previous ones.
        cascaded_tiles = [tile_tuples[0]]
        for miliseconds, tile in tile_tuples[1:]:
            cascaded_tiles.append((miliseconds + cascaded_tiles[-1][0], tile))
        
        # Get the current time.
        now = datetime.now()

        # Return the tile events of when the tile will be at the arm.
        return [TileEvent(cls.get_time_after_ms(miliseconds, now), tile) for miliseconds, tile in cascaded_tiles]

    @staticmethod
    def get_time_after_ms(milliseconds: int, time: datetime = None) -> datetime:
        """
        Return the datetime object of the time after the given milliseconds have passed.
        """

        if time is None:
            time = datetime.now()

        return time + timedelta(milliseconds=milliseconds)
    
