
from .arm import Arm
from .instruction_manager import InstructionManager
from .events import TileEvent

class TileManager:
    
    """
    This is the class that manages the tile distribution. It controls all of the events and the arm.
    """
    
    def __init__(self, instruction_manager: InstructionManager = InstructionManager()) -> None:
        self._instruction_manager = instruction_manager
        self._arm = Arm()
        self._tile_events: list[TileEvent] = list()

    def execute_ready_tile_events(self) -> None:
        if self._tile_events:
            tile_event = self._tile_events[0]

            if tile_event.is_ready():
                self._tile_events.pop(0)
                self.execute_tile_event(tile_event)


    def execute_tile_event(self, tile_event: TileEvent) -> None:

        should_arm_extend = self._instruction_manager.execute_instruction(tile_event.tile)

        if should_arm_extend:
            self._arm.extend()
        else:
            self._arm.hide()

    def add_tile_event(self, tile_event: TileEvent) -> None:
        self._tile_events.append(tile_event)
