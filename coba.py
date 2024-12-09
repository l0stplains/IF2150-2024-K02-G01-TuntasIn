from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sqlite3
from src.ui.calendar_ui import CalendarUi
import sys

if __name__ == "__main__":
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    # Ensure the database exists
    db_path = "tasks.db"
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
    calendar = CalendarUi(db_path)
    calendar.show()

    sys.exit(app.exec_())
