from flask import Flask, jsonify

from ..robot import Robot


class API:
    def __init__(self, robot: Robot) -> None:
        self.robot = robot
        self.logs = robot.logs
        self.instruction_manager = robot.instruction_manager
        self.arm = self.robot.arm


        # Flask app
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return '''
            <button onclick="fetch('./api/push', {method: 'POST'})">Push</button>
            '''

        @self.app.route('/api/logs', methods=["GET"])
        def get_logs():
            return jsonify(self.logs.to_jsonify_format())
        
        @self.app.route('/api/push', methods=["POST"])
        def push():
            self.arm.push()
            return "PUSHED"
    

    def run(self) -> None:
        self.app.run(host="0.0.0.0")
