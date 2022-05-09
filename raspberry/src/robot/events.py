from datetime import datetime


class Event:
    """
    Class describing an event. It contains the time of the event.
    """
    def __init__(self, time: datetime = datetime.now()) -> None:
        self.time = time

    def is_ready(self) -> bool:
        """
        This method returns whether the event is ready.
        Example: event.time = 8:32; current_time = 9:02; event.time.is_ready() == True 
        """
        return datetime.now() > self.time

    def update_time(self, new_time: datetime) -> None:
        """
        Updates the time of the event to the given time.
        """
        self.time = new_time


class TimeoutEvent(Event):
    """
    Class describing the timeout event. It can be used as the sleep instruction end time.
    """
    pass


class TileEvent(Event):
    """
    Class describing the event of a given tile being at certain place in the given time. 
    """
    def __init__(self, time: datetime, tile: int) -> None:
        super().__init__(time)
        self.tile = tile

