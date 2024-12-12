import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.QtCore import QDate
import sqlite3

class AddTask(QDialog):
    def __init__(self):
        super(AddTask, self).__init__()
        loadUi("src/ui/add_task_ui.ui", self)
        self.add.clicked.connect(self.addtask)
        self.cancel.clicked.connect(self.home)
        self.date.setDate(QDate.currentDate())
        

    def addtask(self):
        name = self.name.text()
        description = self.description.toPlainText()
        date = self.date.date().toString("dd-MM-yyyy") 
        category = self.category.currentText()
        tag = self.tag.text()

        if (len(name) == 0 or len(date) == 0):
            if len(name) == 0:
                self.nameWarning.setText("Name cannot be blank!")
        else:
            try:
                conn = sqlite3.connect("tasks.db")
                cur = conn.cursor()

                query = """
                INSERT INTO Task (title, description, dueDate, category, tag)
                VALUES (?, ?, ?, ?, ?)
                """
                cur.execute(query, (name, description, date, category, tag))
                conn.commit()
                conn.close()

                print("Task added successfully!")
                self.nameWarning.setText("")
                self.name.setText("")
                self.description.setText("")
                self.tag.setText("")
            except sqlite3.Error as e:
                print("Error while inserting task:", e)
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

