from unittest import TestCase

from src.robot.instructions import *
from src.robot.config import Config as config
from src.robot.exceptions import *
# Black = 0, White = 1

class TestTileOrderInstruction(TestCase):
# Two tiles
    def test_two_blacks(self):
        instruction = TileOrderInstruction("00")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_one_black_followed_by_one_white(self):
        instruction = TileOrderInstruction("01")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

    def test_one_white_followed_by_one_black(self):
        instruction = TileOrderInstruction("10")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

    def test_two_whites(self):
        instruction = TileOrderInstruction("11")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

#Three tiles
    def test_two_blacks_followed_by_one_white(self):
        instruction = TileOrderInstruction("001")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

    def test_two_whites_followed_by_one_black(self):
        instruction = TileOrderInstruction("110")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_one_black_followed_by_one_white_then_one_blakc(self):
        instruction = TileOrderInstruction("101")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_three_whites(self):
        instruction = TileOrderInstruction("111")
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

#Four Tiles
    def test_four_blacks(self):
        Instruction = TileOrderInstruction("0000")
        self.assertTrue(Instruction.process(config.BLACK_TILE))
        self.assertTrue(Instruction.process(config.BLACK_TILE))
        self.assertTrue(Instruction.process(config.BLACK_TILE))
        self.assertTrue(Instruction.process(config.BLACK_TILE))

    def test_two_whites_followed_by_two_blacks(self):
        instruction = TileOrderInstruction("1100")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertFalse(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

    def test_one_white_then_one_black_then_one_white_then_one_black(self):
        instruction = TileOrderInstruction("1010")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

    def test_four_whites(self):
        instruction = TileOrderInstruction("1111")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

#Five Tiles
    def test_five_blacks(self):
        instruction = TileOrderInstruction("00000")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

    def test_four_black_followed_by_one_white(self):
        instruction = TileOrderInstruction("00001")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_three_black_followed_by_two_white(self):
        instruction = TileOrderInstruction("00011")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_one_black_followed_by_one_white_twice_then_black(self):
        instruction = TileOrderInstruction("01010")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_five_whites(self):
        instruction = TileOrderInstruction("11111")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

    
# Six Tiles
    def test_three_white_followed_by_three_black(self):
        instruction = TileOrderInstruction("000111")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_one_black_followed_by_one_white_three_time(self):
        instruction = TileOrderInstruction("010101")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_one_white_followed_by_one_black_three_time(self):
        instruction = TileOrderInstruction("101010")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_three_white_followed_by_three_black(self):
        instruction = TileOrderInstruction("111000")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_six_white(self):
        instruction = TileOrderInstruction("111111")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

# Other
    def test_three_whites_followed_by_three_blacks_then_three_whites(self):
        instruction = TileOrderInstruction("111000111")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))

        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))

        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_five_blacks_followed_by_five_whites(self):
        instruction = TileOrderInstruction("0000011111")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
    
    def test_one_white_then_one_black_six_times(self):
        instruction = TileOrderInstruction("101010101010")
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
    
    def test_15_blacks_followed_by_five_whites(self):
        instruction = TileOrderInstruction("00000000000000011111")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))
        self.assertTrue(instruction.process(config.WHITE_TILE))