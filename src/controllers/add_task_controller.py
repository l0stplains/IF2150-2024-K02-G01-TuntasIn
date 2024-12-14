import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QMessageBox
from PyQt5.QtCore import QDate
import sqlite3

class AddTask(QDialog):
    def __init__(self):
        super(AddTask, self).__init__()
        loadUi("../ui/add_task_ui.ui", self)
        self.add.clicked.connect(self.addtask)
        self.cancel.clicked.connect(self.home)
        self.date.setDate(QDate.currentDate())
        

    def addtask(self):
        name = self.name.text()
        description = self.description.toPlainText()
        date = self.date.date().toString("dd-MM-yyyy") 
        category = self.category.currentText()
        
        tags = [
            self.tag1.text().strip(),
            self.tag2.text().strip(),
            self.tag3.text().strip(),
            self.tag4.text().strip(),
            self.tag5.text().strip(),
        ]

        if len(name) == 0:  # Validate required fields
            self.nameWarning.setText("Name cannot be blank!")
            return

        try:
            conn = sqlite3.connect("../../tasks.db")
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
            self.nameWarning.setText("")
            self.name.setText("")
            self.description.setText("")
            self.tag1.setText("")
            self.tag2.setText("")
            self.tag3.setText("")
            self.tag4.setText("")
            self.tag5.setText("")
            
            # Show success message box
            QMessageBox.information(self, "Success", "Task and tags added successfully!")

        except sqlite3.Error as e:
            print("Error while inserting task or tags:", e)
            # Show error message box
            QMessageBox.critical(self, "Error", f"Failed to add task and tags: {e}")


    def home(self):
        pass
app = QApplication(sys.argv)
addtask = AddTask()
widget = QStackedWidget()
widget.addWidget(addtask)

widget.setFixedHeight(1024)
widget.setFixedWidth(1280)
widget.show()

try:
    sys.exit(app.exec())
except Exception as e:
    print("Exiting:", e)