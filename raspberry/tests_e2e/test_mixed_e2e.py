
from unittest import TestCase

from src.robot.instructions import RequirementsInstruction, BitmaskInstruction, PatternInstruction
from src.robot.config import Config as config

from run_e2e_test import run_e2e_test


class MixedInstructionE2ETests(TestCase):

    def test_bitmask_and_sorting(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, True)
        ]
        instructions = [
            BitmaskInstruction("010", 1),
            RequirementsInstruction(0, 1, -1)
        ]

        run_e2e_test(self, tile_events, instructions)