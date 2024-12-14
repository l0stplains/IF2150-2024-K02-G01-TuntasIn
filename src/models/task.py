import sqlite3


class TaskModel:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.create_table()
        self.populate_with_dummy_data()

    def create_table(self):
        # Create table with due_time column
        query = """
        CREATE TABLE IF NOT EXISTS Task (
            taskId INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            dueDate TEXT,
            time TEXT, -- Format 'HH:MM:SS'
            category TEXT,
            isComplete BOOLEAN DEFAULT FALSE
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

    def populate_with_dummy_data(self):
        """
        Check if the table is empty. If it is, populate it with some dummy data.
        """
        query = "SELECT COUNT(*) FROM Task"
        cursor = self.conn.execute(query)
        count = cursor.fetchone()[0]

        if count == 0:  # Table is empty
            dummy_data = [
                ("Task 1", "Description for Task 1",
                 "2024-12-15", "10:00:00", "Work", False),
                ("Task 2", "Description for Task 2",
                 "2024-12-16", "14:00:00", "Personal", False),
                ("Task 3", "Description for Task 3",
                 "2024-12-17", "09:30:00", "Work", True),
                ("Task 4", "Description for Task 4",
                 "2024-12-18", "16:45:00", "Hobby", False),
            ]
            query = """
            INSERT INTO Task (title, description, dueDate, time, category, isComplete)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            self.conn.executemany(query, dummy_data)
            self.conn.commit()

    def add_task(self, title, description, due_date, time, category, is_complete=False):
        query = """
        INSERT INTO Task (title, description, dueDate, time, category, isComplete)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (title, description,
                          due_date, time, category, is_complete))
        self.conn.commit()

    def get_all_tasks(self):
        query = "SELECT taskId, title, description, dueDate, time, category, isComplete FROM Task"
        return self.conn.execute(query).fetchall()


if __name__ == "__main__":
    task_model = TaskModel()
    tasks = task_model.get_all_tasks()
    for task in tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due Date: {task[3]}, "
              f"Time: {task[4]}, Category: {task[5]}, Is Complete: {task[6]}")
