import sqlite3
from pathlib import Path

def setup_database():
    db_path = Path("lib/db/magazine.db")  
    schema_path = Path("lib/db/schema.sql")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(schema_path, "r") as schema_file:
        schema_sql = schema_file.read()
        cursor.executescript(schema_sql)

    conn.commit()
    conn.close()
    print(" Database setup complete!")

if __name__ == "__main__":
    setup_database()