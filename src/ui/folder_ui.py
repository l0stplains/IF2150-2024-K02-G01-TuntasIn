from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class FileFolderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File and Folder Explorer")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)  # Changed to QVBoxLayout for buttons at the top

        # Add and Filter Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.filter_button = QPushButton("Filter")

        button_layout.addStretch()  # Push buttons to the right
        self.add_button.setFixedWidth(120)
        self.filter_button.setFixedWidth(120)

        # Style buttons (optional)
        self.add_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.filter_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                background-color: #28A745;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)

        # Add buttons to layout
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.filter_button)
        button_layout.addStretch()  # Push buttons to the left

        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        # Scrollable area for the grid
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Container for the grid layout
        grid_container = QWidget()
        grid_layout = QGridLayout(grid_container)
        grid_layout.setSpacing(20)  # Add spacing between cards
        
        # Set the stylesheet for grid_container
        grid_container.setStyleSheet("""
            QWidget {
                background: #dce0f5;
                border-radius: 10px;      /* Optional rounded corners */
            }
        """)

        # Add some cards
        self.cards = []
        cards = [
            ("Title 1", "This is the first card.", "img/pdf.png"),
            ("Title 2", "This is the second card.", "img/txt.png"),
            ("Title 3", "This is the third card.", "img/word.png"),
            ("Title 4", "This is the fourth card.", "img/pdf.png"),
            ("Title 5", "This is the fifth card.", "img/txt.png"),
            ("Title 6", "This is the sixth card.", "img/word.png"),
        ]

        row, col = 0, 0
        for title, description, icon in cards:
            card = Card(title, description, icon, self)
            grid_layout.addWidget(card, row, col)
            
            self.cards.append(card)  # Store the card reference

            col += 1
            if col > 2:  # Limit to 3 cards per row
                col = 0
                row += 1

        # Set grid container as the widget for the scroll area
        scroll_area.setWidget(grid_container)

        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)


class Card(QWidget):
    def __init__(self, title: str, description: str, icon_path: str, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 250)  # Set the card's size

        # # Add shadow effect
        # shadow = QGraphicsDropShadowEffect(self)
        # shadow.setBlurRadius(15)  # Adjust the blur radius
        # shadow.setXOffset(5)  # Horizontal offset
        # shadow.setYOffset(5)  # Vertical offset
        # shadow.setColor(Qt.gray)  # Shadow color
        # self.setGraphicsEffect(shadow)

        self.setStyleSheet("""
            QWidget {   
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #fff;
            }
        """)

        # Vertical layout for the card
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Add padding inside the card
        layout.setSpacing(10)

        # Icon/Image
        icon_label = QLabel(self)
        icon_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(icon_path).scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)

        # Title
        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        title_label.setAlignment(Qt.AlignCenter)

        # Description
        desc_label = QLabel(description, self)
        desc_label.setStyleSheet("font-size: 12px; color: #666;")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)  # Enable text wrapping for long descriptions

        # Open File button
        self.open_file_button = QPushButton("Open File", self)
        self.open_file_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Add widgets to layout
        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addWidget(self.open_file_button)
        layout.addStretch()  # Push everything to the top


# Run the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FileFolderUI()
    window.show()
    sys.exit(app.exec_())
