import sys
import os
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QWidget, 
                             QLabel, QPushButton, QLineEdit, QFileDialog, 
                             QMessageBox)
from PyQt5.QtGui import QFont

class FileModel:
    def __init__(self, db_name="files.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE Attachment (attachmentId INTEGER PRIMARY KEY AUTOINCREMENT, filePath TEXT, fileName TEXT, fileSize LONG INTEGER);|

        CREATE TABLE Task (taskId INTEGER PRIMARY KEY AUTOINCREMENT, attachmentId INTEGER, title TEXT, description TEXT, dueDate TEXT, category TEXT, isComplete BOOLEAN DEFAULT FALSE ,FOREIGN KEY (attachmentId) REFERENCES Attachment (attachmentId));

        CREATE TABLE Tag (id INTEGER PRIMARY KEY AUTOINCREMENT, task_id INTEGER NOT NULL, name TEXT NOT NULL,FOREIGN KEY (task_id) REFERENCES Task (taskId) ON DELETE CASCADE);
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_file(self, name, tag, file_path, file_data):
        query = "INSERT INTO files (name, tag, file_path, file_data) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (name, tag, file_path, file_data))
        self.conn.commit()

    def get_all_files(self):
        query = "SELECT id, name, tag, file_path FROM files"
        return self.conn.execute(query).fetchall()

    def close_connection(self):
        self.conn.close()

class AddFileUI(QWidget):
    def __init__(self, file_model):
        super().__init__()
        self.file_model = file_model
        self.selected_file_path = None
        self.setupUi()

    def setupUi(self):
        # [Most of the previous UI setup code remains the same]
        # Just add methods for file selection and adding files

    def open_file_dialog(self):
        self.selected_file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", 
            "All Files (*);;Images (*.png *.jpg *.jpeg);;Documents (*.pdf *.docx *.txt)"
        )
        if self.selected_file_path:
            self.pushButtonFile.setText(os.path.basename(self.selected_file_path))

    def add_file_to_database(self):
        # Validate inputs
        file_name = self.lineEditNama.text().strip()
        file_tag = self.lineEditTag.text().strip()

        if not file_name:
            QMessageBox.warning(self, "Validation Error", "Please enter a file name.")
            return

        if not self.selected_file_path:
            QMessageBox.warning(self, "Validation Error", "Please select a file.")
            return

        try:
            # Read file data
            with open(self.selected_file_path, 'rb') as file:
                file_data = file.read()

            # Add file to database
            self.file_model.add_file(
                name=file_name, 
                tag=file_tag, 
                file_path=self.selected_file_path, 
                file_data=file_data
            )

            QMessageBox.information(self, "Success", f"File '{file_name}' added successfully!")
            
            # Reset UI
            self.lineEditNama.clear()
            self.lineEditTag.clear()
            self.pushButtonFile.setText("Upload File")
            self.selected_file_path = None

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add file: {str(e)}")

class FileFolderUI(QWidget):
    def __init__(self, file_model):
        super().__init__()
        self.file_model = file_model
        self.setupUi()
        self.load_files_from_database()

    def setupUi(self):
        # [Previous UI setup code]
        # Add method to load and display files

    def load_files_from_database(self):
        # Clear existing cards
        for card in self.cards:
            card.deleteLater()
        self.cards.clear()

        # Fetch files from database and create cards
        files = self.file_model.get_all_files()
        for file_id, name, tag, file_path in files:
            self.add_card(file_path, name, tag)

class FolderController:
    def __init__(self):
        # Initialize database model
        self.file_model = FileModel()

        # Initialize UIs
        self.folder_ui = FileFolderUI(self.file_model)
        self.add_file_ui = AddFileUI(self.file_model)

        self.setup_connections()

    def setup_connections(self):
        # Connect buttons
        self.folder_ui.add_button.clicked.connect(self.go_to_add_file)
        self.add_file_ui.pushButtonBatal.clicked.connect(self.go_back_to_folder_ui)
        self.add_file_ui.pushButtonFile.clicked.connect(self.add_file_ui.open_file_dialog)
        self.add_file_ui.pushButtonTambah.clicked.connect(self.add_file_ui.add_file_to_database)

    def go_to_add_file(self):
        self.folder_ui.hide()
        self.add_file_ui.show()

    def go_back_to_folder_ui(self):
        self.add_file_ui.hide()
        self.folder_ui.show()
        # Reload files to reflect any changes
        self.folder_ui.load_files_from_database()

def main():
    app = QApplication(sys.argv)
    
    # Create controller which sets up everything
    controller = FolderController()
    
    # Show the main folder UI
    controller.folder_ui.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()