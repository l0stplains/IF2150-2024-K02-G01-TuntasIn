from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QGridLayout, QScrollArea, QFrame, QMessageBox, QDialog, QFormLayout, QLineEdit
)
from PyQt5.QtCore import Qt, QDate
import sqlite3


class CustomCalendar(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self.current_date = QDate.currentDate()

        self.init_ui()

    def init_ui(self):
        """Initialize the calendar UI layout."""
        self.setWindowTitle("Custom Calendar")
        self.setGeometry(100, 100, 1000, 800)

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setAlignment(Qt.AlignTop)

        # Navigation bar
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("◀")
        self.prev_button.clicked.connect(self.previous_month)
        self.month_label = QLabel(self.current_date.toString("MMMM yyyy"))
        self.month_label.setAlignment(Qt.AlignCenter)
        self.month_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.next_button = QPushButton("▶")
        self.next_button.clicked.connect(self.next_month)

        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.month_label, stretch=1)
        nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)

        # Calendar grid
        self.calendar_grid = QGridLayout()
        self.calendar_grid.setSpacing(5)  # Reduce gaps between cells
        main_layout.addLayout(self.calendar_grid)

        self.setLayout(main_layout)
        self.populate_calendar()

        # Apply QSS for styling
        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 5px;
            }
            QLabel {
                padding: 0px;
            }
            QWidget#dayCell {
                background: white;
                border: 1px solid #ccc;
                border-radius: 8px;
                min-width: 160px;
                min-height: 120px;
                max-width: 160px;
                max-height: 120px;
            }
            QScrollArea {
                border: none;
            }
            *[daylabel=\"true\"] {
                min-height: 40px;
                max-height: 40px;
                background-color:rgb(255,0,0);
            }
            dayCell {
                margin: 0px;
            }
        """)

    def populate_calendar(self):
        """Populate the calendar with day cells and tasks."""
        for i in reversed(range(self.calendar_grid.count())):
            widget = self.calendar_grid.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Add day headers
        day_headers = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, header in enumerate(day_headers):
            header_label = QLabel(header)
            header_label.setAlignment(Qt.AlignCenter)
            header_label.setProperty("daylabel", "true")
            header_label.setStyleSheet("font-weight: bold; font-size: 16px;")
            self.calendar_grid.addWidget(header_label, 0, col)

        # Calculate the first day of the month and its weekday
        first_day = QDate(self.current_date.year(),
                          self.current_date.month(), 1)
        start_col = first_day.dayOfWeek() % 7
        num_days = first_day.daysInMonth()

        # Populate days
        row = 1
        col = start_col
        for day in range(1, num_days + 1):
            day_widget = self.create_day_cell(day)
            self.calendar_grid.addWidget(day_widget, row, col)

            col += 1
            if col > 6:  # Move to next row after Sunday
                col = 0
                row += 1

    def create_day_cell(self, day):
        """Create a cell for a specific day with tasks."""
        day_widget = QWidget()
        day_widget.setObjectName("dayCell")  # For QSS styling
        day_layout = QVBoxLayout(day_widget)
        day_layout.setContentsMargins(5, 5, 5, 5)

        # Day label
        day_label = QLabel(str(day))
        add_task_button = QPushButton("+")
        add_task_button.setFixedSize(8, 8)
        add_task_button.clicked.connect(lambda: self.add_task_dialog(date))
        day_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        day_layout.addWidget(day_label)
        day_layout.addWidget(add_task_button)
        # Add task button

        # Scrollable task list
        task_scroll_area = QScrollArea()
        task_list_widget = QWidget()
        task_list_layout = QVBoxLayout(task_list_widget)
        task_list_layout.setContentsMargins(0, 0, 0, 0)

        date = QDate(self.current_date.year(),
                     self.current_date.month(), day).toString("yyyy-MM-dd")
        tasks = self.get_tasks_for_date(date)
        for task in tasks:
            task_label = QLabel(task)
            task_label.setStyleSheet(
                "background: yellow; padding: 4px; border-radius: 4px; font-size: 12px; margin: 2px;")
            task_list_layout.addWidget(task_label)

        task_scroll_area.setWidget(task_list_widget)
        task_scroll_area.setWidgetResizable(True)
        day_layout.addWidget(task_scroll_area)

        return day_widget

    def get_tasks_for_date(self, date):
        """Retrieve tasks for a specific date from the database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT task_name FROM tasks WHERE due_date = ?", (date,))
            tasks = [row[0] for row in cursor.fetchall()]
            conn.close()
            return tasks
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return []

    def add_task_dialog(self, date):
        """Open a dialog to add a task for a specific date."""
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Add Task for {date}")

        form_layout = QFormLayout()
        task_name_input = QLineEdit()
        form_layout.addRow("Task Name:", task_name_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: self.add_task(
            task_name_input.text(), date, dialog))
        form_layout.addWidget(save_button)

        dialog.setLayout(form_layout)
        dialog.exec_()

    def add_task(self, task_name, date, dialog):
        """Save a new task to the database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (task_name, due_date) VALUES (?, ?)", (task_name, date))
            conn.commit()
            conn.close()

            QMessageBox.information(
                self, "Success", "Task added successfully!")
            dialog.accept()

            self.populate_calendar()  # Reload the calendar to display the new task
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error",
                                 f"Failed to add task: {e}")

    def previous_month(self):
        """Navigate to the previous month."""
        self.current_date = self.current_date.addMonths(-1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()

    def next_month(self):
        """Navigate to the next month."""
        self.current_date = self.current_date.addMonths(1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()
