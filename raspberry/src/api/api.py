from flask import Flask, jsonify, request, make_response

from ..robot import Robot
from ..robot import InstructionJSONParser


class API:
    def __init__(self, robot: Robot) -> None:
        self.robot = robot
        self.logs = robot.logs
        self.instruction_manager = robot.instruction_manager
        self.arm = self.robot.arm


        # Flask app
        self.app = Flask(__name__)
        self._register_routes()

    def run(self) -> None:
        self.app.run(host="0.0.0.0")

    def _register_routes(self) -> None:
        @self.app.route('/')
        def index():
            return '''
            <button onclick="fetch('./api/push', {method: 'POST'})">Push</button>
            <button onclick="fetch('./api/instructions/reset', {method: 'POST'})">Reset Instructions</button>
            '''

        @self.app.route('/logs', methods=["GET"])
        def get_logs():
            return f'<pre>{str(self.logs)}</pre>'

        @self.app.route('/api/logs', methods=["GET"])
        def get_logs_json():
            return jsonify(self.logs.to_jsonify_format())
        
        @self.app.route('/api/push', methods=["POST"])
        def push():
            self.arm.push()
            return jsonify({
                "ok": True
            })

        @self.app.route('/api/instructions', methods=["PUT"])
        def update_instructions():
            try:
                instructions = request.json["instructions"]
                self.robot.update_instructions(InstructionJSONParser.parse_instructions(instructions))
            except KeyError:
                return make_response(
                    jsonify({
                        "ok": False,
                        "error": "Incorrect instructions format."
                    }),
                    400
                )
            
            return jsonify({
                "ok": True
            })

