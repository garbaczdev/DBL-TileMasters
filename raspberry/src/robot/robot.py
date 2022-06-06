from time import sleep
from datetime import datetime
from typing import Union


from .tile_manager import TileManager
from .tile_scanner import TileScanner, TestingTileScanner
from .instruction_manager import InstructionManager
from .instructions import Instruction
from .arm import Arm, TestingArm
from .events import TileEvent

from .config import Config as config
from .utils import Utils as utils
from .logs import Logs, LogComponent

class Robot(LogComponent):
    """
    This is the main class for operating the robot.
    """
    
    def __init__(self, test_tile_events: Union[None, list[TileEvent]] = None, mode: str = config.INSTRUCTION_MODE) -> None:
        """
        This constructor takes the optional argument test_tile_events, which is the list of TileEvents.
        If test_tile_events is passed, robot will enter the ARTIFICIAL_ENVIRONMENT_TESTING mode, which will
        simulate how the robot would work if the (given) tiles were present at the TileScanner.
        """
        
        # Enter testing mode basing on test_tile_events
        self._update_testing_variables(test_tile_events)

        self.mode = mode

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
            self.tile_manager = TileManager(self.arm, self.get_mode, self.instruction_manager, logs=self.logs)
            # Create a testing tile scanner.
            self.tile_scanner = TestingTileScanner(test_tile_events, self.tile_manager, logs=self.logs)
        else:
            # Create a normal arm
            self.arm = Arm(config.ARM_GPIO_PIN, logs=self.logs)
            # Create a normal tile manager.
            self.tile_manager = TileManager(self.arm, self.get_mode, self.instruction_manager, logs=self.logs)
            # Create a normal tile scanner.
            self.tile_scanner = TileScanner(self.tile_manager, logs=self.logs)

        # Indicates whether the robot should stop.
        self.should_stop = False

        self.new_instructions = list()
        self.new_instructions_set = False


    @property
    def COMPONENT_NAME(self) -> str:
        return "Robot"

    def get_mode(self) -> str:
        return self.mode

    def change_to_manual_mode(self) -> str:
        self.add_log("switched-to-manual-mode", "Switched to manual mode")
        self.mode = config.MANUAL_MODE

    def change_to_instruction_mode(self) -> str:
        self.add_log("switched-to-instruction-mode", "Switched to instruction mode")
        self.mode = config.INSTRUCTION_MODE


    def update_instructions(self, instructions: list[Instruction]) -> None:
        self.new_instructions = instructions
        self.new_instructions_set = True
    
    def run(self) -> None:
        """
        Runs the main loop of the robot.
        """
        self.add_log("turned-on", "Starting to run")
        self.should_stop = False

        while not self.should_stop:
            self._run_actions()
            sleep(config.MAIN_LOOP_TIMEOUT)

        self.stop()

    def run_until(self, time: datetime) -> None:
        """
        Runs the robot until certain given datetime passes.
        """
        self.add_log("turned-on", f"Starting to run until: {time}")
        self.should_stop = False
        
        while not self.should_stop and datetime.now() < time:
            self._run_actions()
            sleep(config.MAIN_LOOP_TIMEOUT)

        self.stop()

    def run_for(self, seconds: int) -> None:
        """
        Runs the robot for a certain amount of seconds.
        """
        time = utils.get_time_after_ms(seconds*1000)
        self.run_until(time)

    def stop(self, log=True) -> None:
        """
        If this method is called, it will stop the robot as soon as it ends its loop actions.
        """
        if log:
            self.add_log("stop", "Stop called")
        self.should_stop = True

    def _update_testing_variables(self, test_tile_events: Union[None, list[TileEvent]]) -> None:
        if test_tile_events is None:
            config.ARTIFICIAL_ENVIRONMENT_TESTING = False
        else:
            config.ARTIFICIAL_ENVIRONMENT_TESTING = True

    def _run_actions(self) -> None:
        self._update_instructions()
        self.tile_scanner.scan()
        self.tile_manager.execute_ready_tile_event()
    
    def _update_instructions(self) -> None:
        if self.new_instructions_set:
            
            self.instruction_manager.update_instructions(self.new_instructions)
            self.add_log("new-instructions", f"Instructions updated to {[repr(instruction) for instruction in self.new_instructions]}")

            self.new_instructions_set = False
            self.new_instructions = list()
            
