from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QGridLayout, QScrollArea, QFrame, QMessageBox, QDialog, QFormLayout,
    QLineEdit, QDesktopWidget
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
import sqlite3

class CalendarUi(QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self.current_date = QDate.currentDate()
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 0, 10, 0)

        # Navigation bar
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("◀")
        self.prev_button.setObjectName("calendarNavButtonPrev")
        self.prev_button.clicked.connect(self.previous_month)
        self.month_label = QLabel(self.current_date.toString("MMMM yyyy"))
        self.month_label.setAlignment(Qt.AlignCenter)
        self.month_label.setFont(QFont('Arial', 12, QFont.Bold))
        self.next_button = QPushButton("▶")
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
        main_layout.addWidget(nav_container)
        main_layout.addLayout(self.calendar_grid)

        self.setLayout(main_layout)
        self.populate_calendar()

        # Apply custom styling
        self.setStyleSheet(self.get_stylesheet())

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
            self.calendar_grid.setRowStretch(0, 1)
            self.calendar_grid.setColumnStretch(col, 1)

        # Calculate days
        first_day = QDate(self.current_date.year(), self.current_date.month(), 1)
        start_col = first_day.dayOfWeek() % 7
        num_days = first_day.daysInMonth()

        # Populate day cells
        row, col = 1, start_col
        for day in range(1, num_days + 1):
            day_widget = self.create_day_cell(day)
            self.calendar_grid.addWidget(day_widget, row, col)
            self.calendar_grid.setRowStretch(row, 1)
            self.calendar_grid.setColumnStretch(col, 1)
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
        tasks = self.get_tasks_for_date(date)
        for task in tasks:
            task_label = QLabel(task)
            task_label.setObjectName("taskLabel")
            task_list_layout.addWidget(task_label)

        task_scroll.setWidget(task_list_widget)
        day_layout.addWidget(task_scroll)
        day_layout.setObjectName("dayTaskScrollArea")

        return day_widget

    def get_tasks_for_date(self, date):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            query = """
SELECT t.id, t.name, t.category, t.status, t.due_date, GROUP_CONCAT(tag.name) AS tags
FROM tasks t
LEFT JOIN tags tag ON t.id = tag.task_id
WHERE t.due_date = ?
GROUP BY t.id;
"""
            cursor.execute(query, (date,))
            # Fetch and print the results
           
            tasks = [row[1] for row in cursor.fetchall()]
            conn.close()
            return tasks
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return []

    def previous_month(self):
        self.current_date = self.current_date.addMonths(-1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()

    def next_month(self):
        self.current_date = self.current_date.addMonths(1)
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        self.populate_calendar()

    def get_stylesheet(self):
        return """
            /* Calendar */
            QScrollArea {
                border: none;
                background: transparent;
            }

            QScrollBar:vertical {
                border: none;
                background: #E8EAF6;
                width: 10px;
                margin: 0;
            }

            QScrollBar::handle:vertical {
                background: #B39DDB;
                border-radius: 5px;
                min-height: 20px;
            }

            QScrollBar::handle:vertical:hover {
                background: #9575CD;
            }

            QScrollBar:horizontal {
                border: none;
                background: #E8EAF6;
                height: 10px;
                margin: 0;
            }

            QScrollBar::handle:horizontal {
                background: #B39DDB;
                border-radius: 5px;
                min-width: 20px;
            }

            QScrollBar::handle:horizontal:hover {
                background: #9575CD;
            }

            QLabel[dayHeader="true"] {
                font-size: 12px;
                font-weight: bold;
                color: #5C6BC0;
                min-height: 20px;
                max-height: 20px;
                background: #E8EAF6;
                padding: 10px;
                border-radius: 5px;
            }
            QWidget#dayCell {
                background: white;
                max-height: 160px;
                max-width:200px;
                border: 1px solid #E8EAF6;
                border-radius: 10px;
            }
            QLabel#taskLabel {
                background: #FFFFFF;
                border: 1px solid #7E57C2;
                border-radius: 5px;
                padding: 5px;
                min-height: 15px;
                max-height: 15px;
                margin: 1px 0;
                font-size: 12px;
            }
            QPushButton#addTaskButton {
                background: #7E57C2;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                min-width: 30px;
                max-width: 30px;
                min-height: 30px;
                max-height: 30px;
            }
            QPushButton#addTaskButton:hover {
                background: #673AB7;
            }
            #dayTaskScrollArea{
                max-width: 100%;
            }
            #calendarNavButtonPrev, #calendarNavButtonNext {
                background-color: #7E57C2;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 20px;
                font-weight: bold;
                margin: 0 8px;
            }

            #calendarNavButtonPrev:hover, #calendarNavButtonNext:hover {
                background-color: #673AB7;
            }

            #calendarNavButtonPrev:pressed, #calendarNavButtonNext:pressed {
                background-color: #5E35B1;
            }

        """