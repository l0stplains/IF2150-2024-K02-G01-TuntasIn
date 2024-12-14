# **TuntasIn**
> Milestone Project - IF2150 Rekayasa Perangkat Lunak 2024

<p align="center">
    <br />
    <img width="500px" src="https://github.com/user-attachments/assets/41ebf639-6a64-4084-b6ab-1112ceff35e3">
</p>
    <h3 align="center">TuntasIn</h3>
<p align="center">
   TuntasIn is a task management app built in Python.
    <br />
    <br />
    <a href="https://github.com/l0stplains/IF2150-2024-K02-G01-TuntasIn/issues">Report Bug</a>
    ·
    <a href="https://github.com/l0stplains/IF2150-2024-K02-G01-TuntasIn/issues">Request Feature</a>
</p>

## Table of Contents
* [Project Overview](#project-overview)  
* [Features](#features)  
* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)   
   * [Clone the Repository](#1-clone-the-repository)  
   * [Set Up the Environment](#2-set-up-the-environment)  
   * [Install Dependencies](#3-install-dependencies)  
   * [Run the Application](#4-run-the-application)
* [Development Workflow](#development-workflow)
* [Database](#database)  
* [Contributors](#contributors)  

---

## **Project Overview**
<p align="justify"> <b>TuntasIn</b> is a task management app built using PyQt5 and designed to help users manage their tasks effectively. It features a modern UI inspired by productivity tools, offering task tracking, folder management, calendar integration, and progress visualization.</p>

---

## **Features**
- 🏠 **Home**: View tasks with status, priority, and tags.
  ![image](https://github.com/user-attachments/assets/b8832bcd-e763-4307-a56c-ffbaeb6993fc)

- 🔔 **Notifications**: Stay updated with task deadlines and reminders.
  ![image](https://github.com/user-attachments/assets/e4d4034a-1e2b-477d-8aaa-08ad14d749da)

- ☑️ **Add, Edit, and View Task**: Create new tasks or update task.
![image](https://github.com/user-attachments/assets/2bb03f54-25b9-43a4-a010-2a465d6a64b1)


- 🗃️ **Add and View Files (Folder)**: Upload related files or view uploaded file.
![image](https://github.com/user-attachments/assets/1c176a80-571b-4d1d-a6db-711142555dff)

- 📅 **Calendar**: Visualize tasks on a calendar interface.
  ![image](https://github.com/user-attachments/assets/da891f72-5b09-4f23-9ac1-0c642ad001f3)

- 📈 **Progress Tracker**: Monitor task completion statistics.
![image](https://github.com/user-attachments/assets/3d60889c-6679-403e-9c83-7e9cea69fb15)

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
│   ├── components/            # Reusable UI components
│   ├── controllers/           # Logic and interactions
│   ├── models/                # Data models
│   └── utils/                 # Utility functions
└── tests/                     # Unit and integration tests
├── doc/                       # In-app screenshoots
└── img/                       # Unit and integration tests

```

---

## **Prerequisites**
- Python 3.8 or higher
- PyQt5 (automatically installed via `requirements.txt`)

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

## **Development Workflow**
### **Updating UI**
To modify the UI:
1. Open `.ui` files in **Qt Designer**.
2. After editing, convert the `.ui` file to Python:
   ```bash
   pyuic5 -x filename.ui -o filename_ui.py
   ```

## **Database**
![image](https://github.com/user-attachments/assets/5883a34a-7794-4cf3-a023-3d1e711e705b)

This application uses **SQLite** for task and folder management. The database schema is initialized automatically when the app is first launched.
### Task Table

| Column      | Type    | Description                |
|-------------|---------|----------------------------|
| taskId      | integer | Primary Key, Auto Increment |
| title       | text    |                            |
| description | text    |                            |
| dueDate     | text    |                            |
| time        | text    | Format 'HH:MM:SS'          |
| category    | text    |                            |
| isComplete  | boolean | Default: false             |

### Attachment Table

| Column        | Type    | Description                   |
|---------------|---------|-------------------------------|
| attachmentId  | integer | Primary Key, Auto Increment    |
| filePath      | text    |                               |
| fileName      | text    |                               |
| fileSize      | integer |                               |
| taskId        | integer | Foreign Key referencing Task  |
| fileData      | blob    |                               |

### Tags Table

| Column   | Type    | Description                   |
|----------|---------|-------------------------------|
| id       | integer | Primary Key, Auto Increment    |
| taskId   | integer | Foreign Key referencing Task  |
| name     | text    |                               |

### Relationships

- **Task to Attachment**: One-to-Many (One Task can have multiple Attachments).
- **Task to Tags**: One-to-Many (One Task can have multiple Tags).
---





## **Contributors**
### K02-G01 Members
| **Name**                     | **Student ID** | **Developed Feature**                                                                                               |  
|-------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------|  
| [Refki Alfarizi](https://github.com/l0stplains) | 13523002       | Calendar  |  
| [Adhimas Aryo Bimo](https://github.com/ryonlunar) | 13523052      | Add and View Files (Folder)                                       |  
| [Muhammad Rusmin Nurwadin](https://github.com/Rusmn) | 13523068       | Home Page                                                    |  
| [Guntara Hambali](https://github.com/guntarahmbl) | 13523114       | Add, Edit, and View Task                                                        |  
| [Ziyan Agil Nur Ramadhan](https://github.com/ziyanagil) | 13622076 | Notification and Progress Chart                                                              |  

---

