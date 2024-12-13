from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from src.ui.folder_ui import FileFolderUI, Card
from src.ui.add_file_ui import AddFileUI


class FolderController:
    def __init__(self, folder_ui, add_file_ui):
        self.folder_ui = folder_ui
        self.add_file_ui = add_file_ui

        self.setup_connections()

    def setup_connections(self):
        # Connect FolderUI buttons
        self.folder_ui.add_button.clicked.connect(self.go_to_add_file)
        self.add_file_ui.pushButtonBatal.clicked.connect(self.go_back_to_folder_ui)
        
        for card in self.folder_ui.cards:  # Assuming 'cards' is a list of Card instances
            card.open_file_button.clicked.connect(self.add_file)
        
    def go_to_add_file(self):
        # Show AddFileUI and hide FolderUI
        # self.folder_ui.hide()
        self.add_file_ui.show()

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
