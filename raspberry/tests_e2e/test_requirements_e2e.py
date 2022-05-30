
from unittest import TestCase

from src.robot.instructions import RequirementsInstruction
from src.robot.config import Config as config

from run_e2e_test import run_e2e_test


class RequirementsInstructionE2ETests(TestCase):

    def test_sorting_white(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
            RequirementsInstruction(0, 1, -1)
        ]

        run_e2e_test(self, tile_events, instructions, "RequirementsInstructionE2ETests.test_sorting_white")

    def test_sorting_black(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
            RequirementsInstruction(1, 0, -1)
        ]

        run_e2e_test(self, tile_events, instructions, "RequirementsInstructionE2ETests.test_sorting_black")

    def test_requirements_without_repetition(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
            RequirementsInstruction(1, 2)
        ]

        run_e2e_test(self, tile_events, instructions, "RequirementsInstructionE2ETests.test_requirements_without_repetition")
    
    def test_requirements_with_repetition(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
            RequirementsInstruction(1, 2, 2)
        ]

        run_e2e_test(self, tile_events, instructions, "RequirementsInstructionE2ETests.test_requirements_with_repetition")