
from unittest import TestCase

from src.robot.instructions import BitmaskInstruction
from src.robot.config import Config as config

from run_e2e_test import run_e2e_test

class BitmaskE2ETests(TestCase):

    def test_leave_all(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, False),
            (1, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
            BitmaskInstruction("0000000000")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_all(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
            BitmaskInstruction("1111111111")
        ]

        run_e2e_test(self, tile_events, instructions)

    def test_take_half_leave_half(self) -> None:
        tile_events = [
            (1, config.WHITE_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
            BitmaskInstruction("1111100000")
        ]

        run_e2e_test(self, tile_events, instructions)

    def test_sorting_white(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
           BitmaskInstruction("01100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_sorting_black(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False)

        ]
        instructions = [
           BitmaskInstruction("1001100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_takes_2_leaves_2(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
           BitmaskInstruction("1100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_2_leave_2_twice(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False)
        ]
        instructions = [
           BitmaskInstruction("11001100")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_take_3_leave_2_take_1(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, True),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           BitmaskInstruction("111001")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_leave_6_take_4(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, False),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           BitmaskInstruction("0000001111")
        ]

        run_e2e_test(self, tile_events, instructions)
    
    def test_alternate(self) -> None:
        tile_events = [
            (1, config.BLACK_TILE, False),
            (1, config.WHITE_TILE, True),
            (2, config.WHITE_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True),
            (1, config.BLACK_TILE, False),
            (1, config.BLACK_TILE, True)
        ]
        instructions = [
           BitmaskInstruction("0101010101")
        ]

        run_e2e_test(self, tile_events, instructions)
