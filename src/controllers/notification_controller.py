from src.models.task import TaskModel
from PyQt5.QtCore import QTimer
from src.ui.notification_ui import NotificationWindow
from datetime import datetime
from src.utils.date_utils import calculate_time_left

class NotificationController:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.task_model = TaskModel() 
        self.notification_window = NotificationWindow(self)

        # Checking notificartions every 60 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_notifications)
        self.timer.start(60000)  # Setiap 60 detik

        # Time for repeating notification
        self.notification_repeat_timer = QTimer()
        self.notification_repeat_timer.timeout.connect(self.show_notification_again)

        # Loading notifications on startup
        self.check_notifications()

    def check_notifications(self):
        tasks = self.task_model.get_all_tasks()
        notifications = []

        for task in tasks:
            due_datetime = f"{task[2]} {task[3]}"  # task[2] = due_date, task[3] = due_time
            try:
                time_left_str = calculate_time_left(due_datetime)
                due_datetime_obj = datetime.strptime(due_datetime, "%Y-%m-%d %I:%M %p")
                time_left_minutes = int((due_datetime_obj - datetime.now()).total_seconds() / 60)
                if 0 < time_left_minutes < 1440 and time_left_str:
                    status = f"Tenggat waktu {task[1]} tersisa {time_left_str}."
                    notifications.append(status)
            except ValueError as e:
                print(f"Error parsing datetime for task {task[1]}: {e}")

        self.notification_window.update_notifications(notifications)
        if notifications:
            self.show_notification()

    def show_notification(self):
        self.notification_window.setModal(True) 
        self.notification_window.show()
        self.notification_repeat_timer.stop()

    def show_notification_again(self):
        if not self.notification_window.isVisible():
            self.notification_window.setModal(True)
            self.notification_window.show()

    def handle_close(self):
        self.notification_repeat_timer.start(1800000)
        self.parent_window.handle_close()
