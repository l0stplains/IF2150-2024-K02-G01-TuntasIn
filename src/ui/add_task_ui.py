

from PyQt5 import QtCore, QtGui, QtWidgets


class AddTaskUI(object):
    def __init__(self,AddTask):
        super().__init__()
        self.setupUi(AddTask)
    def setupUi(self, AddTask):
        AddTask.setObjectName("AddTask")
        AddTask.resize(1280, 1000)
        AddTask.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        AddTask.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        AddTask.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(AddTask)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(AddTask)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1278, 998))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 1000))
        self.widget.setMinimumSize(QtCore.QSize(1280, 971))
        self.widget.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.widget.setAcceptDrops(True)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: rgb(255, 255,255);\n"
"font-family: \'Segoe UI\', Arial;\n"
"\n"
"}\n"
"\n"
"QLineEdit, QTextEdit{\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 20px;\n"
"font-weight: bold ;\n"
"font-family: \'Segoe UI\', Arial;\n"
"color: #7E57C2 ;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 91, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(440, 10, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("   font-size: 40px;\n"
"   font-weight: bold;\n"
"   color: #7E57C2;\n"
"   padding: 12px 20px;\n"
"   border: none;\n"
"")
        self.label.setObjectName("label")
        self.description = QtWidgets.QTextEdit(self.widget)
        self.description.setGeometry(QtCore.QRect(100, 300, 871, 111))
        self.description.setStyleSheet("")
        self.description.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.description.setObjectName("description")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 260, 111, 41))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(100, 620, 91, 41))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 800, 201, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #7E57C2 ;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(163, 114, 255);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(100, 750, 91, 41))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setGeometry(QtCore.QRect(350, 880, 201, 41))
        self.cancel.setStyleSheet("QPushButton{\n"
"background-color: #EF5350;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(179, 62, 60);\n"
"}\n"
"")
        self.cancel.setObjectName("cancel")
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setGeometry(QtCore.QRect(590, 880, 201, 41))
        self.add.setStyleSheet("QPushButton{\n"
"background-color: #66BB6A;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(79, 145, 81);\n"
"\n"
"}")
        self.add.setObjectName("add")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 800, 51, 41))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #7E57C2 ;\n"
"border-radius: 20px;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(163, 114, 255);\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setGeometry(QtCore.QRect(100, 190, 871, 41))
        self.name.setObjectName("name")
        self.tag1 = QtWidgets.QLineEdit(self.widget)
        self.tag1.setGeometry(QtCore.QRect(100, 670, 141, 31))
        self.tag1.setPlaceholderText("")
        self.tag1.setObjectName("tag1")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(100, 520, 91, 41))
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(100, 420, 171, 41))
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.nameWarning = QtWidgets.QLabel(self.widget)
        self.nameWarning.setGeometry(QtCore.QRect(100, 240, 231, 16))
        self.nameWarning.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";color: rgb(255, 0, 0);")
        self.nameWarning.setText("")
        self.nameWarning.setObjectName("nameWarning")
        self.date = QtWidgets.QDateEdit(self.widget)
        self.date.setGeometry(QtCore.QRect(100, 470, 151, 31))
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.category = QtWidgets.QComboBox(self.widget)
        self.category.setGeometry(QtCore.QRect(100, 570, 151, 31))
        self.category.setStyleSheet("")
        self.category.setObjectName("category")
        self.category.addItem("")
        self.category.addItem("")
        self.tag2 = QtWidgets.QLineEdit(self.widget)
        self.tag2.setGeometry(QtCore.QRect(280, 670, 141, 31))
        self.tag2.setObjectName("tag2")
        self.tag3 = QtWidgets.QLineEdit(self.widget)
        self.tag3.setGeometry(QtCore.QRect(460, 670, 141, 31))
        self.tag3.setObjectName("tag3")
        self.tag4 = QtWidgets.QLineEdit(self.widget)
        self.tag4.setGeometry(QtCore.QRect(640, 670, 141, 31))
        self.tag4.setObjectName("tag4")
        self.tag5 = QtWidgets.QLineEdit(self.widget)
        self.tag5.setGeometry(QtCore.QRect(820, 670, 141, 31))
        self.tag5.setObjectName("tag5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(AddTask)
        QtCore.QMetaObject.connectSlotsByName(AddTask)

    def retranslateUi(self, AddTask):
        _translate = QtCore.QCoreApplication.translate
        AddTask.setWindowTitle(_translate("AddTask", "Dialog"))
        self.label_2.setText(_translate("AddTask", "Nama"))
        self.label.setText(_translate("AddTask", "Form TuntasIn"))
        self.description.setHtml(_translate("AddTask", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.description.setPlaceholderText(_translate("AddTask", "Deskripsikan tugas anda..."))
        self.label_3.setText(_translate("AddTask", "Deskripsi"))
        self.label_6.setText(_translate("AddTask", "Tag"))
        self.pushButton.setText(_translate("AddTask", "Lampirkan"))
        self.label_7.setText(_translate("AddTask", "File"))
        self.cancel.setText(_translate("AddTask", "Batal"))
        self.add.setText(_translate("AddTask", "Tambah"))
        self.pushButton_4.setText(_translate("AddTask", "+"))
        self.name.setPlaceholderText(_translate("AddTask", "Masukkan nama tugas..."))
        self.label_8.setText(_translate("AddTask", "Kategori"))
        self.label_9.setText(_translate("AddTask", "Tanggal Tenggat"))
        self.category.setItemText(0, _translate("AddTask", "Tugas"))
        self.category.setItemText(1, _translate("AddTask", "Meet"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTask = QtWidgets.QDialog()
    ui = AddTaskUI()
    ui.setupUi(AddTask)
    AddTask.show()
    sys.exit(app.exec_())
