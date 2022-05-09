from .robot import Robot

class App:
    def __init__(self) -> None:
        self.robot = Robot()

    def run(self) -> None:
        self.robot.run()
        