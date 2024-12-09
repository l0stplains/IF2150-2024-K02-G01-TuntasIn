import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton

class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.setup_ui()
        self.load_filter_options()
        
    def setup_ui(self):
        self.setWindowTitle("Filter Tasks")
        layout = QVBoxLayout(self)
        
        # Category filter
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel("Category:"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("All Categories", None)
        cat_layout.addWidget(self.category_combo)
        layout.addLayout(cat_layout)
        
        # Tag filter
        tag_layout = QHBoxLayout()
        tag_layout.addWidget(QLabel("Tag:"))
        self.tag_combo = QComboBox()
        self.tag_combo.addItem("All Tags", None)
        tag_layout.addWidget(self.tag_combo)
        layout.addLayout(tag_layout)

        # Status filter
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Status:"))
        self.status_combo = QComboBox()
        self.status_combo.addItem("All Status", None)
        self.status_combo.addItem("Selesai", "Selesai")
        self.status_combo.addItem("Belum Selesai", "Belum Selesai")
        status_layout.addWidget(self.status_combo)
        layout.addLayout(status_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self.accept)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_filters)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        btn_layout.addWidget(apply_btn)
        btn_layout.addWidget(clear_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)
    
    def load_filter_options(self):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        
        # Load categories
        cursor.execute("SELECT DISTINCT category FROM tasks")
        categories = cursor.fetchall()
        for category in categories:
            self.category_combo.addItem(category[0], category[0])
            
        # Load tags
        cursor.execute("SELECT DISTINCT name FROM tags")
        tags = cursor.fetchall()
        for tag in tags:
            self.tag_combo.addItem(tag[0], tag[0])
            
        conn.close()
    
    def get_filters(self):
        return {
            'category': self.category_combo.currentData(),
            'tag': self.tag_combo.currentData(),
            'status': self.status_combo.currentData()
        }
    
    def clear_filters(self):
        self.category_combo.setCurrentIndex(0)
        self.tag_combo.setCurrentIndex(0)
        self.status_combo.setCurrentIndex(0)

class HomeController:
    def __init__(self, view):
        self.view = view
        self.db_path = 'tasks.db'
        self.current_filters = {'category': None, 'tag': None, 'status': None}
        
        # Connect signals
        self.view.search_input.textChanged.connect(self.filter_tasks)
        self.view.add_btn.clicked.connect(self.add_task)
        self.view.filter_btn.clicked.connect(self.show_filter_dialog)
        
        self.load_tasks()
        
    def load_tasks(self, search_text=""):
        self.view.clear_tasks()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = """
        SELECT t.id, t.name, t.category, t.status, t.due_date, GROUP_CONCAT(tag.name)
        FROM tasks t
        LEFT JOIN tags tag ON t.id = tag.task_id
        WHERE t.name LIKE ?
        """
        params = [f'%{search_text}%']
        
        # Add category filter
        if self.current_filters['category']:
            query += " AND t.category = ?"
            params.append(self.current_filters['category'])
            
        # Add tag filter
        if self.current_filters['tag']:
            query += """ AND EXISTS (
                SELECT 1 FROM tags 
                WHERE tags.task_id = t.id 
                AND tags.name = ?
            )"""
            params.append(self.current_filters['tag'])

        # Add status filter
        if self.current_filters['status']:
            query += " AND t.status = ?"
            params.append(self.current_filters['status'])
            
        query += """
        GROUP BY t.id
        ORDER BY t.due_date DESC
        """
        
        cursor.execute(query, tuple(params))
        tasks = cursor.fetchall()
        
        for task in tasks:
            task_id, name, category, status, due_date, tags = task
            tags = tags.split(',') if tags else []
            
            due_date = datetime.strptime(due_date, '%Y-%m-%d').strftime('%d %B %Y')
            
            task_widget = self.view.add_task(task_id, name, category, tags, status, due_date)
            task_widget.clicked.connect(self.show_task_details)
            task_widget.edit_clicked.connect(self.edit_task)
            task_widget.delete_clicked.connect(self.delete_task)
            
        conn.close()
        
    def filter_tasks(self):
        search_text = self.view.search_input.text()
        self.load_tasks(search_text)
        
    def show_filter_dialog(self):
        dialog = FilterDialog(self.view)
        if dialog.exec_() == QDialog.Accepted:
            self.current_filters = dialog.get_filters()
            self.filter_tasks()
        
    def add_task(self):
        # Implement navigation to add task form
        pass
        
    def edit_task(self, task_id):
        # Implement navigation to edit task form
        pass
        
    def show_task_details(self, task_id):
        # Implement navigation to task details
        pass
        
    def delete_task(self, task_id):
        reply = QMessageBox.question(
            self.view,
            'Confirm Deletion',
            'Are you sure you want to delete this task?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Delete tags first due to foreign key constraint
            cursor.execute("DELETE FROM tags WHERE task_id = ?", (task_id,))
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            
            conn.commit()
            conn.close()
            
            self.load_tasks()