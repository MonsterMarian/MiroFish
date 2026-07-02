from flask import Blueprint, jsonify
from ..config import Config

test_bp = Blueprint('test', __name__)

@test_bp.route('/check_key', methods=['GET'])
def check_key():
    api_key = Config.ZEP_API_KEY
    if not api_key:
        return jsonify({"status": "no_key"})
    return jsonify({
        "status": "ok",
        "key_start": api_key[:10],
        "key_end": api_key[-10:],
        "length": len(api_key)
    })
