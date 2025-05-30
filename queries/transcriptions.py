from db.client import get_connection

# GET all transcriptions
def get_all_transcriptions():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM transcriptions;")
        rows = cur.fetchall()

        transcriptions = []
        for row in rows:
            transcriptions.append({
                "id": row[0],
                "filename": row[1],
                "source_type": row[2],
                "speaker_count": row[3],
                "created_at": row[4].isoformat()
            })

        cur.close()
        conn.close()
        return transcriptions
    except Exception as e:
        raise e

# GET transcription by ID
def get_transcription_by_id(id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM transcriptions WHERE id = %s;", (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return {
                "id": row[0],
                "filename": row[1],
                "source_type": row[2],
                "speaker_count": row[3],
                "created_at": row[4].isoformat()
            }
        else:
            return None
    except Exception as e:
        raise e
    
# POST transcription     
def create_transcription(filename, source_type, speaker_count):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO transcriptions (filename, source_type, speaker_count)
            VALUES (%s, %s, %s)
            RETURNING *;
        """, (filename, source_type, speaker_count))
        new_row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return {
            "id": new_row[0],
            "filename": new_row[1],
            "source_type": new_row[2],
            "speaker_count": new_row[3],
            "created_at": new_row[4].isoformat()
        }
    except Exception as e:
        raise e

# PUT transcription 
def update_transcription(id, filename, source_type, speaker_count):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE transcriptions
            SET filename = %s, source_type = %s, speaker_count = %s
            WHERE id = %s
            RETURNING *;
        """, (filename, source_type, speaker_count, id))
        updated_row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if updated_row:
            return {
                "id": updated_row[0],
                "filename": updated_row[1],
                "source_type": updated_row[2],
                "speaker_count": updated_row[3],
                "created_at": updated_row[4].isoformat()
            }
        else:
            return None
    except Exception as e:
        raise e
    
# DELETE transcription 
def delete_transcription(id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM transcriptions WHERE id = %s RETURNING *;", (id,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return deleted is not None
    except Exception as e:
        raise e