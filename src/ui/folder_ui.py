from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QScrollArea, QMessageBox
from PyQt5.QtGui import QPixmap, QFontMetrics
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import os
from src.models.folder import FileModel
from PyQt5.QtWidgets import QMessageBox


class FileFolderUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File and Folder Explorer")
        self.setGeometry(100, 100, 800, 600)
        self.file_model = FileModel("database.db")

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)  # Changed to QVBoxLayout for buttons at the top

        # Add and Filter Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")

        button_layout.addStretch()  # Push buttons to the right
        self.add_button.setFixedWidth(500)

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
        
        # Add buttons to layout
        button_layout.addWidget(self.add_button)
        button_layout.addStretch()  # Push buttons to the left

        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        # Scrollable area for the grid
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Container for the grid layout
        grid_container = QWidget()
        self.grid_layout = QGridLayout(grid_container)
        self.grid_layout.setHorizontalSpacing(10)  # Keep horizontal spacing larger
        self.grid_layout.setVerticalSpacing(10)  # Reduce vertical gap
        # grid_layout.rowStretch(100)  # Push everything to the top 
        
        # Set the stylesheet for grid_container
        grid_container.setStyleSheet("""
            QWidget {
                background: #dce0f5;
                border-radius: 10px;      /* Optional rounded corners */
            }
        """)

        # Add some cards
        self.cards = []
        
        # Set grid container as the widget for the scroll area
        scroll_area.setWidget(grid_container)
        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)
        
    def add_card(self, id, file_path, name=None, task=None):
        # Check if name and tag are provided, otherwise use defaults
        name = name or "Unnamed File"
        task = task or "No Task"

        # Use default or dynamic icon based on file extension
        if name.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            icon_path = "img/image.png"
        elif name.endswith((".docx")):
            icon_path = "img/word.png"
        elif name.endswith((".pdf")):
            icon_path = "img/pdf.png"
        elif name.endswith((".txt")):
            icon_path = "img/txt.png"

        # Create the card widget
        card = Card(id, name, task, icon_path, file_path, self)
        row, col = len(self.cards) // 3, len(self.cards) % 3  # 3 cards per row

        # Add the card to the grid layout
        self.grid_layout.addWidget(card, row, col)
        self.cards.append(card)
        
    def delete_card(self, attachment_id):
        """
        Delete the card and remove the associated file record from the database.
        """
        
        card_to_delete = next((card for card in self.cards if card.attachment_id == attachment_id), None)
        if card_to_delete:
            self.file_model.delete_file(attachment_id)  # Remove the file from the database
            self.cards.remove(card_to_delete)  # Remove the card from the list
            card_to_delete.deleteLater()  # Remove card widget from the UI
        else:
            QMessageBox.warning(self, "Error", "Card not found!")



class Card(QWidget):
    def __init__(self, attachment_id, name, task, icon_path, file_path, parent=None):
        super().__init__(parent)
        self.attachment_id = attachment_id  # Store the unique attachment ID
        self.file_path = file_path
        self.parent_ui = parent  # Store the parent UI (FileFolderUI) instance
        self.setMaximumWidth(400)
        self.setMaximumHeight(400)
        self.setStyleSheet("""
            QWidget {   
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #fff;
            }
        """)

        # Vertical layout for the card
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        # Icon/Image
        icon_label = QLabel(self)
        icon_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(icon_path).scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)

        # Title
        title_label = QLabel(name, self)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setFixedHeight(30)

        # Description
        task_label = QLabel(task, self)
        task_label.setStyleSheet("font-size: 12px; color: #666;")
        task_label.setAlignment(Qt.AlignCenter)
        task_label.setWordWrap(True)
        task_label.setFixedHeight(20)

        # Truncate title if it's too long
        font_metrics = QFontMetrics(title_label.font())
        max_width = title_label.width() - 20
        title_width = font_metrics.width(name)
        task_width = font_metrics.width(task)

        if title_width > max_width:
            truncated_title = font_metrics.elidedText(name, Qt.ElideRight, max_width)
            truncated_task = font_metrics.elidedText(task, Qt.ElideRight, max_width)
            title_label.setText(truncated_title)
            task_label.setText(truncated_task)

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
        self.open_file_button.clicked.connect(self.open_file_from_card)

        # Delete button (X button)
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                background-color: red;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        self.delete_button.clicked.connect(self.delete_card)

        # Add widgets to layout
        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(task_label)
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.delete_button)

    def delete_card(self):
        # Directly call the delete_card method of FileFolderUI instance (parent_ui)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Confirm Delete")
        msg_box.setText("Are you sure you want to delete this file?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Manually set button texts
        yes_button = msg_box.button(QMessageBox.Yes)
        yes_button.setText("Yes")
        no_button = msg_box.button(QMessageBox.No)
        no_button.setText("No")

        # Tampilkan QMessageBox
        reply = msg_box.exec_()
        if reply == QMessageBox.Yes:
            if self.parent_ui:
                self.parent_ui.delete_card(self.attachment_id)

    def open_file_from_card(self):
        """Open the file associated with the current card."""
        if not self.file_path:
            QMessageBox.warning(self, "Error", "File path not found!")
            return

        if os.path.exists(self.file_path):
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(self.file_path)
                elif os.name == 'posix':  # macOS/Linux
                    subprocess.run(["xdg-open", self.file_path], check=True)
                else:
                    QMessageBox.warning(self, "Error", "Unsupported operating system.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to open file: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", f"File does not exist: {self.file_path}")


# Run the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FileFolderUI()
    window.show()
    sys.exit(app.exec_())
