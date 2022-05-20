
from flask import Flask

from ..robot import Robot


class API:
    def __init__(self, robot: Robot) -> None:
        self.logs = robot.logs
        self.instruction_manager = robot.instruction_manager

        # Flask app
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return str(self.logs)
    

    def run(self) -> None:
        self.app.run(host="0.0.0.0")
