
from .arm import Arm
from .instruction_manager import InstructionManager
from .events import TileEvent

from .logs import Logs, LogComponent

class TileManager(LogComponent):
    
    """
    This is the class that manages the tile distribution. It controls all of the events and the arm.
    """
    
    def __init__(self, arm: Arm, instruction_manager: InstructionManager = None, logs: Logs = Logs()) -> None:
        super().__init__(logs)

        if instruction_manager is None:
            instruction_manager = InstructionManager(logs=self.logs)
        
        self.instruction_manager = instruction_manager

        self._arm = arm
        
        self._tile_events: list[TileEvent] = list()

    @property
    def COMPONENT_NAME(self) -> str:
        return "TileManager"

    def execute_ready_tile_events(self) -> None:
        if self._tile_events:
            tile_event = self._tile_events[0]

            if tile_event.is_ready():
                self._log_action(f"{tile_event} at the arm")
                self._tile_events.pop(0)
                self.execute_tile_event(tile_event)


    def execute_tile_event(self, tile_event: TileEvent) -> None:

        should_arm_push = self.instruction_manager.execute_instruction(tile_event.tile)

        if should_arm_push:
            self._arm.push()


    def add_tile_event(self, tile_event: TileEvent) -> None:
        self._tile_events.append(tile_event)
