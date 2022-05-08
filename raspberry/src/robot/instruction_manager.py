
from .instructions import Instruction

class InstructionManager:
    def __init__(self, instructions: list[Instruction] = list()) -> None:
        self._instructions = instructions

    def execute_instruction(self, tile: int) -> bool:
        
        while self._instructions and self._instructions[0].has_ended():
            self._instructions.pop(0)

        if self.had_instructions_ended():
            return False

        instruction = self._instructions[0]

        should_take = instruction.process(tile)

        if instruction.has_ended():
            self._instructions.pop(0)

        return should_take


    def had_instructions_ended(self) -> bool:
        return len(self._instructions) == 0

    def clear_instructions(self) -> None:
        self.set_new_instructions(list())

    def set_new_instructions(self, instructions: list[Instruction]) -> None:
        self._instructions = instructions

    def add_instruction(self, instruction: Instruction) -> None:
        self._instructions.append(instruction)
    
    def add_instructions(self, instructions: list[Instruction]) -> None:
        for instruction in instructions:
            self.add_instruction(instruction)
