from flask import Blueprint, jsonify

example_bp = Blueprint("example_bp", __name__)

@example_bp.route("/")
def index():
    return jsonify({"message": "This is an example route!"})

