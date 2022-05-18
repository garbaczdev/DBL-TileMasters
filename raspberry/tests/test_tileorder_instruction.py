from unittest import TestCase

from src.robot.instructions import *
from src.robot.config import Config as config
from src.robot.exceptions import *


class TestTileOrderInstruction(TestCase):

    def one_black_followed_by_one_white(self):
        instruction = TileOrderInstruction("10")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.WHITE_TILE))
    
    def two_black_followed_by_one_white(self):
        instruction = TileOrderInstruction("110")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.WHITE_TILE))