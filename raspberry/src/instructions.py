from abc import ABC, abstractmethod

from .config import Config as config
from .exceptions import InstructionError

class Instruction(ABC):

    @abstractmethod
    def should_take(self, tile: int) -> bool:

        """
        Returns a boolean value indicating whether a certain tile should be taken.

        Below code returns false if the given tile is NO_TILE or UNDEFINED_TILE.
        """

        if self.has_ended():
            raise InstructionError("should_take() called after an instruction has ended")

        return not (tile == config.UNDEFINED_TILE or tile == config.NO_TILE)

    @abstractmethod
    def next_tile(self, tile: int) -> None:
        """
        Goes to the next tile in the instruction.

        Below code throws an error if this method is called after the instruction has ended.
        """
        if self.has_ended():
            raise InstructionError("next_tile() called after an instruction has ended")

    @abstractmethod
    def has_ended(self) -> bool:
        """
        Returns a boolean value indicating whether the instruction has_ended.
        """
        pass


class RequirementsInstruction(Instruction):

    def __init__(self, black: int, white: int) -> None:
        self._black = black
        self._white = white

    @property
    def black_left(self):
        return self._black

    @property
    def white_left(self):
        return self._white

    def should_take(self, tile: int) -> bool:

        if not super().should_take(tile):
            return False

        if tile == config.BLACK_TILE:
            return self.black_left > 0
        
        else:
            return self.white_left > 0

    def next_tile(self, tile: int) -> None:
        super().next_tile(tile)

        if tile == config.BLACK_TILE:
            self._black -= 1
        
        elif tile == config.WHITE_TILE:
            self._white -= 1

    def has_ended(self) -> bool:
        return self.black_left == 0 and self.white_left == 0


class BitmaskInstruction(Instruction):

    def __init__(self, bitmask: str) -> None:
        # Error checking the bitmask
        # This will throw a ValueError if the mitmask is not in the binary format
        int(bitmask, 2)
        
        self.bitmask = bitmask
        self.position = 0


    def should_take(self, tile: int) -> bool:
        if not super().should_take(tile):
            return False

        return bool(self.bitmask[self.position])

    def next_tile(self, tile: int) -> None:
        super().next_tile(tile)
        self.position += 1

    def has_ended(self) -> bool:
        return self.position == len(self.bitmask)


class TileOrderInstruction(Instruction):
    
    def __init__(self, tile_order: str) -> None:
        # Error checking the bitmask
        # This will throw a ValueError if the mitmask is not in the binary format
        int(tile_order, 2)
        
        self.tile_order = tile_order
        self.position = 0
    
    def should_take(self, tile: int) -> bool:
        if not super().should_take(tile):
            return False
        
        return self.tile_order[self.position] == "0" and tile == config.BLACK_TILE \
            or self.tile_order[self.position] == "1" and tile == config.WHITE_TILE

    def next_tile(self, tile: int) -> None:
        super().next_tile(tile)
        self.position += 1

    def has_ended(self) -> bool:
        return self.position == len(self.tile_order)

