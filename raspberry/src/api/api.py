import os

from flask import Flask, jsonify, request, make_response, send_from_directory

from ..robot import Robot
from ..robot import InstructionJSONParser


class API:
    def __init__(self, robot: Robot, main_dir, debug: bool = True) -> None:
        self.robot = robot
        self.logs = robot.logs
        self.instruction_manager = robot.instruction_manager
        self.arm = self.robot.arm


        # Flask app
        self.debug = debug
        self.app = Flask(main_dir, static_folder='build')
        self._register_routes()

    def run(self) -> None:
        self.app.run(host="0.0.0.0")

    def _register_routes(self) -> None:

        @self.app.route('/', defaults={'path': ''})
        @self.app.route('/<path:path>')
        def send_static_file(path):
            if path != "" and os.path.exists(self.app.static_folder + '/' + path):
                return send_from_directory(self.app.static_folder, path)
            else:
                return send_from_directory(self.app.static_folder, 'index.html')

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
            except Exception as e:
                return make_response(
                    jsonify({
                        "ok": False,
                        "error": str(e) if self.debug else "Incorrect instructions format.",
                    }),
                    400
                )
            
            return jsonify({
                "ok": True
            })

