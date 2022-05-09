
from .tile_manager import TileManager
from .tile_scanner import TileScanner

class Robot:
    
    def __init__(self) -> None:
        self.tile_manager = TileManager()
        self.tile_scanner = TileScanner(self.tile_manager)

    def run(self) -> None:
        self._main_loop()

    def _main_loop(self) -> None:
        pass