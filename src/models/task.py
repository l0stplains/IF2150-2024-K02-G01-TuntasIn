import sqlite3


class TaskModel:
    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, name, due_date):
        query = "INSERT INTO tasks (name, due_date) VALUES (?, ?)"
        self.conn.execute(query, (name, due_date))
        self.conn.commit()

    def get_all_tasks(self):
        query = "SELECT id, name, due_date, status FROM tasks"
        return self.conn.execute(query).fetchall()
