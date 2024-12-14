import sqlite3

class ProgressModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get_completed_tasks_per_week(self, month, year):
        query = """
        SELECT 
            ((CAST(strftime('%d', t.dueDate) AS INTEGER) - 1) / 7) + 1 AS week,  
            COUNT(DISTINCT t.taskId) as count
        FROM Task t
        LEFT JOIN tags tag ON t.taskId = tag.task_id
        WHERE t.isComplete = 1  
            AND strftime('%m', t.dueDate) = ?  
            AND strftime('%Y', t.dueDate) = ?  
        GROUP BY week  
        ORDER BY week;  
        """
        cursor = self.conn.execute(query, (month, year))
        data = cursor.fetchall()
        cursor.close()
        return data