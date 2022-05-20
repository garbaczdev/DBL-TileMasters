from .robot import Robot
from .api import API

class App:
    def __init__(self) -> None:
        self.robot = Robot()
        self.api = API(Robot, 80)

    def run(self) -> None:
        self.robot.run()
        