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
        self.black = black
        self.white = white

    def should_take(self, tile: int) -> bool:

        if not super().should_take(tile):
            return False

        if tile == config.BLACK_TILE:
            return self.black > 0
        
        else:
            return self.white > 0

    def next_tile(self, tile: int) -> None:
        super().next_tile(tile)

        if tile == config.BLACK_TILE:
            self.black -= 1
        
        elif tile == config.WHITE_TILE:
            self.white -= 1

    def has_ended(self) -> bool:
        return self.black == 0 and self.white == 0


class BitmaskInstruction(Instruction):

    def __init__(self) -> None:
        pass

    def should_take(self, tile: int) -> bool:
        pass

    def next_tile(self, tile: int) -> None:
        pass

    def has_ended(self) -> bool:
        pass


class TileOrderInstruction(Instruction):
    
    def __init__(self) -> None:
        pass
    
    def should_take(self, tile: int) -> bool:
        pass

    def next_tile(self, tile: int) -> None:
        pass

    def has_ended(self) -> bool:
        pass

