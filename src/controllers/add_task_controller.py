import sys
import os

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import sqlite3
from src.ui.add_task_ui import AddTaskUI
from src.controllers.add_file_controller import AddFileController


from PyQt5.QtWidgets import QMessageBox


class AddTaskController:

    def __init__(self, ui):
        """
        Initialize the controller with a reference to the UI instance.
        """
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        self.ui.add.clicked.connect(self.add_task)
        self.ui.cancel.clicked.connect(self.home)
        self.ui.date.setDate(QDate.currentDate())

    def add_task(self):
        name = self.ui.name.text()
        description = self.ui.description.toPlainText()
        date = self.ui.date.date().toString("dd-MM-yyyy")
        category = self.ui.category.currentText()

        tags = [
            self.ui.tag1.text().strip(),
            self.ui.tag2.text().strip(),
            self.ui.tag3.text().strip(),
            self.ui.tag4.text().strip(),
            self.ui.tag5.text().strip(),
        ]

        if len(name) == 0:  # Validate required fields
            self.ui.nameWarning.setText("Name cannot be blank!")
            return

        try:
            DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database.db')

            # Then in the add_task method:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            # Insert task into Task table
            query1 = """
            INSERT INTO Task (title, description, dueDate, category)
            VALUES (?, ?, ?, ?)
            """
            cur.execute(query1, (name, description, date, category))

            # Get the taskId of the newly inserted task
            task_id = cur.lastrowid

            # Insert tags into Tag table
            query2 = """
            INSERT INTO tags (task_id, name)
            VALUES (?, ?)
            """
            for tag in tags:
                if tag:  # Only insert non-empty tags
                    cur.execute(query2, (task_id, tag))

            # Commit the transaction
            conn.commit()
            conn.close()

            # Clear the form fields after successful insertion
            print("Task and tags added successfully!")
            self.ui.nameWarning.setText("")
            self.ui.name.setText("")
            self.ui.description.setText("")
            self.ui.tag1.setText("")
            self.ui.tag2.setText("")
            self.ui.tag3.setText("")
            self.ui.tag4.setText("")
            self.ui.tag5.setText("")

            # Show success message box (using self.ui as the parent)
            QMessageBox.information(None, "Success", "Task and tags added successfully!")

        except sqlite3.Error as e:
            print("Error while inserting task or tags:", e)
            # Show error message box
            QMessageBox.critical(None, "Error", f"Failed to add task and tags: {e}")

    def home(self):
        QMessageBox.information(None, "Cancel", "Operation cancelled.")
        self.ui.close()
