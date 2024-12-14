from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QGridLayout, QScrollArea, QDesktopWidget
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from src.controllers.calendar_controller import CalendarController

class CalendarUi(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.controller = CalendarController(db_path)
        self.current_date = QDate.currentDate()
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 0, 10, 0)

        # Navigation bar
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("\u25C0")
        self.prev_button.setObjectName("calendarNavButtonPrev")
        self.prev_button.clicked.connect(self.previous_month)
        self.month_label = QLabel(self.current_date.toString("MMMM yyyy"))
        self.month_label.setAlignment(Qt.AlignCenter)
        self.month_label.setFont(QFont('Arial', 12, QFont.Bold))
        self.next_button = QPushButton("\u25B6")
        self.next_button.setObjectName("calendarNavButtonNext")
        self.next_button.clicked.connect(self.next_month)

        nav_container = QWidget()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.month_label, stretch=1)
        nav_layout.addWidget(self.next_button)
        nav_container.setLayout(nav_layout)
        nav_container.setFixedWidth(300)

        # Calendar grid
        self.calendar_grid = QGridLayout()
        self.calendar_grid.setSpacing(5)

        # Add widgets to main layout
        main_layout.addWidget(nav_container, alignment=Qt.AlignRight)
        main_layout.addLayout(self.calendar_grid)

        self.setLayout(main_layout)
        self.populate_calendar()

    def center_window(self):
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def populate_calendar(self):
        # Clear existing widgets
        for i in reversed(range(self.calendar_grid.count())):
            widget = self.calendar_grid.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Day headers
        day_headers = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, header in enumerate(day_headers):
            header_label = QLabel(header)
            header_label.setAlignment(Qt.AlignCenter)
            header_label.setProperty("dayHeader", True)
            self.calendar_grid.addWidget(header_label, 0, col)

        # Calculate days
        first_day = QDate(self.current_date.year(), self.current_date.month(), 1)
        start_col = first_day.dayOfWeek() % 7
        num_days = first_day.daysInMonth()

        # Populate day cells
        row, col = 1, start_col
        for day in range(1, num_days + 1):
            day_widget = self.create_day_cell(day)
            self.calendar_grid.addWidget(day_widget, row, col)
            col += 1
            if col > 6:
                col = 0
                row += 1

    def create_day_cell(self, day):
        day_widget = QWidget()
        day_widget.setObjectName("dayCell")
        day_layout = QVBoxLayout(day_widget)
        day_layout.setContentsMargins(10, 10, 10, 10)

        # Day label
        day_label = QLabel(str(day))
        day_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        day_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        day_layout.addWidget(day_label)

        # Scrollable task area
        task_scroll = QScrollArea()
        task_scroll.setWidgetResizable(True)
        task_list_widget = QWidget()
        task_list_layout = QVBoxLayout(task_list_widget)
        task_list_layout.setContentsMargins(5, 5, 5, 5)

        # Add tasks to task list
        date = QDate(self.current_date.year(), self.current_date.month(), day).toString("yyyy-MM-dd")
        tasks = self.controller.get_tasks_for_date(date)
        for task in tasks:
            task_label = QLabel(task)
            task_label.setObjectName("taskLabel")
            task_list_layout.addWidget(task_label)

        task_scroll.setWidget(task_list_widget)
        day_layout.addWidget(task_scroll)
        day_layout.setObjectName("dayTaskScrollArea")

        return day_widget

    def previous_month(self):
        self.current_date = self.current_date.addMonths(-1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()

    def next_month(self):
        self.current_date = self.current_date.addMonths(1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()
