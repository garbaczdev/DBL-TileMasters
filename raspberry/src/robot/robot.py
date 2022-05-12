from time import sleep
from typing import Union

from .tile_manager import TileManager
from .tile_scanner import TileScanner, TestingTileScanner
from .instruction_manager import InstructionManager
from .instructions import RequirementsInstruction
from .arm import Arm, TestingArm
from .events import TileEvent

from .config import Config as config
from .logs import Logs, LogComponent

class Robot(LogComponent):
    """
    This is the main class for operating the robot.
    """
    
    def __init__(self, test_tile_events: Union[None, list[TileEvent]] = None) -> None:
        """
        This constructor takes the optional argument test_tile_events, which is the list of TileEvents.
        If test_tile_events is passed, robot will enter the ARTIFICIAL_ENVIRONMENT_TESTING mode, which will
        simulate how the robot would work if the (given) tiles were present at the TileScanner.
        """
        
        # Enter testing mode basing on test_tile_events
        self.update_testing_variables(test_tile_events)

        # Create main logs.
        logs = Logs()
        super().__init__(logs)

        # Create the instruction manager.
        self.instruction_manager = InstructionManager(logs=self.logs)

        # If in ARTIFICIAL_ENVIRONMENT_TESTING mode
        if config.ARTIFICIAL_ENVIRONMENT_TESTING:
            # Create a testing arm
            self.arm = TestingArm(logs=self.logs)
            # Create a normal tile manager.
            self.tile_manager = TileManager(self.arm, self.instruction_manager, logs=self.logs)
            # Create a testing tile scanner.
            self.tile_scanner = TestingTileScanner(test_tile_events, self.tile_manager, logs=self.logs)
        else:
            # Create a normal arm
            self.arm = Arm(logs=self.logs)
            # Create a normal tile manager.
            self.tile_manager = TileManager(self.arm, self.instruction_manager, logs=self.logs)
            # Create a normal tile scanner.
            self.tile_scanner = TileScanner(self.tile_manager, logs=self.logs)


    @property
    def COMPONENT_NAME(self) -> str:
        return "Robot"

    def run(self) -> None:
        """
        Runs the robot.
        """
        self._prepare()
        self._main_loop()

    def run_loop(self) -> None:
        self.tile_scanner.scan()
        self.tile_manager.execute_ready_tile_events()

    def update_testing_variables(self, test_tile_events: Union[None, list[TileEvent]]) -> None:
        if test_tile_events is None:
            config.ARTIFICIAL_ENVIRONMENT_TESTING = False
        else:
            config.ARTIFICIAL_ENVIRONMENT_TESTING = True

    def _prepare(self) -> None:
        pass

    def _main_loop(self) -> None:
        """
        Run the main loop.
        """
        while True:
            self.run_loop()
            sleep(config.MAIN_LOOP_TIMEOUT)