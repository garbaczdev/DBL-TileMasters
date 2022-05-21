from .robot import Robot
from .api import API


class App:
    def __init__(self) -> None:
        self.robot = Robot([])
        self.api = API(self.robot)

    def run(self) -> None:
        # It should run in two threads!
        # self.robot.run()
        self.api.run()
        