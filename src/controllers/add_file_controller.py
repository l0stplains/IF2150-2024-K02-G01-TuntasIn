from PyQt5.QtWidgets import QFileDialog, QMessageBox


class AddFileController:
    def __init__(self, ui):
        """
        Initialize the controller with a reference to the UI instance.
        """
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        """
        Connect UI buttons to their respective slot methods.
        """
        self.ui.pushButtonTag.clicked.connect(self.add_tag)
        self.ui.pushButtonFile.clicked.connect(self.upload_file)
        self.ui.pushButtonBatal.clicked.connect(self.cancel)
        self.ui.pushButtonTambah.clicked.connect(self.add_task)

    def add_tag(self):
        """
        Handle the 'Tambah Tag' button click.
        """
        tag = self.ui.lineEditTag.text()
        if not tag.strip():
            QMessageBox.warning(self.ui, "Warning", "Tag cannot be empty!")
            return
        QMessageBox.information(self.ui, "Success", f"Tag '{tag}' added!")
        self.ui.lineEditTag.clear()

    def upload_file(self):
        """
        Handle the 'Upload File' button click.
        """
        file_name, _ = QFileDialog.getOpenFileName(
            self.ui, 
            "Select File", 
            "", 
            "Images (*.png *.jpg *.jpeg *.bmp);;Documents (*.docx *.pdf *.txt);;All Files (*.*)  "
            )
        if file_name:
            QMessageBox.information(self.ui, "File Selected", f"File '{file_name}' selected!")

    def cancel(self):
        """
        Handle the 'Batal' button click.
        """
        QMessageBox.information(self.ui, "Cancel", "Operation cancelled.")
        self.ui.close()

    def add_task(self):
        """
        Handle the 'Tambah Tugas' button click.
        """
        file_name = self.ui.lineEditNama.text()
        if not file_name.strip():
            QMessageBox.warning(self.ui, "Warning", "File name cannot be empty!")
            return
        QMessageBox.information(self.ui, "Success", f"Task '{file_name}' added!")
        self.ui.lineEditNama.clear()
