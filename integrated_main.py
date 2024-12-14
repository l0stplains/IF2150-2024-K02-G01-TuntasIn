import sys
from src.ui.home_ui import HomeUI
from src.ui.calendar_ui import CalendarUi
from src.ui.progress_ui import ProgressWindow
from src.ui.folder_ui import FileFolderUI
from src.ui.add_file_ui import AddFileUI
from src.ui.add_task_ui import AddTaskUI
from src.controllers.folder_controller import FolderController
from src.controllers.add_file_controller import AddFileController
from src.controllers.add_task_controller import AddTaskController
from src.controllers.home_controller import HomeController
from src.components.navbar import NavBar
from src.controllers.calendar_controller import CalendarController
from src.controllers.progress_controller import ProgressController
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QDialog, QScrollArea
from PyQt5.QtCore import Qt
# from src.setup_database import setup_database  # Tambahkan ini

class MainWindow(QMainWindow):
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TuntasIn")
        self.setup_ui()
        
    def setup_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Add navbar
        self.navbar = NavBar()
        layout.addWidget(self.navbar)
        
        # Add stacked widget for page management
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Add pages to stacked widget
        self.home_ui = HomeUI()
        self.home_controller = HomeController(self.home_ui)
        self.folder_ui = FileFolderUI()
        self.add_file_ui = AddFileUI()
        self.add_task_ui = AddTaskUI()  
        self.calendar_ui = CalendarUi("database.db")  # Replace with your actual calendar UI
        self.progress_ui = ProgressWindow()  # Replace with your actual progress UI
        self.progress_ui.set_progress_controller(ProgressController(self.progress_ui, "database.db"))
        
        self.stacked_widget.addWidget(self.home_ui)
        self.stacked_widget.addWidget(self.folder_ui)
        self.stacked_widget.addWidget(self.calendar_ui)
        self.stacked_widget.addWidget(self.progress_ui)
        self.stacked_widget.addWidget(self.add_file_ui)
        self.stacked_widget.addWidget(self.add_task_ui)

        # Create controllers
        self.folder_controller = FolderController(self.folder_ui, self.add_file_ui)
        self.add_file_controller = AddFileController(self.add_file_ui, isInside=True)
        self.add_task_controller = AddTaskController(self.add_task_ui)
        
        # Set window properties
        self.setMinimumSize(1280, 1050)
             
        # Connect navbar signals to switch pages
        self.navbar.home_clicked.connect(self.show_home)
        self.navbar.folder_clicked.connect(lambda: self.switch_page(self.folder_ui))
        self.navbar.calendar_clicked.connect(lambda: self.switch_page(self.calendar_ui))
        self.navbar.progress_clicked.connect(lambda: self.switch_page(self.progress_ui))
        self.folder_ui.add_button.clicked.connect(self.show_add_file)
        self.add_file_ui.pushButtonBatal.clicked.connect(self.show_folder)
        self.home_ui.add_btn.clicked.connect(lambda: self.switch_page(self.add_task_ui))
        
    def switch_page(self, page):
        """Switch to the given page."""
        self.stacked_widget.setCurrentWidget(page)

    def show_folder(self):
        self.folder_controller.load_files_from_database()
        self.stacked_widget.setCurrentWidget(self.folder_ui)

    def show_add_file(self):
        # Show the add file view
        self.stacked_widget.setCurrentWidget(self.add_file_ui)

    def show_add_task(self):
        self.stacked_widget.setCurrentWidget(self.add_task_ui)
    def show_home(self):
        self.home_controller.load_tasks()
        self.stacked_widget.setCurrentWidget(self.home_ui)
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