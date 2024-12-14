import sys
from PyQt5.QtWidgets import QApplication
from src.ui.folder_ui import FileFolderUI
from src.ui.add_file_ui import AddFileUI
from src.controllers.folder_controller import FolderController
from src.components.navbar import NavBar
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
# from src.setup_database import setup_database  # Tambahkan ini

class Folder_Main(QMainWindow):
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
        self.folder_ui = FileFolderUI()
        self.add_file_ui = AddFileUI()
        self.folder_controller = FolderController(self.folder_ui, self.add_file_ui)
        layout.addWidget(self.folder_ui)
        
        # Set window properties
        self.setMinimumSize(800, 600)
        
        # Connect navbar signals
        # self.navbar.home_clicked.connect(lambda: self.home_ui.show())
        self.navbar.folder_clicked.connect(self.show_folder)
        self.navbar.calendar_clicked.connect(self.show_calendar)
        self.navbar.progress_clicked.connect(self.show_progress)
    
    
    def on_add_button_clicked(self):
        # Call the controller method and then close the window
        
        self.close()
        
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
    
    window = Folder_Main()
    window.show()
    
    sys.exit(app.exec_())