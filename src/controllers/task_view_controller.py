import sys
import os

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import sqlite3

from PyQt5.QtWidgets import QMessageBox


class TaskViewController:
    def __init__(self, ui, taskId):
        self.ui = ui
        self.taskId = taskId  
        self.DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database.db')
        self.setup_connections()
        self.load_task_details()

    def setup_connections(self):
        self.ui.back.clicked.connect(self.ui.widget.parent().close)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.edit.clicked.connect(self.edit)
        self.ui.file.clicked.connect(self.query_filepath)

    def query_filepath(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            # Check if the task exists in the Task table
            query_task = "SELECT filePath FROM Attachment WHERE taskId = ?"
            cursor = conn.execute(query_task, (self.taskId,))
            task = cursor.fetchone()

        if not task:
            QMessageBox.warning(None, "Warning", f"No task exists!")
            return
        self.open_file(task[0])
            
    def open_file(self, file_path):
        if os.path.exists(file_path):
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(file_path)
                elif os.name == 'posix':  # macOS/Linux
                    subprocess.run(["xdg-open", file_path], check=True)
                else:
                    QMessageBox.warning(self.folder_ui, "Error", "Unsupported operating system.")
            except Exception as e:
                QMessageBox.warning(self.folder_ui, "Error", f"Failed to open file: {str(e)}")
        else:
            QMessageBox.warning(self.folder_ui, "Error", f"File does not exist: {file_path}")

    def load_task_details(self):
        try:
            with sqlite3.connect(self.DB_PATH) as conn:
                cur = conn.cursor()

                query1 = """
                SELECT title, description, dueDate, category
                FROM Task
                WHERE taskId = ?
                """
                cur.execute(query1, (self.taskId,))
                task = cur.fetchone()

                if task:  
                    title, description, due_date, category = task
                    self.ui.name.setText(title)
                    self.ui.description.setPlainText(description)
                    self.ui.date.setText(QDate.fromString(due_date, "dd-MM-yyyy").toString("dd-MM-yyyy"))
                    index = self.ui.category.setText(category)
            

                # Fetch tags associated with the task
                query2 = """
                SELECT name
                FROM tags
                WHERE task_id = ?
                """
                cur.execute(query2, (self.taskId,))
                tags = [tag[0] for tag in cur.fetchall()]  

                tag_fields = [self.ui.tag1, self.ui.tag2, self.ui.tag3, self.ui.tag4, self.ui.tag5]
                for i, tag in enumerate(tags):
                    if i < len(tag_fields):
                        tag_fields[i].setText(tag)

        except sqlite3.Error as e:
            QMessageBox.critical(None, "Error", f"Failed to load task details: {e}")
    def delete(self):
        pass
    def edit(self):
        pass
    def home(self):
        QMessageBox.information(None, "Cancel", "Operation cancelled.")
        self.ui.close()
