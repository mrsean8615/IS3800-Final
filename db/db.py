import sqlite3
from pathlib import Path

curr_dir = Path(__file__).resolve().parent
def db(): 
    conn = sqlite3.connect(f'{curr_dir}/users.db') 
    cursor = conn.cursor() 
    return conn, cursor
