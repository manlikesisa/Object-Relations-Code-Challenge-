from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")

    
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Smith",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Alice Johnson",))

    
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Weekly", "Health"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Art Monthly", "Art"))

    
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("AI in 2025", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Wellness Tips", 2, 2))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Modern Sculpture", 3, 3))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Quantum Computing", 1, 1))

    conn.commit()
    conn.close()
    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed()