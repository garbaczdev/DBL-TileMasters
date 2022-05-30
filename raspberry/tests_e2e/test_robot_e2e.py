# from concurrent.futures.thread import _threads_queues
# from time import sleep
# from threading import Thread

# from unittest import TestCase

# from src.robot import Robot
# from src.robot.instructions import Instruction, RequirementsInstruction, BitmaskInstruction, TileOrderInstruction
# from src.robot.utils import Utils as utils
# from src.robot.config import Config as config


# def run_e2e_test(testing_class: TestCase, tile_events: list[tuple[int, int, bool]], instructions: list[Instruction]) -> None:

#     config.PRINT_LOGS = False

#     robot_tile_events = utils.create_robot_tile_events(tile_events)
#     robot = Robot(robot_tile_events)
#     robot.instruction_manager.update_instructions(instructions)
    
#     arm = robot.tile_manager._arm

#     error = None

#     def testing_func():
        
#         nonlocal error

#         sleep(config.E2E_TESTING_START_TIMEOUT)
#         sleep(config.SCANNER_TILE_EVENT_TIMEOUT)
        
#         for tile_event in tile_events:
#             sleep(tile_event[0])
#             try:
#                 testing_class.assertEqual(tile_event[2], arm.has_pushed())
#             except AssertionError as e:
#                 robot.stop(log=False)
#                 robot.logs.print()

#                 error = e
#                 return

#         robot.stop()

#     robot_thread = Thread(target=robot.run)
#     testing_thread = Thread(target=testing_func)

#     robot_thread.start()
#     testing_thread.start()

#     testing_thread.join()
#     testing_thread.join()

#     if error is not None:
#         raise error

        
# class RequirementsInstructionE2ETests(TestCase):

#     def test_sorting_white(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, False),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             RequirementsInstruction(0, 1, -1)
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_sorting_black(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#             RequirementsInstruction(1, 0, -1)
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_requirements_without_repetition(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             RequirementsInstruction(1, 2)
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_requirements_without_repetition_2(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             RequirementsInstruction(2, 2)
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
    
#     def test_requirements_with_repetition(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             RequirementsInstruction(1, 2, 2)
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_requirements_with_repetition_2(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#             RequirementsInstruction(4, 2, 2),
#         ]

#     def test_requirements_without_repetition_3(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True)
#         ]
#         instructions = [
#             RequirementsInstruction(2, 2, 2)
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_requirements_without_repetition_4(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True)
#         ]
#         instructions = [
#             RequirementsInstruction(1, 2, 3)
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_requirements_without_repetition_5(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False)
#         ]
#         instructions = [
#             RequirementsInstruction(1, 0, 3)
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_requirements_without_repetition_6(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True)
          
#         ]
#         instructions = [
#             RequirementsInstruction(1, 1, 5)
#         ]

#         run_e2e_test(self, tile_events, instructions)

# # Bitmask
# class BitmaskE2ETests(TestCase):

#     def test_leave_all(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, False),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             BitmaskInstruction("0000000000")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_all(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#             BitmaskInstruction("1111111111")
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_take_half_leave_half(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#             BitmaskInstruction("1111100000")
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_sorting_white(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, False),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#            BitmaskInstruction("01100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_sorting_black(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False)

#         ]
#         instructions = [
#            BitmaskInstruction("1001100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_takes_2_leaves_2(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#            BitmaskInstruction("1100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_2_leave_2_twice(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False)
#         ]
#         instructions = [
#            BitmaskInstruction("11001100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_3_leave_2_take_1(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            BitmaskInstruction("111001")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_leave_6_take_4(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, False),
#             (1, config.WHITE_TILE, False),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            BitmaskInstruction("0000001111")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_alternate(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, False),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, False),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            BitmaskInstruction("0101010101")
#         ]

#         run_e2e_test(self, tile_events, instructions)

# # 
# class TileOrderE2ETests(TestCase):
#     def test_take_2_black_and_2_whitw(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#             TileOrderInstruction("1100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_5_whites(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True)
#         ]
#         instructions = [
#             TileOrderInstruction("11111")
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_take_5_blacks(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#             TileOrderInstruction("00000")
#         ]

#         run_e2e_test(self, tile_events, instructions)

#     def test_1_black_2_whites_and_2_blacks(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            TileOrderInstruction("01100")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_sorting_black(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True)

#         ]
#         instructions = [
#            TileOrderInstruction("0110011")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_1_black_2_whites_and_1_black(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            TileOrderInstruction("0110")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_1_black_2_whites_5_blacks(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            TileOrderInstruction("01100000")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_1_black_2_whites_3_black(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            TileOrderInstruction("011000")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_2_white_then_take_8_black(self) -> None:
#         tile_events = [
#             (1, config.WHITE_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True)
#         ]
#         instructions = [
#            TileOrderInstruction("1100000000")
#         ]

#         run_e2e_test(self, tile_events, instructions)
    
#     def test_take_2_black_and_2_whites_4_times(self) -> None:
#         tile_events = [
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.BLACK_TILE, True),
#             (1, config.WHITE_TILE, True),
#             (2, config.WHITE_TILE, True)
            
#         ]
#         instructions = [
#            TileOrderInstruction("0011001100110011")
#         ]

#         run_e2e_test(self, tile_events, instructions)

# # Requirements and Bitmask
# class RequirementsAndBitmaskE2ETest(TestCase):
#     pass

# # Requirements and TileOrder
# class RequirementsAndTileOrderE2ETest(TestCase):
#     pass

# # Bitmask and TileOrer
# class BitmaskAndBTileOrderE2ETest(TestCase):
#     pass

# # Requirements and Bitmask and TileOrder
# class RequirementsAndBitmaskAndTileOrderE2ETest(TestCase):
#     pass
