from PyQt5.QtWidgets import QMessageBox , QPushButton
from PyQt5.QtWidgets import QFileDialog
from src.ui.folder_ui import FileFolderUI, Card
from src.ui.add_file_ui import AddFileUI
from src.models.folder import FileModel
import os
from functools import partial
import subprocess
from add_file_main import Add_File_Main
from PyQt5.QtCore import QCoreApplication

class FolderController:
    def __init__(self, folder_ui, add_file_ui):
        self.file_model = FileModel()
        self.folder_ui = folder_ui
        self.add_file_ui = add_file_ui

        self.setup_connections()
        self.load_files_from_database()

    def setup_connections(self):
        # Connect FolderUI buttons
        self.folder_ui.add_button.clicked.connect(self.go_to_add_file)
        self.add_file_ui.pushButtonBatal.clicked.connect(self.go_back_to_folder_ui)
        
        # # Add connections to open file buttons dynamically
        for card in self.folder_ui.cards:
            open_file_button = card.findChild(QPushButton, 'open_file_button')
            open_file_button.clicked.connect(lambda _, card=card: self.open_file_from_card(card))
        
    def go_to_add_file(self):
        # Show AddFileUI and hide FolderUI
        self.folder_ui.hide()
        QCoreApplication.processEvents() 
        add_file_ui_instance = Add_File_Main()  # Create an instance
        add_file_ui_instance.show()
        
        self.add_file_ui_instance = add_file_ui_instance
        

    def go_back_to_folder_ui(self):
        # Show FolderUI and hide AddFileUI
        # self.add_file_ui.hide()
        self.folder_ui.show()

    def add_file(self):
        # Logic to select a file
        file_path, _ = QFileDialog.getOpenFileName(
            self.add_file_ui, "Select File", "", 
            "Images (*.png *.jpg *.jpeg);;Documents (*.pdf *.docx *.txt);"
        )
        if file_path:
            # Add the file to the FolderUI
            self.folder_ui.add_card(file_path)
            QMessageBox.information(self.add_file_ui, "File Added", f"File '{file_path}' has been added!")
    
    def load_files_from_database(self):
        # Clear existing cards
        for card in self.folder_ui.cards:
            card.deleteLater()
        self.folder_ui.cards.clear()

        # Fetch files from database
        files = self.file_model.get_all_files()
        
        for attachment_id, name, path, size, task in files:
            self.folder_ui.add_card(path, name, task)

    def open_file_from_card(self, card):
        """
        Open the file associated with the given card.
        """
        file_path = getattr(card, 'file_path', None)  # Safely get file_path attribute
        if not file_path:
            QMessageBox.warning(self.folder_ui, "Error", "File path not found!")
            return

        if os.path.exists(file_path):
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(file_path)
                elif os.name == 'posix':  # macOS/Linux
                    subprocess.run(["xdg-open", file_path], check=True)
                else:
                    QMessageBox.warning(self.folder_ui, "Error", "Unsupported operating system.")
            except Exception as e:
                QMessageBox.warning(self.folder_ui, "Error", f"Failed to open file: {str(e)}")
        else:
            QMessageBox.warning(self.folder_ui, "Error", f"File does not exist: {file_path}")

