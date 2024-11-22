from db import db

conn, cursor = db()

cursor.execute("""
SELECT * from users;
""")
users = cursor.fetchall()
print(users)

