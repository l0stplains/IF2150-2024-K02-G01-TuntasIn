# **TuntasIn**

**TuntasIn** is a task management app built using PyQt5 and designed to help users manage their tasks effectively. It features a modern UI inspired by productivity tools, offering task tracking, folder management, calendar integration, and progress visualization.

---

## **Features**
- 🏠 **Home**: View tasks with status, priority, and tags.
- 📂 **Folders**: Organize tasks into folders for better categorization.
- 📅 **Calendar**: Visualize tasks on a calendar interface.
- ➕ **Add Task/File**: Create new tasks or upload related files.
- 📈 **Progress Tracker**: Monitor task completion statistics.
- 🔔 **Notifications**: Stay updated with task deadlines and reminders.
- ✏️ **Edit/View Tasks**: Modify or review task details.

---

## **Getting Started**

Follow these steps to set up and run the project:

### **1. Clone the Repository**
```bash
git clone https://github.com/l0stplains/IF2150-2024-K02-G01-TuntasIn.git
cd IF2150-2024-K02-G01-TuntasIn
```

### **2. Set Up the Environment**
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

If it's your first time cloning this repository, install the required PyQt5 Tools:
```bash
pip install pyqt5-tools
```

### **4. Run the Application**
Start the application by running:
```bash
python main.py
```

---

## **Project Structure**
Here's a view of the folder structure:

```
TuntasIn/
├── main.py                    # Entry point of the application
├── requirements.txt           # Dependencies
├── README.md                  # Documentation for the project
├── assets/                    # Static files like icons, images, or styles
├── src/
│   ├── ui/                    # UI files
│   │   ├── home_ui.py         # Home screen
│   │   ├── folder_ui.py       # Folder view
│   │   ├── calendar_ui.py     # Calendar view
│   │   ├── add_task_ui.py     # Add Task screen
│   │   ├── progress_ui.py     # Progress screen
│   │   ├── add_file_ui.py     # Add File screen
│   │   ├── task_view_ui.py    # Task Detail View
│   │   ├── edit_view_ui.py    # Edit Task View
│   │   ├── notification_ui.py # Notification modal
│   └── components/            # Reusable UI components
│       ├── task_item.py       # Task item widget
│       ├── folder_item.py     # Folder item widget
│       ├── notification.py    # Notification widget
│   ├── controllers/           # Logic and interactions
│   │   ├── home_controller.py
│   │   ├── folder_controller.py
│   │   ├── calendar_controller.py
│   │   ├── add_task_controller.py
│   │   ├── progress_controller.py
│   │   ├── add_file_controller.py
│   │   ├── task_view_controller.py
│   │   ├── edit_view_controller.py
│   │   ├── notification_controller.py
│   ├── models/                # Data models
│   │   ├── task.py            # Task model
│   │   ├── folder.py          # Folder model
│   │   ├── calendar.py        # Calendar model
│   │   ├── progress.py        # Progress model
│   └── utils/                 # Utility functions
│       ├── database.py        # SQLite database handler
│       ├── date_utils.py      # Date and time utilities
│       ├── config.py          # Configurations (e.g., theme, colors)
│       ├── notifications.py   # Notification logic
└── tests/                     # Unit and integration tests
    ├── test_models.py         # Tests for models
    ├── test_controllers.py    # Tests for controllers
    ├── test_ui.py             # Tests for UI behavior

```

---

## **Prerequisites**
- Python 3.8 or higher
- PyQt5 (automatically installed via `requirements.txt`)

---

## **Development Workflow**
### **Updating UI**
To modify the UI:
1. Open `.ui` files in **Qt Designer**.
2. After editing, convert the `.ui` file to Python:
   ```bash
   pyuic5 -x filename.ui -o filename_ui.py
   ```

### **Database**
This application uses **SQLite** for task and folder management. The database schema is initialized automatically when the app is first launched.

---

## **Contributing**
Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

