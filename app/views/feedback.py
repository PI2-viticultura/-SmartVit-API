from flask import Blueprint, request
from flask_cors import CORS
import controllers.feedback_controller as controller

app = Blueprint('feedback', __name__)
CORS(app)


@app.route("/feedback", methods=["POST"])
def feedback():
    return controller.save_feedback_request(request.json)
