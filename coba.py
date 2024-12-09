from PyQt5.QtWidgets import QApplication
import sqlite3
from src.ui.calendar_ui import CustomCalendar
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Ensure the database exists
    db_path = "awok.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        due_date DATE NOT NULL
    );
    """)
    conn.close()

    # Launch the custom calendar
    calendar = CustomCalendar(db_path)
    calendar.show()

    sys.exit(app.exec_())
