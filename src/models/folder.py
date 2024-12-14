import sqlite3
import os
from PyQt5.QtWidgets import QMessageBox

class FileModel:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):

        # Create the Attachment table with the correct syntax
        query_attachment = """
        CREATE TABLE IF NOT EXISTS Attachment (
            attachmentId INTEGER PRIMARY KEY AUTOINCREMENT,
            filePath TEXT,
            fileName TEXT,
            fileSize INTEGER,
            taskId INTEGER,
            fileData BLOB,
            FOREIGN KEY (taskId) REFERENCES Task (taskId)
        );
        """
        self.conn.execute(query_attachment)
        self.conn.commit()

    def add_file(self, name, path, file_data, task_id):
        # Get the file size
        file_size = len(file_data)
        query = "INSERT INTO Attachment (fileName, filePath, fileSize, fileData, taskId) VALUES (?,?,?,?,?)"
        self.conn.execute(query, (name, path, file_size, file_data, task_id))
        self.conn.commit()

    def save_file_from_path(self, file_path, task_id):
        """
        Save a file into the database from a file path.
        """
        with open(file_path, 'rb') as file:
            file_data = file.read()
        self.add_file(os.path.basename(file_path), file_path, file_data, task_id)

    def populate_from_folder(self, folder_path, task_id):
        """
        Populate the database with files from a given folder.
        If the folder doesn't exist or is empty, insert dummy data.
        """
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    self.save_file_from_path(file_path, task_id)
        else:
            # Insert dummy data
            dummy_files = [
                ("example1.txt", b"This is dummy text for file 1."),
                ("example2.pdf", b"%PDF-1.4 Dummy PDF content."),
                ("example3.jpg", b"\xFF\xD8\xFF Dummy JPEG content."),
            ]
            for name, data in dummy_files:
                self.add_file(name, "dummy_path", data, task_id)

    def get_all_files(self):
        """
        Retrieve all files with their associated task titles.
        """
        query = """
        SELECT 
            a.attachmentId, 
            a.fileName, 
            a.filePath, 
            a.fileSize, 
            t.title AS taskName 
        FROM 
            Attachment a
        LEFT JOIN 
            Task t
        ON 
            a.taskId = t.taskId
        """
        return self.conn.execute(query).fetchall()

    def retrieve_and_print_files(self):
        """
        Retrieve and print all files stored in the database.
        """
        files = self.get_all_files()
        for attachment_id, name, path, size, task_name in files:
            print(f"ID: {attachment_id}, Name: {name}, Path: {path}, Size: {size} bytes, Task: {task_name or 'None'}")
    
    def retrieve_and_open_file(self, attachment_id):
        """
        Retrieve a file from the database and open it.
        """
        try:
            # Query to fetch the file name and file data
            query = "SELECT fileName, fileData FROM Attachment WHERE attachmentId = ?"
            cursor = self.conn.execute(query, (attachment_id,))
            result = cursor.fetchone()

            if result:
                file_name, file_data = result

                # Save the file to the local filesystem
                output_path = os.path.join("retrieved_files", file_name)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'wb') as file:
                    file.write(file_data)

                print(f"File saved to '{output_path}'.")

                # Open the file
                if os.name == 'nt':  # Windows
                    os.startfile(output_path)
                elif os.name == 'posix':  # macOS/Linux
                    subprocess.run(["xdg-open", output_path])
                else:
                    print(f"File saved but cannot open automatically on this OS.")
            else:
                print("No file found with the specified attachment ID.")
        except Exception as e:
            print(f"Error retrieving file: {str(e)}")
        
    def open_file(self, file_path):
        try:
            import os
            os.startfile(file_path)  # Works on Windows to open files
        except Exception as e:
            QMessageBox.critical(self.folder_ui, "Error", f"Could not open file: {e}")
    
    def delete_file(self, attachment_id):
        try:
            query = "SELECT filePath FROM Attachment WHERE attachmentId = ?"
            cursor = self.conn.execute(query, (attachment_id,))
            result = cursor.fetchone()

            if result:
                delete_query = "DELETE FROM Attachment WHERE attachmentId = ?"
                self.conn.execute(delete_query, (attachment_id,))
                self.conn.commit()
                
            else:
                print(f"No file found with attachment ID: {attachment_id}")

        except Exception as e:
            print(f"Error deleting file: {str(e)}")

    def close_connection(self):
        self.conn.close()

# Example usage
if __name__ == "__main__":
    model = FileModel()
    task_id = 1  # Example taskId, this should be obtained from your Task table or elsewhere
    model.populate_from_folder("files", -1)  # Specify the folder with files you want to populate
    model.retrieve_and_print_files()
    model.close_connection()