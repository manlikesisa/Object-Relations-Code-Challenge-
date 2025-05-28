from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?",
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Article(row[1], row[2], row[3], row[0]) for row in rows]

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute(
                """
                UPDATE articles
                SET title = ?, author_id = ?, magazine_id = ?
                WHERE id = ?
                """,
                (self.title, self.author_id, self.magazine_id, self.id)
            )
        else:
            cursor.execute(
                """
                INSERT INTO articles (title, author_id, magazine_id)
                VALUES (?, ?, ?)
                """,
                (self.title, self.author_id, self.magazine_id)
            )
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, author_id, magazine_id FROM articles WHERE id = ?",
            (id,)
        )
        row = cursor.fetchone()
        conn.close()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, author_id, magazine_id FROM articles WHERE title = ?",
            (title,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?",
            (author_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?",
            (magazine_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5:
            raise ValueError("Title must be a string with at least 5 characters")
        self._title = value

    def author(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name FROM authors WHERE id = ?",
            (self.author_id,)
        )
        row = cursor.fetchone()
        conn.close()
        return Author(row[1], row[0]) if row else None

    def magazine(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, category FROM magazines WHERE id = ?",
            (self.magazine_id,)
        )
        row = cursor.fetchone()
        conn.close()
        return Magazine(row[1], row[2], row[0]) if row else None