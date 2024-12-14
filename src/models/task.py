import sqlite3

class TaskModel:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.create_table()

    def create_table(self):
        # Create table with due_time column
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            due_time TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, name, due_date, due_time):
        # Add task with due_time
        query = "INSERT INTO tasks (name, due_date, due_time) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, due_date, due_time))
        self.conn.commit()

    def get_all_tasks(self):
        # Add all task from database
        query = "SELECT id, name, due_date, due_time, status FROM tasks"
        return self.conn.execute(query).fetchall()
