from time import sleep

from .tile_manager import TileManager
from .tile_scanner import TileScanner
from .instructions import RequirementsInstruction

from .logs import Logs, LogComponent

class Robot(LogComponent):
    """
    This is the main class for operating the robot.
    """
    
    def __init__(self) -> None:
        
        logs = Logs()
        super().__init__(logs)

        self.tile_manager = TileManager(logs=self.logs)
        self.tile_scanner = TileScanner(self.tile_manager, logs=self.logs)

    def _log(self) -> None:
        pass

    def run(self) -> None:
        """
        Runs the robot.
        """

        self.tile_manager.instruction_manager.add_instruction(RequirementsInstruction(5, 0))

        self._main_loop()

    def _main_loop(self) -> None:
        """
        Run the main loop.
        """
        second = 0
        while True:
            print(f"----LOOP {second} START----")
            self.tile_scanner.scan()
            self.tile_manager.execute_ready_tile_events()
            sleep(1)
            second += 1