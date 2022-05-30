from unittest import TestCase

from src.robot.instructions import PatternInstruction
from src.robot.config import Config as config

from run_e2e_test import run_e2e_test


class PatternE2ETests(TestCase):
    def test_take_2_black_and_2_whitw(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, True),
            (1, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
            PatternInstruction("1100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_5_whites(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True)
        ]
        instructions = [
            PatternInstruction("11111")
        ]

        run_e2e_test(self, tile_events, instructions)

    def test_take_5_blacks(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
            PatternInstruction("00000")
        ]

        run_e2e_test(self, tile_events, instructions)

    def test_1_black_2_whites_and_2_blacks(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           PatternInstruction("01100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_sorting_black(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True)

        ]
        instructions = [
           PatternInstruction("0110011")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_1_black_2_whites_and_1_black(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           PatternInstruction("0110")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_1_black_2_whites_5_blacks(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           PatternInstruction("01100000")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_1_black_2_whites_3_black(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           PatternInstruction("011000")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_2_white_then_take_8_black(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           PatternInstruction("1100000000")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_2_black_and_2_whites_4_times(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True)
            
        ]
        instructions = [
           PatternInstruction("0011001100110011")
        ]

        run_e2e_test(self, tile_events, instructions)