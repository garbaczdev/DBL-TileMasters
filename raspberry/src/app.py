from threading import Thread
from time import sleep

from .robot import Robot
from .api import API
from .robot.instructions import PatternInstruction


class App:
    def __init__(self, testing = False) -> None:
        if testing:
            self.robot = Robot([])
        else:
            self.robot = Robot()
            
        self.api = API(self.robot, __name__)

        self.robot.update_instructions([
            PatternInstruction("01", -1)
        ])

    def run(self) -> None:

        robot_thread = Thread(target = self.robot.run)
        api_thread = Thread(target = self.api.run)

        robot_thread.setDaemon(True)
        api_thread.setDaemon(True)

        robot_thread.start()
        api_thread.start()

        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            print("----Shutting Down----")
            exit(0)