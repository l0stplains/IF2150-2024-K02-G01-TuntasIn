from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class NotificationWindow(QDialog):
    def __init__(self, parent_window):
        super().__init__()
        self.setObjectName("NotificationWindow")
        self.setWindowTitle("Notifikasi")

        self.setWindowModality(Qt.ApplicationModal)

        # Set window flags to prevent dragging
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint) 
        
        self.parent_window = parent_window 
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Title
        self.title_label = QLabel("Notifikasi")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Notification list
        self.notification_list = QListWidget()
        self.notification_list.setObjectName("notificationList")
        layout.addWidget(self.notification_list)

        # Close button
        self.close_button = QPushButton("Tutup")
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close_and_notify)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def update_notifications(self, notifications):
        self.notification_list.clear()
        font = QFont("Segoe UI", 12) 

        for notification in notifications:
            item = QListWidgetItem(notification)
            item.setFont(font)  
            item.setTextAlignment(Qt.AlignCenter)  
            self.notification_list.addItem(item)

    def close_and_notify(self):
        self.close()
        self.parent_window.handle_close() 
