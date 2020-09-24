from flask import Blueprint, request, jsonify
from flask_cors import CORS
from extensions import db
import controllers.feedback_controller as controller
import requests

app = Blueprint('feedback', __name__)
CORS(app)

@app.route("/feedback", methods=["POST"])
def feedback():
    return controller.save_feedback_request(request.json)