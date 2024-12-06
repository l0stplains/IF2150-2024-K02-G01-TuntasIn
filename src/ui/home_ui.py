from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QLineEdit, QDateEdit


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.resize(800, 600)

        # Layout and widgets
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.task_name_input = QLineEdit()
        self.due_date_input = QDateEdit()
        self.add_task_button = QPushButton("Add Task")
        self.refresh_button = QPushButton("Refresh")
        self.task_list = QListWidget()

        layout.addWidget(self.task_name_input)
        layout.addWidget(self.due_date_input)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.task_list)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_task_list(self, tasks):
        self.task_list.clear()
        for task in tasks:
            self.task_list.addItem(f"{task[1]} (Due: {task[2]}) - {task[3]}")
