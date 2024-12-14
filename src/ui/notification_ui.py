import sqlite3
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from datetime import datetime, timedelta

class NotificationWindow(QDialog):
    def __init__(self, parent_window, db_path="database.db"):
        super().__init__()
        self.setObjectName("NotificationWindow")
        self.setWindowTitle("Notifikasi")

        self.setWindowModality(Qt.ApplicationModal)

        # Set window flags to prevent dragging
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        self.parent_window = parent_window
        self.db_path = db_path  # Path to your database
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

        # Fetch notifications (tasks) from the database
        self.update_notifications()

    def fetch_tasks_from_db(self):
        """Fetch task titles, due dates, from the database."""
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Query to get task title, due date, and time
            cursor.execute("SELECT title, dueDate FROM Task WHERE isComplete = 0")  # Only incomplete tasks
            tasks = cursor.fetchall()
            connection.close()
            return tasks

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def update_notifications(self):
        """Update notification list with task titles and deadlines."""
        self.notification_list.clear()
        font = QFont("Segoe UI", 12)

        # Fetch tasks from the database
        tasks = self.fetch_tasks_from_db()

        # Get the current time
        current_time = datetime.now()

        # Loop through tasks and check if dueDate and time is within 1 hour of current time
        matching_tasks = []
        for task in tasks:
            title, due_date_str = task
            
            try:
                # Combine dueDate and time into a single datetime object
                combined_datetime_str = f"{due_date_str}"
                due_datetime = datetime.strptime(combined_datetime_str, '%d-%m-%Y %H:%M:%S')  # Format 'YYYY-MM-DD HH:MM:SS'

                # Calculate the time difference between now and the due datetime
                time_difference = abs(current_time - due_datetime)

                # Check if the time difference is less than or equal to 1 hour
                if time_difference <= timedelta(hours=1):
                    notification = f"Tugas: {title} | Deadline: {due_datetime.strftime('%Y-%m-%d %H:%M:%S')}"
                    matching_tasks.append(notification)
            except ValueError:
                print(f"Invalid date or time format for task: {title}")
        
        # Display matching tasks or a message if none
        if not matching_tasks:
            self.notification_list.addItem("Tidak ada tugas yang tenggatnya berbeda 1 jam dari sekarang.")
        else:
            for notification in matching_tasks:
                item = QListWidgetItem(notification)
                item.setFont(font)
                item.setTextAlignment(Qt.AlignCenter)
                self.notification_list.addItem(item)

    def close_and_notify(self):
        """Close the notification window and notify the parent."""
        self.close()
        # self.parent_window.handle_close()  # Uncomment if you need to handle close in parent window