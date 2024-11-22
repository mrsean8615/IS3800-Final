import sqlite3

def db(): 
    conn = sqlite3.connect('db/users.db') 
    cursor = conn.cursor() 
    return conn, cursor
