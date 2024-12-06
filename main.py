import sys
from PyQt5.QtWidgets import QApplication
from src.ui.home_ui import HomeWindow
from src.controllers.home_controller import HomeController
# from src.utils.database import initialize_database


def main():
    """
    Entry point for the application.
    Sets up the database, initializes the main window, and starts
    the event loop.
    """
    # Initialize the PyQt5 application
    app = QApplication(sys.argv)

    # Set up the database
    # initialize_database()  # Ensure the database is set up before use

    # Load the main window and initialize the controller
    main_window = HomeWindow()
    home_controller = HomeController(main_window)  # Inject dependency

    # Show the main window
    main_window.show()

    # Start the application event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
