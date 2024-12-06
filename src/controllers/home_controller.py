from PyQt5.QtWidgets import QMessageBox
from src.models.task import TaskModel


class HomeController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.task_model = TaskModel()

        # Connect UI signals to methods
        self.main_window.add_task_button.clicked.connect(self.add_task)
        self.main_window.refresh_button.clicked.connect(self.refresh_tasks)

        # Initial data load
        self.refresh_tasks()

    def add_task(self):
        # Collect task details from the UI
        task_name = self.main_window.task_name_input.text()
        due_date = self.main_window.due_date_input.date().toString("yyyy-MM-dd")

        # Add task to the database
        if task_name:
            self.task_model.add_task(task_name, due_date)
            QMessageBox.information(
                self.main_window, "Success", "Task added successfully!")
            self.refresh_tasks()
        else:
            QMessageBox.warning(self.main_window, "Error",
                                "Task name cannot be empty!")

    def refresh_tasks(self):
        # Fetch tasks and update the UI
        tasks = self.task_model.get_all_tasks()
        self.main_window.update_task_list(tasks)
