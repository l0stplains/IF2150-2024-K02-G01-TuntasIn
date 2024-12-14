import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QWidget
from src.ui.add_task_ui import AddTaskUI
from src.controllers.add_task_controller import AddTaskController

class Add_Task_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tuntasin")
        self.setup_ui()
        
    def setup_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create a dialog to hold the UI
        self.add_task_dialog = QDialog(self)
        
        # Create AddTaskUI and set it up on the dialog
        self.add_task_ui = AddTaskUI(self.add_task_dialog)
        
        # Add the dialog to the layout
        layout.addWidget(self.add_task_dialog)
        
        # Set window properties
        self.setMinimumSize(1280, 1000)
        self.add_task_controller = AddTaskController(self.add_task_ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open('src/styles/main.qss', 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: main.qss not found")

    window = Add_Task_Main()
    window.show()
    
    sys.exit(app.exec_())