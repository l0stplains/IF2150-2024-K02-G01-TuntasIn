import sys
from PyQt5.QtWidgets import QApplication
from src.ui.home_ui import HomeUI
from src.controllers.home_controller import HomeController
from src.components.navbar import NavBar
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from src.setup_database import setup_database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TuntasIn")
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.navbar = NavBar()
        layout.addWidget(self.navbar)
        
        self.home_ui = HomeUI()
        self.home_controller = HomeController(self.home_ui)
        layout.addWidget(self.home_ui)
        
        self.setMinimumSize(1280, 720)
        
        self.navbar.home_clicked.connect(lambda: self.home_ui.show())
        self.navbar.folder_clicked.connect(self.show_folder)
        self.navbar.calendar_clicked.connect(self.show_calendar)
        self.navbar.progress_clicked.connect(self.show_progress)
        
    def show_folder(self):
        # Implement folder view
        pass
        
    def show_calendar(self):
        # Implement calendar view
        pass
        
    def show_progress(self):
        # Implement progress view
        pass

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    try:
        with open('src/styles/main.qss', 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: style.qss not found")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())