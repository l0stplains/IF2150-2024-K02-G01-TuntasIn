import sys
from PyQt5.QtWidgets import QApplication
from src.ui.add_file_ui import AddFileUI
from src.controllers.add_file_controller import AddFileController
from src.components.navbar import NavBar
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
# from src.setup_database import setup_database  # Tambahkan ini

class Add_File_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tuntasin")
        self.setup_ui()
        
    def setup_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Add navbar
        self.navbar = NavBar()
        layout.addWidget(self.navbar)
        
        # Add home widget
        self.add_file_ui = AddFileUI()
        self.add_file_controller = AddFileController(self.add_file_ui)
        # self.home_controller = HomeController(self.home_ui)
        layout.addWidget(self.add_file_ui)
        
        # Set window properties
        self.setMinimumSize(800, 600)
        # Ensure widgets fill space properly
        layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins if necessary
        layout.setSpacing(20)  # Adjust spacing between widgets
        layout.addStretch(1)  # Add stretch to allow the layout to adjust space
        
        # Connect navbar signals
        # self.navbar.home_clicked.connect(lambda: self.home_ui.show())
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
    
    # Load stylesheet
    try:
        with open('src/styles/main.qss', 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: style.qss not found")
    
    window = Add_File_Main()
    window.show()
    
    sys.exit(app.exec_())