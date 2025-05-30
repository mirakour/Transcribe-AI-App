from db.client import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transcriptions;")
    count = cursor.fetchone()[0]
    print(f"✅ Connected! Found {count} transcriptions in the DB.")

    cursor.close()
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)