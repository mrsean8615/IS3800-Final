from db.db import db
from werkzeug.security import check_password_hash



def login_user(email, password):
        conn, cursor = db()

        query = """
        SELECT * FROM users
        WHERE email = ?;"""

        cursor.execute(query, (email,))
        result = cursor.fetchone()
        conn.close()

        if result:
                stored_pass = result[-1]

                if check_password_hash(stored_pass, password):
                    return True
                else:
                    return False
        else:
            return False




# superpassword!2B
   
print(login_user('oh@gmail.com', 'superpassword!2B'))



    