import sqlite3

class ProgressModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get_completed_tasks_per_week(self, month, year):
        query = """
        SELECT 
            ((CAST(strftime('%d', t.dueDate) AS INTEGER) - 1) / 7) + 1 AS week  -- Calculate week in the month
        FROM Task t
        LEFT JOIN tags tag ON t.taskId = tag.task_id
        WHERE t.isComplete = 0  -- Filter only completed tasks
            AND strftime('%m', t.dueDate) = ?  -- Filter by month
            AND strftime('%Y', t.dueDate) = ?  -- Filter by year
        GROUP BY week, t.taskId  -- Group by week and taskId to retain task-level details
        ORDER BY week, t.dueDate;  -- Order by week and dueDate for better readability
        """
        cursor = self.conn.execute(query, (month, year))
        data = cursor.fetchall()
        cursor.close()  # Pastikan cursor ditutup
        return data
