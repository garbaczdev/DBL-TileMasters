
from .arm import Arm
from .instruction_manager import InstructionManager
from .events import TileEvent

from .config import Config as config
from .logs import Logs, LogComponent

class TileManager(LogComponent):
    
    """
    This is the class that manages the tile distribution. It controls all of the events and the arm.
    """
    
    def __init__(self, arm: Arm, mode_callback = None,  instruction_manager: InstructionManager = None, logs: Logs = Logs()) -> None:
        super().__init__(logs)

        # If the instruction manager was not given.
        if instruction_manager is None:
            instruction_manager = InstructionManager(logs=self.logs)

        self._arm = arm
        self.mode_callback = mode_callback
        self.instruction_manager = instruction_manager
        
        # List containing the tile events.
        # Every TileEvent indicates that a tile of color X is at the place of the arm in the time X.
        self._tile_events: list[TileEvent] = list()

    @property
    def COMPONENT_NAME(self) -> str:
        return "TileManager"

    def execute_ready_tile_event(self) -> None:
        """
        Executes the ready tile event, which means that it will take notice of
        the tile being present at the place of the arm and it will push the arm accordingly.

        It can execute at most 1 ready tile event.
        """

        # If the tile events are not empty.
        if self._tile_events:

            # Get the first tile event
            tile_event = self._tile_events[0]

            # If the tile event is ready.
            if tile_event.is_ready():
                # Log out the action.
                self._log_action(f"{config.TILE_COLOR_DICT[tile_event.tile]} tile at the arm")
                # Delete the tile event.
                self._tile_events.pop(0)

                # Execute the tile event.
                if self.mode_callback is None or self.mode_callback() == config.INSTRUCTION_MODE:
                    self.execute_tile_event(tile_event)


    def execute_tile_event(self, tile_event: TileEvent) -> None:

        # Check whether the arm should be pushed.
        should_arm_push = self.instruction_manager.execute_instruction(tile_event.tile)

        # If it should be, push it.
        if should_arm_push:
            self._arm.push()


    def add_tile_event(self, tile_event: TileEvent) -> None:
        """
        Adds a tile event, which means that it notifies the tile manager that
        the tile of color X will be at the place of the arm in the time X.
        """
        self._tile_events.append(tile_event)
