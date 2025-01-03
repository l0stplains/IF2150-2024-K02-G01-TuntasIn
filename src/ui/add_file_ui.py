from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QSpacerItem, QSizePolicy
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.ui.folder_ui import FileFolderUI
from PyQt5.QtCore import QTranslator, QLibraryInfo
from PyQt5.QtWidgets import QApplication

class AddFileUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWidget")
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setStyleSheet("QWidget {\n"
                           "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                           "                               stop:0 #F5F7FA, stop:1 #E8EAF6);\n"
                           "}")
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(100, 50, 100, 200)  # Adjust the bottom margin


        # Title Section
        self.Title = QLabel("File Tuntasin", self)
        self.Title.setStyleSheet("QLabel {\n"
                                 "    font-size: 30px;\n"
                                 "    font-weight: bold;\n"
                                 "    color: #7E57C2;\n"
                                 "    text-align: center;\n"
                                 "    font-family: 'Segoe UI', Arial;\n"
                                 "    letter-spacing: 1px;\n"
                                 "}")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.Title)

        # Form Section
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(15,15,15,15)  # Set spacing between form elements

        # File Name Input
        self.labelNamaFile = QLabel("Nama Task", self)
        self.labelNamaFile.setStyleSheet("QLabel {\n"
                                         "    font-weight: bold;\n"
                                         "    font-size: 20px;\n"
                                         "    font-family: 'Segoe UI', Arial;\n"
                                         "    color: #7E57C2;\n"
                                         "}")
        form_layout.addWidget(self.labelNamaFile)

        self.lineEditNama = QLineEdit(self)
        self.lineEditNama.setMinimumHeight(70)
        self.lineEditNama.setPlaceholderText("Masukkan nama Task yang berkaitan dengan file, jika tidak ada kosongkan")
        self.lineEditNama.setStyleSheet("QLineEdit {\n"
                                        "    padding: 10px 20px;\n"
                                        "    border: 2px solid #E8EAF6;\n"
                                        "    border-radius: 8px;\n"
                                        "    font-size: 14px;\n"
                                        "    background-color: white;\n"
                                        "    color: #2C3E50;\n"
                                        "}")
        form_layout.addWidget(self.lineEditNama)

        # File Upload Button
        upload_button_layout = QHBoxLayout()
        self.pushButtonFile = QPushButton("Upload File", self)
        self.pushButtonFile.setStyleSheet("QPushButton {\n"
                                          "    background-color: #7E57C2;\n"
                                          "    color: white;\n"
                                          "    border: none;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 12px 24px;\n"
                                          "    font-size: 14px;\n"
                                          "    font-weight: 500;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(206, 174, 255);\n"
                                          "}")
        upload_button_layout.addWidget(self.pushButtonFile, alignment=QtCore.Qt.AlignLeft)
        form_layout.addLayout(upload_button_layout)

        main_layout.addLayout(form_layout)

        # Bottom Buttons
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.pushButtonBatal = QPushButton("Kembali", self)
        self.pushButtonBatal.setStyleSheet("QPushButton {\n"
                                           "    background-color: #EF5350;\n"
                                           "    color: white;\n"
                                           "    border: none;\n"
                                           "    border-radius: 10px;\n"
                                           "    padding: 12px 24px;\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 500;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(255, 102, 102);\n"
                                           "}")
        button_layout.addWidget(self.pushButtonBatal)

        self.pushButtonTambah = QPushButton("Tambah Tugas", self)
        self.pushButtonTambah.setStyleSheet("QPushButton {\n"
                                            "    background-color: #66BB6A;\n"
                                            "    color: white;\n"
                                            "    border: none;\n"
                                            "    border-radius: 10px;\n"
                                            "    padding: 12px 24px;\n"
                                            "    font-size: 14px;\n"
                                            "    font-weight: 500;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(102, 204, 102);\n"
                                            "}")
        button_layout.addWidget(self.pushButtonTambah)

        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(button_layout)
        
        form_layout.addStretch(1)

    def backToPreviousWindow(self):
        # Close the current window and show the previous window (FolderUI)
        self.close()
        self.previous_window = FileFolderUI()  # Assuming you have a FolderUI class
        self.previous_window.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = AddFileUI()
    widget.show()
    sys.exit(app.exec_())