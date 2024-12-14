import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from src.controllers.edit_view_controller import EditViewController
from src.controllers.task_view_controller import TaskViewController
from src.ui.task_view_ui import TaskViewUI
from src.ui.edit_view_ui import EditViewUI

class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.setup_ui()
        self.load_filter_options()
        
    def setup_ui(self):
        self.setWindowTitle("Filter Tasks")
        layout = QVBoxLayout(self)
        
        cat_layout = QHBoxLayout()
        cat_layout.addWidget(QLabel("Category:"))
        self.category_combo = QComboBox()
        self.category_combo.addItem("All Categories", None)
        cat_layout.addWidget(self.category_combo)
        layout.addLayout(cat_layout)
        
        tag_layout = QHBoxLayout()
        tag_layout.addWidget(QLabel("Tag:"))
        self.tag_combo = QComboBox()
        self.tag_combo.addItem("All Tags", None)
        tag_layout.addWidget(self.tag_combo)
        layout.addLayout(tag_layout)

        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Status:"))
        self.status_combo = QComboBox()
        self.status_combo.addItem("All Status", None)
        self.status_combo.addItem("Completed", "Completed")
        self.status_combo.addItem("Not Completed", "Not Completed")
        status_layout.addWidget(self.status_combo)
        layout.addLayout(status_layout)
        
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
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        cursor.execute("SELECT DISTINCT category FROM Task")
        categories = cursor.fetchall()
        for category in categories:
            self.category_combo.addItem(category[0], category[0])

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
        self.db_path = 'database.db'
        self.current_filters = {'category': None, 'tag': None, 'status': None}
        
        self.view.search_input.textChanged.connect(self.filter_tasks)
        # self.view.add_btn.clicked.connect(self.add_task)
        self.view.filter_btn.clicked.connect(self.show_filter_dialog)
        
        self.load_tasks()

    def filter_tasks(self):
        search_text = self.view.search_input.text()
        self.load_tasks(search_text)
        
    def load_tasks(self, search_text=""):
        self.view.clear_tasks()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = """
        SELECT t.taskId, t.title, t.category, t.isComplete, t.dueDate, GROUP_CONCAT(tag.name)
        FROM Task t
        LEFT JOIN tags tag ON t.taskId = tag.task_id
        WHERE t.title LIKE ?
        """
        params = [f'%{search_text}%']
        
        if self.current_filters['category']:
            query += " AND t.category = ?"
            params.append(self.current_filters['category'])
            
        if self.current_filters['tag']:
            query += """ AND EXISTS (
                SELECT 1 FROM tags 
                WHERE tags.task_id = t.taskId 
                AND tags.name = ?
            )"""
            params.append(self.current_filters['tag'])

        if self.current_filters['status']:
            query += " AND t.isComplete = ?"
            is_complete = 1 if self.current_filters['status'] == "Completed" else 0
            params.append(is_complete)
            
        query += """
        GROUP BY t.taskId
        ORDER BY t.dueDate DESC
        """
        
        cursor.execute(query, tuple(params))
        tasks = cursor.fetchall()
        
        for task in tasks:
            task_id, title, category, is_complete, due_date, tags = task
            tags = tags.split(',') if tags else []
            
            status = "Completed" if is_complete else "Not Completed"
            
            task_widget = self.view.add_task(task_id, title, category, tags, status, due_date)
            task_widget.clicked.connect(self.show_task_details)
            task_widget.edit_clicked.connect(self.edit_task)
            task_widget.delete_clicked.connect(self.delete_task)
            
        conn.close()
        
    def show_filter_dialog(self):
        dialog = FilterDialog(self.view)
        if dialog.exec_() == QDialog.Accepted:
            self.current_filters = dialog.get_filters()
            self.filter_tasks()
                
        

    def refresh_tasks(self):
        tasks = self.task_model.get_all_tasks()
        self.main_window.update_task_list(tasks)
        
    def edit_task(self, task_id):
        task_dialog = QDialog()
        
        task_view_ui = EditViewUI(task_dialog)
        
        task_controller = EditViewController(task_view_ui, task_id)
        
        task_dialog.exec_()
        
    def show_task_details(self, task_id):
        dialog = QDialog()
        task_view_ui = TaskViewUI(dialog)
        task_controller = TaskViewController(task_view_ui, task_id)
        dialog.exec_()
        
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
            
            cursor.execute("DELETE FROM tags WHERE task_id = ?", (task_id,))
            cursor.execute("DELETE FROM Task WHERE taskId = ?", (task_id,))
            
            conn.commit()
            conn.close()
            
            self.load_tasks()
