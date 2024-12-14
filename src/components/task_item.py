from PyQt5.QtWidgets import QMessageBox
from src.utils.database import add_task, get_all_tasks

class HomeController:
    def __init__(self, main_window):
        self.main_window = main_window

        # Connect UI signals to methods
        self.main_window.add_task_button.clicked.connect(self.add_task)
        self.main_window.refresh_button.clicked.connect(self.refresh_tasks)

        # Initial data load
        self.refresh_tasks()

    def add_task(self):
        # Mengumpulkan detail tugas dari UI
        task_name = self.main_window.task_name_input.text()
        due_date = self.main_window.due_date_input.date().toString("yyyy-MM-dd")
        due_time = self.main_window.due_time_input.text()  # Asumsikan Anda memiliki input waktu

        # Menambahkan tugas ke database
        if task_name and due_time:  # Pastikan due_time ada
            add_task(task_name, due_date, due_time)
            QMessageBox.information(self.main_window, "Success", "Task added successfully!")
            self.refresh_tasks()
        else:
            QMessageBox.warning(self.main_window, "Error", "Task name or due time cannot be empty!")

    def refresh_tasks(self):
        # Fetch tasks and update the UI
        tasks = get_all_tasks()
        self.main_window.update_task_list(tasks)
