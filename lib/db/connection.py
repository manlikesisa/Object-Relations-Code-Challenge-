import sqlite3

DB_PATH = "lib/db/magazine.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
