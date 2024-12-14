import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QWidget, QScrollArea
from src.ui.add_task_ui import AddTaskUI
from src.controllers.add_task_controller import AddTaskController


class Add_Task_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tuntasin")
        self.setup_ui()

    def setup_ui(self):
        
        self.setFixedSize(1280, 720)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  
        layout.setSpacing(0)  
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  
        scroll_area.setContentsMargins(0, 0, 0, 0) 
        layout.addWidget(scroll_area)

        self.add_task_dialog = QDialog(self)  
        self.add_task_ui = AddTaskUI(self.add_task_dialog)  
        self.add_task_dialog.setMinimumSize(1250, 975)  

        scroll_area.setWidget(self.add_task_dialog)

        self.add_task_controller = AddTaskController(self.add_task_ui)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("src/styles/main.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: main.qss not found")

    window = Add_Task_Main()
    window.show()

    sys.exit(app.exec_())
