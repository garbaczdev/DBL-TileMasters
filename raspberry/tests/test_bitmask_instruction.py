from unittest import TestCase

from src.robot.instructions import *
from src.robot.config import Config as config


class TestBitmaskInstruction(TestCase):
    def test_take_1_leave1_take1(self):
        instruction = BitmaskInstruction("101")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.has_ended())
        
    def test_take1_leave1_take2_leave1(self):
        instruction = BitmaskInstruction("10110")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.has_ended())
        
    def test_take1(self):    
        instruction = BitmaskInstruction("1")
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.has_ended())
        
    def test_dont_take2(self):
     instruction = BitmaskInstruction("00")
     self.assertFalse(instruction.process(config.BLACK_TILE))
     self.assertFalse(instruction.process(config.BLACK_TILE))
     self.assertTrue(instruction.has_ended())
     
    def test_skip2_take2(self):
        instruction = BitmaskInstruction("0011")
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.has_ended())
    
    def test_skip1_take1(self):
        instruction = BitmaskInstruction("01")
        self.assertFalse(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.process(config.BLACK_TILE))
        self.assertTrue(instruction.has_ended())

    def test_take2_leave2(self):
      instruction = BitmaskInstruction("1100")
      self.assertTrue(instruction.process(config.BLACK_TILE))
      self.assertTrue(instruction.process(config.BLACK_TILE))
      self.assertFalse(instruction.process(config.BLACK_TILE))
      self.assertFalse(instruction.process(config.BLACK_TILE))
      self.assertTrue(instruction.has_ended())  

class TestTileOrderInstruction(TestCase):
    pass
