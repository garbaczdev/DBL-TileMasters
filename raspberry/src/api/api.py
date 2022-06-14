import os

from flask import Flask, jsonify, request, make_response, send_from_directory
from werkzeug.exceptions import BadRequest, MethodNotAllowed, TooManyRequests
import logging

from ..robot import Robot
from ..robot import InstructionJSONParser


class API:
    def __init__(self, robot: Robot, main_dir, host: str = "0.0.0.0", debug: bool = True) -> None:
        self.robot = robot

        self.logs = robot.logs
        self.instruction_manager = robot.instruction_manager
        self.arm = self.robot.arm


        # Flask app
        self.host = host
        self.debug = debug

        self.app = Flask(main_dir, static_folder='build')
        
        self._register_routes()

    def run(self) -> None:
        self.app.run(host=self.host)

    def _register_routes(self) -> None:

        @self.app.route('/', defaults={'path': ''})
        @self.app.route('/<path:path>')
        def send_static_file(path):
            if path != "" and os.path.exists(self.app.static_folder + '/' + path):
                return send_from_directory(self.app.static_folder, path)
            else:
                return send_from_directory(self.app.static_folder, 'index.html')

        @self.app.route('/api/logs', methods=["GET"])
        def get_logs_json():
            return jsonify({
                "logs": self.logs.to_jsonify_format()
            })

        @self.app.route('/api/mode', methods=["GET"])
        def get_mode_json():
            return jsonify({
                "mode": self.robot.get_mode()
            })

        @self.app.route('/api/count', methods=["GET"])
        def get_tile_count_json():
            return jsonify({
                "count": self.logs.tile_count
            })

        @self.app.route('/api/mode/<string:mode>', methods=["POST"])
        def update_mode(mode: str):

            if mode == "instruction":

                self.robot.change_to_instruction_mode()

                return jsonify({
                    "ok": True,
                    "mode": self.robot.get_mode()
                })

            elif mode == "manual":

                self.robot.change_to_manual_mode()

                return jsonify({
                    "ok": True,
                    "mode": self.robot.get_mode()
                })

            raise BadRequest(f"{mode} is an unknown mode.")

        @self.app.route("/api/info-pagination/<int:last_log_id>", methods=["GET"])
        def get_paginated_info_with_logs(last_log_id: int):
            return jsonify({
                "logs": self.logs.to_jsonify_format(last_log_id),
                "mode": self.robot.get_mode(),
                "count": self.logs.tile_count
            })

        @self.app.route("/api/info-pagination/", methods=["GET"])
        def get_paginated_info():
            return jsonify({
                "logs": [],
                "mode": self.robot.get_mode(),
                "count": self.logs.tile_count
            })
        
        @self.app.route('/api/push', methods=["POST"])
        def push():
            if self.robot.is_in_manual_mode():

                if self.arm.is_pushing:
                    return TooManyRequests("Arm is being pushed already.")
                    
                self.arm.push()

                return jsonify({
                    "ok": True
                })
            
            raise MethodNotAllowed("Robot is not in the manual mode.")

        @self.app.route('/api/instructions', methods=["PUT"])
        def update_instructions():
            try:
                instructions = request.json["instructions"]
                self.robot.update_instructions(InstructionJSONParser.parse_instructions(instructions))
            except Exception as e:
                raise BadRequest(str(e) if self.debug else "Incorrect instruction format.")
            
            return jsonify({
                "ok": True
            })

