import sqlite3

class ProgressModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get_completed_tasks_per_week(self, month, year):
        query = """
        SELECT 
            ((CAST(strftime('%d', due_date) AS INTEGER) - 1) / 7) + 1 AS week,  -- Menghitung minggu dalam bulan
            COUNT(*) AS task_count
        FROM tasks
        WHERE status = 'Completed'
          AND strftime('%m', due_date) = ?   -- Filter berdasarkan bulan
          AND strftime('%Y', due_date) = ?   -- Filter berdasarkan tahun
        GROUP BY week
        ORDER BY week;  -- Mengurutkan hasil berdasarkan minggu
        """
        cursor = self.conn.execute(query, (month, year))
        data = cursor.fetchall()
        cursor.close()  # Pastikan cursor ditutup
        return data
