
from .instructions import Instruction

from .logs import Logs, LogComponent

class InstructionManager(LogComponent):
    """
    This class is responsible for managing the instructions.
    """

    def __init__(self, instructions: list[Instruction] = list(), logs: Logs = Logs()) -> None:
        super().__init__(logs)
        self._instructions = instructions

    @property
    def COMPONENT_NAME(self) -> str:
        return "InstructionManager"

    def execute_instruction(self, tile: int) -> bool:

        """
        Executes the current instruction and returns whether a given tile should be taken.
        If the return value is False, the tile should be skipped.
        """
        
        # This checks whether there are instructions to execute and rejects the finished instructions.
        if self.had_instructions_ended():
            return False

        # Get the current instruction
        instruction = self._instructions[0]

        # Process the instruction
        should_take = instruction.process(tile)

        # Return whether the given tile should be taken
        return should_take


    def had_instructions_ended(self) -> bool:
        """
        Returns whether the instructions have ended.
        It also rejects the finished instructions.
        """
        
        # Reject ended instructions
        self._reject_ended_instructions()

        # If the instruction list is empty, return True
        return len(self._instructions) == 0

    def clear_instructions(self) -> None:
        """
        Clears the instructions list.
        """
        self.set_new_instructions(list())

    def set_new_instructions(self, instructions: list[Instruction]) -> None:
        """
        Sets the instruction list to the new given instructions.
        """
        self._instructions = instructions

    def add_instruction(self, instruction: Instruction) -> None:
        """
        Adds a given instructions.
        """
        self._instructions.append(instruction)
    
    def add_instructions(self, instructions: list[Instruction]) -> None:
        """
        Adds the given instructions to the instruction list.
        """
        for instruction in instructions:
            self.add_instruction(instruction)
        
    def _reject_ended_instructions(self) -> None:
        """
        Pops the finished instructions from the list.
        
        It starts from the beginning of the instruction lists and stops when an unfinished instruction is found,
        so if the finished instructions are found after an unfinished instruction, they will not be deleted.
        """
        while self._instructions and self._instructions[0].has_ended():
            self._instructions.pop(0)
