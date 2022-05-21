from abc import ABC, abstractmethod
from typing import Union

from .config import Config as config
from .exceptions import InstructionError, InvalidInstructionError


class Instruction(ABC):
    """
    An abstract class representing an instruction.
    """

    def __init__(self, repetitions: int) -> None:
        super().__init__()
        # Determines how many times the instruction should be repeated.
        # If the repetitions is -1, it means forever.
        self.repetitions = repetitions
        # Raise error if the instruction is finished before even starting.
        if self._has_repetition_ended() or self.has_ended():
            raise InvalidInstructionError("Instruction is finished before even starting.")

    def process(self, tile: int) -> bool:
        """
        This method informs the instruction that it is being performed by an instruction manager.
        The instruction will note that the tile is being processed.

        This method returns whether the tile should be taken.
        """

        if self.has_ended():
            raise InstructionError("process() called after an instruction has ended")
        
        # Check whether the tile should be taken
        should_take = self.should_take(tile)
        
        # Note that the tile is being processed
        self.inform(tile)

        # If the repetition has ended, reset the instruction. 
        if self._has_repetition_ended():
            
            # Reset the instruction.
            self.reset()
            
            # If repetitions are positive, decrease it by 1.
            if self.repetitions > 0:
                self.repetitions -= 1

        # Return whether the tile should be taken
        return should_take

    def has_ended(self) -> bool:
        """
        Returns a boolean value indicating whether the whole instruction has_ended.
        """
        return self.repetitions == 0

    @abstractmethod
    def reset(self) -> None:
        """
        Resets the instruction to the initial state.
        """
        pass

    @abstractmethod
    def should_take(self, tile: int) -> bool:

        """
        Returns a boolean value indicating whether a certain tile should be taken.

        Below code returns false if the given tile is NO_TILE or UNDEFINED_TILE.
        """

        # If instruction has ended, throw error
        if self.has_ended():
            raise InstructionError("should_take() called after an instruction has ended")

        # Return False if the tile is undefined or none
        return not (tile == config.UNDEFINED_TILE or tile == config.NO_TILE)

    @abstractmethod
    def inform(self, tile: int) -> None:
        """
        Informs the instruction that the tile is being processed on the basis of this instruction.
        This is here because some instructions do not care when the tile is skipped, for example requirements instruction,
        but some do, like a bitmask instruction.

        Below code throws an error if this method is called after the instruction has ended.
        """

        # Error checking for whether the instruction has ended
        if self.has_ended():
            raise InstructionError("inform() called after an instruction has ended")

    @abstractmethod
    def _has_repetition_ended(self) -> bool:
        """
        Returns a boolean value indicating whether the instruction repetition has ended.
        """
        pass


class RequirementsInstruction(Instruction):

    """
    This instruction type indicates how many tiles of each color should be taken (in any order).
    This instruction works only for white and black tiles.

    Example: if we were to call RequirementsInstruction(black=3, white=2), we would require
    3 black tiles and 2 white tiles to be pushed, in whatever order.
    """

    def __init__(self, black: int, white: int, repetitions: int = 1) -> None:
        
        self._black = black
        self._white = white

        self._initial_black = black
        self._initial_white = white

        super().__init__(repetitions)

    def reset(self) -> None:
        self._black = self._initial_black
        self._white = self._initial_white

    @property
    def black_left(self):
        """
        Returns how many black tiles are needed.
        """
        return self._black

    @property
    def white_left(self):
        """
        Returns how many white tiles are needed.
        """
        return self._white

    def should_take(self, tile: int) -> bool:

        # none/undefined tile checking
        if not super().should_take(tile):
            return False

        # If tile is black, return whether we need black tiles
        if tile == config.BLACK_TILE:
            return self.black_left > 0
        
        # If the tile is white, return whether we need white tiles
        else:
            return self.white_left > 0

    def inform(self, tile: int) -> None:
        # Error checking
        super().inform(tile)

        # If the tile should not be taken, do not note anything
        if not self.should_take(tile):
            return

        # If we are taking a black tile, reduce the amount of black tiles needed
        if tile == config.BLACK_TILE:
            self._black -= 1
        
        # If we are taking a white tile, reduce the amount of white tiles needed
        elif tile == config.WHITE_TILE:
            self._white -= 1

    def _has_repetition_ended(self) -> bool:
        # If we do not need any more black or white tiles, the instruction has ended 
        return self.black_left == 0 and self.white_left == 0


