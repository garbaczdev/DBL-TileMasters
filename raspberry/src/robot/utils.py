from typing import Union
from datetime import datetime, timedelta

from .events import TileEvent

from .config import Config as config

class Utils:
    
    @classmethod
    def create_robot_tile_events(cls, tile_tuples: list[tuple[int, int, bool]]) -> list[TileEvent]:
        """
        This returns the list of tile events given the list of tuples containing the seconds from the last tile when 
        the tile should appear at the scanner and tile_color.

        On top of that, some time (configurable in config.py) will be added to the given time.
        """

        tile_tuples = [tile_tuple[:2] for tile_tuple in tile_tuples]

        # Make every miliseconds of the tuple be the sum of the previous ones.
        cascaded_tiles = [tile_tuples[0]]
        for miliseconds, tile in tile_tuples[1:]:
            cascaded_tiles.append((miliseconds + cascaded_tiles[-1][0], tile))
        
        # Get the current time.
        now = datetime.now()

        # Return the tile events of when the tile will be at the arm.
        return [TileEvent(cls.get_time_after_s(seconds, now), tile) for seconds, tile in cascaded_tiles]

    @staticmethod
    def get_log_format_str(_id: Union[int, str], date_str: str, component_name: str, description: str) -> str:
        """
        Returns the string in the Log format, given all of the variables.
        """
        return f"{f'%-{config.LOG_ID_SPACE}s' % f'[{_id}]:'} ({date_str[:config.LOG_TIME_SPACE]}) {f'%-{config.LOG_COMPONENT_NAME_SPACE}s' % f'[{component_name}]:'}({description})"
    

    @classmethod
    def get_time_after_s(cls, seconds: int, time: datetime = None) -> datetime:
        """
        Return the datetime object of the time after the given seconds have passed.
        """

        return cls.get_time_after_ms(seconds*1000, time)

    @staticmethod
    def get_time_after_ms(milliseconds: int, time: datetime = None) -> datetime:
        """
        Return the datetime object of the time after the given milliseconds have passed.
        """

        if time is None:
            time = datetime.now()

        return time + timedelta(milliseconds=milliseconds)
    
    @staticmethod
    def is_in_range(num1: float, num2: float, range: float) -> bool:
        return abs(num1 - num2) <= range

