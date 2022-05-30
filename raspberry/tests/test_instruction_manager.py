from unittest import TestCase

from src.robot.instructions import *
from src.robot.instruction_manager import InstructionManager
from src.robot.config import Config as config


class TestInstructionManager(TestCase):
    def test_take_1_leave1_take1(self):
        instructions = [
            BitmaskInstruction("001", 2),
            RequirementsInstruction(2, 1, -1)
        ]
        instruction_manager = InstructionManager(instructions)
        
        self.assertFalse(instruction_manager.execute_instruction(config.BLACK_TILE))
        self.assertFalse(instruction_manager.execute_instruction(config.BLACK_TILE))
        self.assertTrue(instruction_manager.execute_instruction(config.BLACK_TILE))

        self.assertTrue(instruction_manager.exectute_instruction( config.BlACK_TILE))
        self.assertTrue(instruction_manager.exectute_instruction( config.BlACK_TILE))
        self.assertTrue(instruction_manager.exectute_instruction( config.WHITE_TILE))
        self.assertTrue(instruction_manager.had_instructions_ended())
        