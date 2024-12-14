import sys
import os
from PyQt5.QtWidgets import QApplication
from src.ui.home_ui import HomeWindow
from src.controllers.home_controller import HomeController
from src.ui.progress_ui import ProgressWindow
from src.controllers.progress_controller import ProgressController
from src.utils.database import initialize_database

def main():
    """
    Entry point for the application.
    Sets up the database, initializes the main window, and starts
    the event loop.
    """
    # Initialize the PyQt5 application
    app = QApplication(sys.argv)

    # Add style from external QSS file
    stylesheet_path = "src/styles/main.qss"
    if os.path.exists(stylesheet_path):
        with open(stylesheet_path, "r") as file:
            app.setStyleSheet(file.read())

    # Set up the database
    initialize_database()  # Ensure the database is set up before use

    # Initialize the main window first, then pass it to HomeController
    main_window = HomeWindow()  # Initialize main window
    home_controller = HomeController(main_window)  # Pass main window to controller

    # Initialize the progress window and controller
    db_path = "tasks.db"  # Define the database path
    progress_window = ProgressWindow(progress_controller=None)  # Temporary, will set in controller
    progress_controller = ProgressController(progress_window, db_path)  # Pass db_path to controller

    # Set up controller in progress window
    progress_window.set_progress_controller(progress_controller)

    # Show the main window
    main_window.show()

    # Optionally, show the progress window (e.g., on button click or condition)
    progress_window.show()

    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
