import sqlite3
from datetime import datetime


class CalendarController:
    def __init__(self, db_path):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """Create a database schema if it doesn't exist."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """
        )
        connection.commit()
        connection.close()

    def get_tasks_for_date(self, date):
        """Fetch tasks for a specific date."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = """
        SELECT t.taskId, t.title, t.category, t.isComplete, t.dueDate, GROUP_CONCAT(tag.name)
        FROM Task t
        LEFT JOIN tags tag ON t.taskId = tag.task_id
        WHERE t.dueDate LIKE ?
        GROUP BY t.taskId
"""
        date_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        # Format the datetime object into the desired format
        formatted_date = date_object.strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute(query, (formatted_date,))
        tasks = [(row[1], row[3], row[4]) for row in cursor.fetchall()]
        connection.close()
        return tasks
