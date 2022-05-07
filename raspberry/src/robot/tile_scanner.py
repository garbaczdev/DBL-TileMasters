from datetime import datetime

from .config import Config as config
from .events import TimeoutEvent

class TileScanner:

    """
    Class representing the scanner that scans the tiles.
    """

    def __init__(self) -> None:
        self.timeout_end = TimeoutEvent()

    def scan(self) -> None:
        
        if self.timeout_end.is_ready():
            # Put some scanning code here
            # Add a tile event to the arm.
            self.set_timeout(config.SCANNER_TIMEOUT)

    def current_tile(self) -> None:
        pass

    def set_timeout(self, miliseconds: int) -> None:
        pass

    def _current_color(self) -> None:
        pass
