import sqlite3

class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    faculty TEXT NOT NULL)'''
        self.conn.execute(query)
        self.conn.commit()

    def add_student(self, name, surname, age, faculty):
        query = "INSERT INTO students (name, surname, age, faculty) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (name, surname, age, faculty))
        self.conn.commit()

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = ?"
        self.conn.execute(query, (student_id,))
        self.conn.commit()

    def get_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
