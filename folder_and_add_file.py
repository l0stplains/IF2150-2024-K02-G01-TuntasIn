import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedWidget
from src.ui.folder_ui import FileFolderUI
from src.ui.add_file_ui import AddFileUI
from src.controllers.folder_controller import FolderController
from src.controllers.add_file_controller import AddFileController
from src.components.navbar import NavBar
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
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

        # Create a stacked widget to hold different views
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Create the views
        self.folder_ui = FileFolderUI()
        self.add_file_ui = AddFileUI()

        # Add the views to the stacked widget
        self.stacked_widget.addWidget(self.folder_ui)
        self.stacked_widget.addWidget(self.add_file_ui)

        # Create controllers
        self.folder_controller = FolderController(self.folder_ui, self.add_file_ui)
        self.add_file_controller = AddFileController(self.add_file_ui, True)

        # Set window properties
        self.setMinimumSize(800, 600)

        # Connect navbar signals to switch between views
        self.navbar.folder_clicked.connect(self.show_folder)
        self.folder_ui.add_button.clicked.connect(self.show_add_file)
        self.add_file_ui.pushButtonBatal.clicked.connect(self.show_folder)

    def show_folder(self):
        self.folder_controller.load_files_from_database()
        self.stacked_widget.setCurrentWidget(self.folder_ui)

    def show_add_file(self):
        # Show the add file view
        self.stacked_widget.setCurrentWidget(self.add_file_ui)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Load stylesheet
    try:
        with open('src/styles/main.qss', 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("Warning: style.qss not found")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())