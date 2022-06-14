from threading import Thread
from time import sleep

from .robot import Robot
from .api import API
from .robot.instructions import RequirementsInstruction


class App:
    def __init__(self, testing = False) -> None:
        if testing:
            self.robot = Robot([])
            host = "127.0.0.1"
        else:
            self.robot = Robot()
            host = "0.0.0.0"

        self.api = API(self.robot, __name__, host=host)

        self.robot.update_instructions([
            RequirementsInstruction(0, 1, -1)
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