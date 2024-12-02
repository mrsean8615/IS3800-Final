from db.db import dbConnect
conn, cursor = dbConnect()


def createDB():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fname VARCHAR(30) NOT NULL,
            lname VARCHAR(30) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(60) NOT NULL,
            password VARCHAR(45)
        )
    """)
    conn.commit()


def insertUsers():
    createDB()
    users = [
        ("Alice", "Smith", 30, "alice.smith@example.com", "pass")
    ]

    cursor.executemany("INSERT INTO users (fname, lname, age, email, password) VALUES (?, ?, ?, ?, ?)", users)

    conn.commit()
    conn.close()


insertUsers()