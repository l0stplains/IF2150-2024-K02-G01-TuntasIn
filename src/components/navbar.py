from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class NavBar(QWidget):
    home_clicked = pyqtSignal()
    folder_clicked = pyqtSignal()
    calendar_clicked = pyqtSignal()
    progress_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Logo/Brand
        brand = QPushButton("TuntasIn")
        brand.setObjectName("navBrand")
        brand.clicked.connect(self.home_clicked.emit)
        
        # Navigation buttons
        home_btn = QPushButton("Home")
        home_btn.setObjectName("navButton")
        home_btn.clicked.connect(self.home_clicked.emit)
        
        folder_btn = QPushButton("Folder")
        folder_btn.setObjectName("navButton")
        folder_btn.clicked.connect(self.folder_clicked.emit)
        
        calendar_btn = QPushButton("Calendar")
        calendar_btn.setObjectName("navButton")
        calendar_btn.clicked.connect(self.calendar_clicked.emit)
        
        progress_btn = QPushButton("Progress")
        progress_btn.setObjectName("navButton")
        progress_btn.clicked.connect(self.progress_clicked.emit)
        
        # Add widgets to layout
        layout.addWidget(brand)
        layout.addWidget(home_btn)
        layout.addWidget(folder_btn)
        layout.addWidget(calendar_btn)
        layout.addWidget(progress_btn)
        layout.addStretch()