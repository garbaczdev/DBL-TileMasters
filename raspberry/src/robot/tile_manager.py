
from .arm import Arm
from .events import TileEvent

class TileManager:
    
    """
    This is the class that manages the tile distribution. It controls all of the events and the arm.
    """
    
    def __init__(self) -> None:
        self._arm = Arm()
        self._tile_events: list[TileEvent] = list()

    def execute_ready_tile_events(self) -> None:
        if self._tile_events:
            tile_event = self._tile_events[0]

            if tile_event.is_ready():
                self._tile_events.pop(0)
                self.execute_tile_event(tile_event)


    def execute_tile_event(self, tile_event: TileEvent) -> None:
        pass

    def add_tile_event(self, tile_event: TileEvent) -> None:
        self._tile_events.append(tile_event)
