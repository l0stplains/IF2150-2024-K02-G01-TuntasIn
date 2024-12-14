import sys
import os

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import sqlite3


from PyQt5.QtWidgets import QMessageBox


class EditViewController:

    def __init__(self, ui, taskId):
        self.ui = ui
        self.taskId = taskId  
        self.DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database.db')

        self.setup_connections()
        self.load_task_details()

    def setup_connections(self):
        self.ui.add.clicked.connect(self.edit_task)
        self.ui.cancel.clicked.connect(self.home)
        self.ui.date.setDate(QDate.currentDate())

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
                    self.ui.date.setDate(QDate.fromString(due_date, "dd-MM-yyyy"))
                    index = self.ui.category.findText(category)
                    if index != -1:
                        self.ui.category.setCurrentIndex(index)

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

    def edit_task(self):

        task_details = self.get_task_details()
        name, description, date, category, tags = (
            task_details["name"],
            task_details["description"],
            task_details["date"],
            task_details["category"],
            task_details["tags"],
        )

        if not name:
            self.ui.nameWarning.setText("Name cannot be blank!")
            return

        try:
            with sqlite3.connect(self.DB_PATH) as conn:
                cur = conn.cursor()

                # Update task details
                query1 = """
                UPDATE Task
                SET title = ?, description = ?, dueDate = ?, category = ?
                WHERE taskId = ?
                """
                cur.execute(query1, (name, description, date, category, self.taskId))

                # Remove old tags
                query2 = """
                DELETE FROM tags
                WHERE task_id = ?
                """
                cur.execute(query2, (self.taskId,))

                query3 = """
                INSERT INTO tags (task_id, name)
                VALUES (?, ?)
                """
                for tag in tags:
                    if tag:
                        cur.execute(query3, (self.taskId, tag))

                conn.commit()

                QMessageBox.information(None, "Success", "Task edited successfully!")

        except sqlite3.Error as e:
            QMessageBox.critical(None, "Error", f"Failed to edit task: {e}")

    def get_task_details(self):
        """
        Collect all task details from the UI fields.
        """
        return {
            "name": self.ui.name.text(),
            "description": self.ui.description.toPlainText(),
            "date": self.ui.date.date().toString("dd-MM-yyyy"),
            "category": self.ui.category.currentText(),
            "tags": [
                self.ui.tag1.text().strip(),
                self.ui.tag2.text().strip(),
                self.ui.tag3.text().strip(),
                self.ui.tag4.text().strip(),
                self.ui.tag5.text().strip(),
            ],
        }

    def home(self):
        """
        Handle cancel action.
        """
        QMessageBox.information(None, "Cancel", "Operation cancelled.")
        self.ui.close()