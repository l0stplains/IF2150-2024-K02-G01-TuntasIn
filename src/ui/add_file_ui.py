from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow
from src.models.folder import FileModel  # Import model FileModel
import os
from PyQt5.QtCore import QCoreApplication
from src.components.navbar import NavBar

Folder_Main = None
class AddFileController:
    def __init__(self, ui):
        """
        Initialize the controller with a reference to the UI instance.
        """
        self.ui = ui
        self.model = FileModel()  # Inisialisasi model database
        self.setup_connections()

    def setup_connections(self):
        """
        Connect UI buttons to their respective slot methods.
        """
        # self.ui.pushButtonTag.clicked.connect(self.add_tag)
        self.ui.pushButtonFile.clicked.connect(self.upload_file)
        self.ui.pushButtonTambah.clicked.connect(self.query_id)

    def upload_file(self):
        """
        Handle the 'Upload File' button click.
        """
        file_name, _ = QFileDialog.getOpenFileName(
            self.ui, 
            "Select File", 
            "", 
            "Images (*.png *.jpg *.jpeg *.bmp);;Documents (*.docx *.pdf *.txt);;All Files (*.*)"
        )
        if file_name:
            QMessageBox.information(self.ui, "File Selected", f"File '{file_name}' selected!", QMessageBox.Ok)
            self.ui.selected_file = file_name  # Store selected file path
            
    def query_id(self):
        file_name = self.ui.lineEditNama.text()
        if not file_name.strip():
                task_id = -1
        else:
            # Check if the task exists in the Task table
            query_task = "SELECT taskId FROM Task WHERE title = ?"
            cursor = self.model.conn.execute(query_task, (file_name,))
            task = cursor.fetchone()

            if not task:
                QMessageBox.warning(self.ui, "Warning", f"No task with title '{file_name}' exists!")
                return

            # Get the taskId
            task_id = task[0]
            
        self.add_task_file(task_id)

    def add_task_file(self, task_id):
        """
        Handle the 'Tambah Tugas' button click.
        """
        # Get file path from UI (assuming a file was uploaded
        
        try:
            file_path = getattr(self.ui, "selected_file", None)
            if not file_path:
                QMessageBox.warning(self.ui, "Warning", "No file selected!", QMessageBox.Ok)
                return
            # Save the file to the Attachment table
            with open(file_path, 'rb') as file:
                file_data = file.read()

            # Calculate file size
            file_size = len(file_data)

            # Insert the file into the Attachment table
            query_attachment = """
            INSERT INTO Attachment (taskId, fileName, filePath, fileSize, fileData) 
            VALUES (?, ?, ?, ?, ?)
            """
            self.model.conn.execute(query_attachment, (task_id, os.path.basename(file_path), file_path, file_size, file_data))
            self.model.conn.commit()
        
        except Exception as e:
            QMessageBox.warning(self.ui, "Error", f"Failed to add task: {str(e)}", QMessageBox.Ok)

        # Clear inputs
        QMessageBox.information(self.ui, "Success", "File added successfully!", QMessageBox.Ok)
        self.ui.lineEditNama.clear()