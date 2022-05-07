from datetime import datetime


class Event:
    """
    Class describing an event. It contains the time of the event.
    """
    def __init__(self, time: datetime = datetime.now()) -> None:
        self.time = time

    def is_ready(self) -> bool:
        return datetime.now() > self.time

    def update_time(self, new_time: datetime) -> None:
        self.time = new_time


class TimeoutEvent(Event):
    """
    Class describing the timeout event. It is used as the sleep instruction.
    """
    pass


class TileEvent(Event):
    """
    Class describing the event of a given tile being at certain place in the given time. 
    """
    def __init__(self, time: datetime, tile: int) -> None:
        super().__init__(time)
        self.tile = tile

