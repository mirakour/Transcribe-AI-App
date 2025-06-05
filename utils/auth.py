import os
import jwt
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

def hash_password(password):
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    import bcrypt
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_token(payload):
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Unauthorized"}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded = decode_token(token)
            request.user = decoded
        except Exception as e:
            return jsonify({"error": "Invalid token"}), 403

        return f(*args, **kwargs)
    return wrapper