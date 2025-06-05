from flask import Blueprint, jsonify, request
from queries.summaries import get_all_summaries, create_summary
from utils.auth import auth_required

summaries_bp = Blueprint('summaries', __name__)

@summaries_bp.route('/', methods=['GET'])
def fetch_summaries():
    try:
        summaries = get_all_summaries()
        return jsonify(summaries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@summaries_bp.route('/', methods=['POST'])
@auth_required
def add_summary():
    try:
        data = request.get_json()
        transcription_id = data.get("transcription_id")
        summary_text = data.get("summary_text")

        if not transcription_id or not summary_text:
            return jsonify({"error": "Missing required fields"}), 400

        new_summary = create_summary(transcription_id, summary_text)
        return jsonify(new_summary), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@summaries_bp.route("/protected", methods=["GET"])
@auth_required
def protected_summary_view():
    return {"message": f"You accessed a protected summary route!"}