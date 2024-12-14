import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QWidget, QScrollArea
from src.ui.task_view_ui import TaskViewUI
from src.controllers.task_view_controller import TaskViewController


class Task_View_Main(QMainWindow):
    def __init__(self, taskId):
        super().__init__()
        self.setWindowTitle("Tuntasin")
        self.setup_ui(taskId)

    def setup_ui(self, taskId):
        
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

        self.task_view_dialog = QDialog(self)  
        self.task_view_ui = TaskViewUI(self.task_view_dialog)  
        self.task_view_dialog.setMinimumSize(1250, 975)  

        scroll_area.setWidget(self.task_view_dialog)

        self.task_view_controller = TaskViewController(self.task_view_ui, taskId)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("src/styles/main.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: main.qss not found")

    # taskId ini harus minta dari home yaa aa repki aslinya
    taskId = 15
    window = Task_View_Main(taskId)
    window.show()

    sys.exit(app.exec_())
