from flask import Blueprint, jsonify, request
from queries.transcriptions import (
    get_all_transcriptions,
    get_transcription_by_id,
    create_transcription
)
from queries.transcriptions import update_transcription
from queries.transcriptions import delete_transcription

transcriptions_bp = Blueprint('transcriptions', __name__)

# GET /transcriptions
@transcriptions_bp.route('/', methods=['GET'])
def fetch_transcriptions():
    try:
        data = get_all_transcriptions()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /transcriptions/<id>
@transcriptions_bp.route('/<int:id>', methods=['GET'])
def fetch_transcription_by_id(id):
    try:
        data = get_transcription_by_id(id)
        if data:
            return jsonify(data), 200
        else:
            return jsonify({"error": "Transcription not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /transcriptions
@transcriptions_bp.route('/', methods=['POST'])
def add_transcription():
    try:
        data = request.get_json()

        filename = data.get("filename")
        source_type = data.get("source_type")
        speaker_count = data.get("speaker_count")

        if not filename or not source_type or speaker_count is None:
            return jsonify({"error": "Missing required fields"}), 400

        new_transcription = create_transcription(filename, source_type, speaker_count)
        return jsonify(new_transcription), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@transcriptions_bp.route('/<int:id>', methods=['PUT'])
def edit_transcription(id):
    try:
        data = request.get_json()
        filename = data.get("filename")
        source_type = data.get("source_type")
        speaker_count = data.get("speaker_count")

        if not filename or not source_type or speaker_count is None:
            return jsonify({"error": "Missing required fields"}), 400

        updated = update_transcription(id, filename, source_type, speaker_count)
        if updated:
            return jsonify(updated), 200
        else:
            return jsonify({"error": "Transcription not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@transcriptions_bp.route('/<int:id>', methods=['DELETE'])
def remove_transcription(id):
    try:
        deleted = delete_transcription(id)
        if deleted:
            return jsonify({"message": f"Transcription {id} deleted"}), 200
        else:
            return jsonify({"error": "Transcription not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500