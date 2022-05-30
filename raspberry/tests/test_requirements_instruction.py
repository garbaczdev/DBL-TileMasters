from unittest import TestCase

from src.robot.instructions import *
from src.robot.config import Config as config
from src.robot.exceptions import *

class TestRequirementsInstruction(TestCase):
#Loops Once
    def test_take_one_white(self):
        instruction = RequirementsInstruction(0, 1, 1)
        self.assertFalse(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_one_black(self):
        instruction = RequirementsInstruction(1, 0, 1)
        self.assertFalse(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_one_black_and_one_white(self):
        instruction = RequirementsInstruction(1,1,1)
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_two_black(self):
        instruction = RequirementsInstruction(2, 0, 1)
        self.assertFalse(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_two_blacks_and_two_whites(self):
        instruction = RequirementsInstruction(2, 2, 1)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_five_blacks_three_whites_once(self):
        instruction = RequirementsInstruction(5, 3, 1)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())


#Loops Twice
    def test_take_one_black_twice(self):
        instruction = RequirementsInstruction(1, 0, 2)
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_one_white_twice(self):
        instruction = RequirementsInstruction(0, 1, 2)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_two_black_twice(self):
        instruction = RequirementsInstruction(2, 0, 2)
        self.assertFalse(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_two_blacks_and_two_whites_twice(self):
        instruction = RequirementsInstruction(2, 2, 2)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_3_blacks_and_two_whites_twice(self):
        instruction = RequirementsInstruction(3, 2, 2)
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_five_blacks_three_whites_twice(self):
        instruction = RequirementsInstruction(5, 3, 2)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

#Loops Three times
    def test_take_one_black_three_times(self):
        instruction = RequirementsInstruction(1, 0, 3)
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_one_white_three_times(self):
        instruction = RequirementsInstruction(0, 1, 3)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_two_black_tree_times(self):
        instruction = RequirementsInstruction(2, 0, 3)
        self.assertFalse(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

    def test_take_two_blacks_and_two_whites_three_times(self):
        instruction = RequirementsInstruction(2, 2, 3)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_three_blacks_and_two_whites_three_times(self):
        instruction = RequirementsInstruction(3, 2, 3)
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())
    
    def test_take_five_blacks_three_whites_three_times(self):
        instruction = RequirementsInstruction(5, 3, 3)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertTrue(instruction.has_ended())

#Loops Forever
    def test_take_one_black_forever(self):
        instruction = RequirementsInstruction(1, 0, -1)
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())

    def test_take_one_white_forever(self):
        instruction = RequirementsInstruction(0, 1, -1)
        self.assertTrue(instruction.process(config.WHITE_TILE))
        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())

    def test_take_two_blacks_forever(self):
        instruction = RequirementsInstruction(2, 0, -1)
        self.assertFalse(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())
    
    def test_take_two_whites_forever(self):
        instruction = RequirementsInstruction(0, 2, -1)
        self.assertFalse(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())
    
    def test_take_two_blacks_and_two_whites_forever(self):
        instruction = RequirementsInstruction(2, 2, -1)
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())

    def test_take_two_blacks_and_two_whites_forever(self):
        instruction = RequirementsInstruction(5, 5, -1)
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        # Checks if instruction has ended
        self.assertFalse(instruction.has_ended())