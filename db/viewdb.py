from db import dbConnect

conn, cursor = dbConnect()

cursor.execute("""
SELECT * from users;
""")
users = cursor.fetchall()
print(users)

