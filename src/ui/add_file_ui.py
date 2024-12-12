from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QLineEdit
from src.ui.folder_ui import FileFolderUI

class AddFileUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWidget")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setStyleSheet("QWidget {\n"
                           "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                           "                               stop:0 #F5F7FA, stop:1 #E8EAF6);\n"
                           "}")

        self.Title = QLabel(self)
        self.Title.setGeometry(QtCore.QRect(270, 50, 261, 71))
        self.Title.setStyleSheet("QLabel {\n"
                                 "    font-size: 30px;\n"
                                 "    font-weight: bold;\n"
                                 "    color: #7E57C2;\n"
                                 "    padding: 12px 20px;\n"
                                 "    border: none;\n"
                                 "    background: transparent;\n"
                                 "    font-family: \'Segoe UI\', Arial;\n"
                                 "    letter-spacing: 1px;\n"
                                 "}")
        self.Title.setObjectName("Title")

        self.widget = QWidget(self)
        self.widget.setGeometry(QtCore.QRect(80, 140, 651, 276))
        self.widget.setObjectName("widget")
        self.verticalLayoutMain = QVBoxLayout(self.widget)
        self.verticalLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")

        self.labelNamaFile = QLabel(self.widget)
        self.labelNamaFile.setStyleSheet("QLabel {\n"
                                         "    font-weight: bold;\n"
                                         "    font-size: 20px;\n"
                                         "    padding: 0px 5px;\n"
                                         "    font-family: \'Segoe UI\', Arial;\n"
                                         "    color: #7E57C2;\n"
                                         "}")
        self.labelNamaFile.setObjectName("labelNamaFile")
        self.verticalLayoutMain.addWidget(self.labelNamaFile)

        self.lineEditNama = QLineEdit(self.widget)
        self.lineEditNama.setStyleSheet("QLineEdit {\n"
                                        "    padding: 10px 20px;\n"
                                        "    border: 2px solid #E8EAF6;\n"
                                        "    border-radius: 8px;\n"
                                        "    margin: 10px;\n"
                                        "    font-size: 14px;\n"
                                        "    background-color: white;\n"
                                        "    min-width: 300px;\n"
                                        "    color: #2C3E50;\n"
                                        "}")
        self.lineEditNama.setText("")
        self.lineEditNama.setObjectName("lineEditNama")
        self.verticalLayoutMain.addWidget(self.lineEditNama)

        self.labelTagTugas = QLabel(self.widget)
        self.labelTagTugas.setStyleSheet("QLabel {\n"
                                         "    font-weight: bold;\n"
                                         "    font-size: 20px;\n"
                                         "    padding: 0px 5px;\n"
                                         "    font-family: \'Segoe UI\', Arial;\n"
                                         "    color: #7E57C2;\n"
                                         "}")
        self.labelTagTugas.setObjectName("labelTagTugas")
        self.verticalLayoutMain.addWidget(self.labelTagTugas)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEditTag = QLineEdit(self.widget)
        self.lineEditTag.setStyleSheet("QLineEdit {\n"
                                       "    padding: 10px 20px;\n"
                                       "    border: 2px solid #E8EAF6;\n"
                                       "    border-radius: 8px;\n"
                                       "    margin: 10px;\n"
                                       "    font-size: 14px;\n"
                                       "    background-color: white;\n"
                                       "    min-width: 300px;\n"
                                       "    color: #2C3E50;\n"
                                       "}")
        self.lineEditTag.setObjectName("lineEditTag")
        self.horizontalLayout.addWidget(self.lineEditTag)

        self.pushButtonTag = QPushButton(self.widget)
        self.pushButtonTag.setStyleSheet("QPushButton {\n"
                                         "    background-color: #7E57C2;\n"
                                         "    color: white;\n"
                                         "    border: none;\n"
                                         "    border-radius: 10px;\n"
                                         "    padding: 12px 24px;\n"
                                         "    margin: 0 4px;\n"
                                         "    font-size: 14px;\n"
                                         "    font-weight: 500;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: rgb(206, 174, 255);\n"
                                         "}")
        self.pushButtonTag.setObjectName("pushButtonTag")
        self.horizontalLayout.addWidget(self.pushButtonTag)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayoutMain.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButtonFile = QPushButton(self.widget)
        self.pushButtonFile.setStyleSheet("QPushButton {\n"
                                          "    background-color: #7E57C2;\n"
                                          "    color: white;\n"
                                          "    border: none;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 12px 24px;\n"
                                          "    margin: 0 4px;\n"
                                          "    font-size: 14px;\n"
                                          "    font-weight: 500;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "    background-color: rgb(206, 174, 255);\n"
                                          "}")
        self.pushButtonFile.setObjectName("pushButtonFile")
        self.horizontalLayout_2.addWidget(self.pushButtonFile)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayoutMain.addLayout(self.horizontalLayout_2)

        self.widget1 = QWidget(self)
        self.widget1.setGeometry(QtCore.QRect(280, 480, 258, 43))
        self.widget1.setObjectName("widget1")

        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButtonBatal = QPushButton(self.widget1)
        self.pushButtonBatal.setStyleSheet("QPushButton {\n"
                                           "    background-color: #EF5350;\n"
                                           "    color: white;\n"
                                           "    border: none;\n"
                                           "    border-radius: 10px;\n"
                                           "    padding: 12px 24px;\n"
                                           "    margin: 0 4px;\n"
                                           "    font-size: 14px;\n"
                                           "    font-weight: 500;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: rgb(206, 174, 255);\n"
                                           "}")
        self.pushButtonBatal.setObjectName("pushButtonBatal")
        self.horizontalLayout_3.addWidget(self.pushButtonBatal)

        self.pushButtonTambah = QPushButton(self.widget1)
        self.pushButtonTambah.setStyleSheet("QPushButton {\n"
                                            "    background-color: #66BB6A;\n"
                                            "    color: white;\n"
                                            "    border: none;\n"
                                            "    border-radius: 10px;\n"
                                            "    padding: 12px 24px;\n"
                                            "    margin: 0 4px;\n"
                                            "    font-size: 14px;\n"
                                            "    font-weight: 500;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: rgb(206, 174, 255);\n"
                                            "}")
        self.pushButtonTambah.setObjectName("pushButtonTambah")
        self.horizontalLayout_3.addWidget(self.pushButtonTambah)

        self.retranslateUi()
    
    def backToPreviousWindow(self):
        # Close the current window and show the previous window (FolderUI)
        self.close()
        self.previous_window = FileFolderUI()  # Assuming you have a FolderUI class
        self.previous_window.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWidget", "File Tuntasin"))
        self.Title.setText(_translate("MainWidget", "File Tuntasin"))
        self.labelNamaFile.setText(_translate("MainWidget", "Nama File"))
        self.labelTagTugas.setText(_translate("MainWidget", "Tag Tugas"))
        self.pushButtonTag.setText(_translate("MainWidget", "Tambah Tag"))
        self.pushButtonFile.setText(_translate("MainWidget", "Upload File"))
        self.pushButtonBatal.setText(_translate("MainWidget", "Batal"))
        self.pushButtonTambah.setText(_translate("MainWidget", "Tambah Tugas"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = AddFileUI()
    widget.show()
    sys.exit(app.exec_())
