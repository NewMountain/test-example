from flask import Flask, jsonify, request
from src.business_logic import add_two


def create_flask_app():
    app = Flask(__name__)

    @app.route("/")
    def home_handler():
        return "Hello world"

    @app.route("/addTwo", methods=["POST"])
    def add_two_handler():

        json_content = request.get_json()
        return {"number": add_two(json_content)}

    return app
