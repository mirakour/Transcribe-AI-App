from db.client import get_connection
from utils.auth import decode_token
from flask import request

def get_all_summaries():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT s.id, s.summary_text, t.filename
            FROM summaries s
            JOIN transcriptions t ON s.transcription_id = t.id;
        """)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        summaries = []
        for row in rows:
            summaries.append({
                "id": row[0],
                "summary_text": row[1],
                "transcription_filename": row[2]
            })
        return summaries
    except Exception as e:
        raise e

def create_summary(transcription_id, summary_text):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO summaries (transcription_id, summary_text)
            VALUES (%s, %s)
            RETURNING *;
        """, (transcription_id, summary_text))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return {
            "id": row[0],
            "transcription_id": row[1],
            "summary_text": row[2]
        }
    except Exception as e:
        raise e
    
def auth_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return {"error": "Missing token"}, 401
        try:
            user = decode_token(token)
            request.user = user  # optional
            return f(*args, **kwargs)
        except Exception:
            return {"error": "Invalid or expired token"}, 403
    wrapper.__name__ = f.__name__
    return wrapper