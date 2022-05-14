from time import sleep

from unittest import TestCase

from src.robot import Robot
from src.robot.instructions import RequirementsInstruction
from src.robot.utils import Utils as utils
from src.robot.config import Config as config

class EnvironmentTesting(TestCase):
    
    def test1(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE),
            (1, config.WHITE_TILE),
            (2, config.WHITE_TILE),
            (1, config.BLACK_TILE),
            (1, config.BLACK_TILE)
        ]
        tile_events = utils.create_tile_events(tile_events)
        robot = Robot(tile_events)
        robot.instruction_manager.add_instruction(RequirementsInstruction(1, 2, 2))
        # robot.instruction_manager.add_instruction(RequirementsInstruction(1, 0))
        robot.run_for(12)

    def test2(self) -> None:
        tile_events = []
        robot = Robot(tile_events)