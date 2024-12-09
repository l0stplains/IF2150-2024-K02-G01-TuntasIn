import sqlite3
import os

class FileModel:
    def __init__(self, db_name="files.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tag TEXT NOT NULL,
            file_data BLOB NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_file(self, name, tag, file_data):
        query = "INSERT INTO files (name, tag, file_data) VALUES (?,?,?)"
        self.conn.execute(query, (name, tag ,file_data))
        self.conn.commit()

    def save_file_from_path(self, file_path):
        """
        Save a file into the database from a file path.
        """
        with open(file_path, 'rb') as file:
            file_data = file.read()
        self.add_file(os.path.basename(file_path), file_data)

    def populate_from_folder(self, folder_path):
        """
        Populate the database with files from a given folder.
        If the folder doesn't exist or is empty, insert dummy data.
        """
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    self.save_file_from_path(file_path)
        else:
            # Insert dummy data
            dummy_files = [
                ("example1.txt", b"This is dummy text for file 1."),
                ("example2.pdf", b"%PDF-1.4 Dummy PDF content."),
                ("example3.jpg", b"\xFF\xD8\xFF Dummy JPEG content."),
            ]
            for name, data in dummy_files:
                self.add_file(name, data)

    def get_all_files(self):
        query = "SELECT id, name, file_data FROM files"
        return self.conn.execute(query).fetchall()

    def retrieve_and_print_files(self):
        """
        Retrieve and print all files stored in the database.
        """
        files = self.get_all_files()
        for file_id, name, file_data in files:
            print(f"ID: {file_id}, Name: {name}, Size: {len(file_data)} bytes")

    def close_connection(self):
        self.conn.close()
        
if __name__ == "__main__":
    model = FileModel()
    model.populate_from_folder("files")
    model.retrieve_and_print_files()
    model.close_connection()
