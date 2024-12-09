from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFrame, QScrollArea)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

class TaskWidget(QFrame):
    clicked = pyqtSignal(int)
    edit_clicked = pyqtSignal(int)
    delete_clicked = pyqtSignal(int)
    
    def __init__(self, task_id, name, category, tags, status, due_date, parent=None):
        super().__init__(parent)
        self.task_id = task_id
        self.setup_ui(name, category, tags, status, due_date)
        
    def setup_ui(self, name, category, tags, status, due_date):
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setObjectName("taskWidget")
        
        layout = QVBoxLayout(self)
        
        # Top section with name and status
        top_layout = QHBoxLayout()
        name_label = QLabel(name)
        name_label.setFont(QFont("Arial", 12, QFont.Bold))
        top_layout.addWidget(name_label)
        
        status_label = QLabel(status)
        status_label.setObjectName("statusLabel")
        top_layout.addWidget(status_label, alignment=Qt.AlignRight)
        
        # Middle section with category and tags
        middle_layout = QHBoxLayout()
        category_label = QLabel(category)
        category_label.setObjectName("categoryLabel")
        middle_layout.addWidget(category_label)
        
        for tag in tags:
            tag_label = QLabel(tag)
            tag_label.setObjectName("tagLabel")
            middle_layout.addWidget(tag_label)
        middle_layout.addStretch()
        
        # Bottom section with due date and buttons
        bottom_layout = QHBoxLayout()
        due_date_label = QLabel(due_date)
        due_date_label.setObjectName("dueDateLabel")
        bottom_layout.addWidget(due_date_label)
        
        edit_btn = QPushButton("Edit")
        edit_btn.setObjectName("editButton")
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(self.task_id))
        
        delete_btn = QPushButton("Hapus")
        delete_btn.setObjectName("deleteButton")
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(self.task_id))
        
        bottom_layout.addStretch()
        bottom_layout.addWidget(edit_btn)
        bottom_layout.addWidget(delete_btn)
        
        # Add all sections to main layout
        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Only emit if not clicking buttons
            if not self.childAt(event.pos()):
                self.clicked.emit(self.task_id)
        super().mousePressEvent(event)

class HomeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.setObjectName("homeWidget")
        main_layout = QVBoxLayout(self)
        
        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search tasks...")
        self.search_input.setObjectName("searchInput")
        
        self.add_btn = QPushButton("Tambah")
        self.add_btn.setObjectName("addButton")
        self.filter_btn = QPushButton("Filter")
        self.filter_btn.setObjectName("filterButton")
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.add_btn)
        search_layout.addWidget(self.filter_btn)
        
        # Scrollable task area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setObjectName("taskScrollArea")
        
        self.task_container = QWidget()
        self.task_layout = QVBoxLayout(self.task_container)
        self.task_layout.addStretch()
        
        scroll.setWidget(self.task_container)
        
        main_layout.addLayout(search_layout)
        main_layout.addWidget(scroll)
        
    def add_task(self, task_id, name, category, tags, status, due_date):
        task_widget = TaskWidget(task_id, name, category, tags, status, due_date)
        self.task_layout.insertWidget(self.task_layout.count() - 1, task_widget)
        return task_widget
        
    def clear_tasks(self):
        while self.task_layout.count() > 1:  # Keep the stretch
            item = self.task_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()