class BitmaskInstruction(Instruction):
    """
    This instruction type indicates the exact order in which the tiles should be taken or skipped.
    
    Example: BitmaskInstruction(bitmask="101100") means that we should take 1 tile,
    then skip 1 tile, then take 2 tiles and then skip 2 tiles.
    """

    def __init__(self, bitmask: str, repetitions: int = 1) -> None:
        # Error checking the bitmask
        # This will throw a ValueError if the mitmask is not in the binary format
        int(bitmask, 2)
        
        self.bitmask = bitmask
        # The position in the bitmask (index in a string).
        self.position = 0

        super().__init__(repetitions)

    def reset(self) -> None:
        self.position = 0

    def should_take(self, tile: int) -> bool:
        # Error checking
        if not super().should_take(tile):
            return False

        # Return False if "0" at the current position and True if "1" at the current position.
        return self.bitmask[self.position] == "1"

    def inform(self, tile: int) -> None:
        # IMPORTANT!
        # This instruction does not care about whether the tile has been skipped or not.
        # Every detected tile should be noted and treated as a part of this instruction!

        # Error checking
        super().inform(tile)

        # Increase the position in the bitmask
        self.position += 1

    def _has_repetition_ended(self) -> bool:
        # Return whether the index is bigger than the max index of the bitmask string.
        return self.position == len(self.bitmask)


class TileOrderInstruction(Instruction):
    """
    This instruction type indicates in what order the tiles of a certain color should be pushed to the box.

    Example: TileOrderInstruction(tile_order="111000111") should first take 3 white tiles and skip all the black tiles
    which were detected, then take 3 black tiles and skip the others, then take 3 white tiles and skip all the black tiles.
    This is an equivalent to the morse code SOS (or OSO, depends on the interpretation of 0s and 1s).

    This could be extended to using more than only black and white tiles.
    """
    
    def __init__(self, tile_order: Union[str, list], repetitions: int = 1) -> None:
        
        # If the tile_order is string, make it a list
        if isinstance(tile_order, str):
            # This will make a list of characters.
            # Example: tile_order = "11100"; then: self.tile_order = ["1", "1", "1", "0", "0"]
            self.tile_order = [char for char in tile_order]
        else:
            # This allows for having more arbitrary tile types.
            # Example: ["green", "blue", "purple"]
            self.tile_order = tile_order

        self.initial_tile_order = self.tile_order[:]
        
        super().__init__(repetitions)
        
    def reset(self) -> None:
        self.tile_order = self.initial_tile_order[:]
    
    def should_take(self, tile: int) -> bool:
        
        # Error checking
        if not super().should_take(tile):
            return False
        
        # Return whether the tile order at the current position is equal to the tile color
        return self.tile_order[0] == str(tile)

    def inform(self, tile: int) -> None:
        # Error checking
        super().inform(tile)

        # If we skip the tile, this instruction does not care.
        if not self.should_take(tile):
            return

        # Remove the first tile in the order.
        self.tile_order.pop(0)

    def _has_repetition_ended(self) -> bool:
        # Return whether the tile_order is empty
        return len(self.tile_order) == 0


class InstructionJSONParser:
    """
    Parses the instructions from the JSON request format to actual objects.
    """
    @classmethod
    def parse_instructions(cls, instruction_list: list[dict]) -> list[Instruction]:
        return []
