from db import db
conn, cursor = db()


def createDB():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fname VARCHAR(30) NOT NULL,
            lname VARCHAR(30) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(60) NOT NULL
        )
    """)
    conn.commit()


def insertUsers():
    createDB()
    users = [
        ("Alice", "Smith", 30, "alice.smith@example.com"),
        ("Bob", "Jones", 25, "bob.jones@example.com"),
        ("Charlie", "Brown", 35, "charlie.brown@example.com"),
        ("Diana", "Taylor", 28, "diana.taylor@example.com"),
        ("Eve", "Davis", 22, "eve.davis@example.com"),
        ("Frank", "Miller", 40, "frank.miller@example.com"),
        ("Grace", "Wilson", 27, "grace.wilson@example.com"),
        ("Hank", "Moore", 31, "hank.moore@example.com"),
        ("Ivy", "Anderson", 26, "ivy.anderson@example.com"),
        ("Jack", "Thomas", 33, "jack.thomas@example.com"),
    ]

    cursor.executemany("INSERT INTO users (fname, lname, age, email) VALUES (?, ?, ?, ?)", users)

    conn.commit()
    conn.close()


insertUsers()