import sqlite3


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
SELECT t.id, t.name, t.category, t.status, t.due_date, GROUP_CONCAT(tag.name) AS tags
FROM tasks t
LEFT JOIN tags tag ON t.id = tag.task_id
WHERE t.due_date = ?
GROUP BY t.id;
"""
        cursor.execute(query, (date,))
        tasks = [row[1] for row in cursor.fetchall()]
        connection.close()
        return tasks
