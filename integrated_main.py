import sys
from src.ui.home_ui import HomeUI
from src.ui.calendar_ui import CalendarUi
from src.controllers.home_controller import HomeController
from src.components.navbar import NavBar
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedWidget
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
        self.folder_ui = QWidget()  # Replace with your actual folder UI
        self.calendar_ui = CalendarUi("tasks.db")  # Replace with your actual calendar UI
        self.progress_ui = QWidget()  # Replace with your actual progress UI
        
        self.stacked_widget.addWidget(self.home_ui)
        self.stacked_widget.addWidget(self.folder_ui)
        self.stacked_widget.addWidget(self.calendar_ui)
        self.stacked_widget.addWidget(self.progress_ui)
        
        # Set window properties
        self.setMinimumSize(1280, 720)
             
        # Connect navbar signals to switch pages
        self.navbar.home_clicked.connect(lambda: self.switch_page(self.home_ui))
        self.navbar.folder_clicked.connect(lambda: self.switch_page(self.folder_ui))
        self.navbar.calendar_clicked.connect(lambda: self.switch_page(self.calendar_ui))
        self.navbar.progress_clicked.connect(lambda: self.switch_page(self.progress_ui))
        
    def switch_page(self, page):
        """Switch to the given page."""
        self.stacked_widget.setCurrentWidget(page)
        

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