from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class AddFileUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add File")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # File name input
        name_layout = QHBoxLayout()
        name_label = QLabel("File Name:")
        self.name_input = QLineEdit()
        
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        
        # File tag input
        tag_layout = QHBoxLayout()
        tag_label = QLabel("File Tag:")
        self.tag_input = QLineEdit()
        
        
        
        