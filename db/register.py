from db.db import db
from werkzeug.security import generate_password_hash

def register_user(fname, lname, age, email, password):
    try:

        conn, cursor = db()

        hashed_password = generate_password_hash(password)

        query = """
        INSERT INTO users (fname, lname, age, email, password) 
        VALUES (?, ?, ?, ?, ?);
        """
        cursor.execute(query, (fname, lname, age, email, hashed_password))
        conn.commit()
        conn.close()

        return True
    except:
        return False


