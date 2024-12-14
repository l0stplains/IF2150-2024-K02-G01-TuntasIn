import sqlite3
from datetime import datetime, timedelta

def initialize_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        due_date DATE NOT NULL,
        status TEXT NOT NULL
    );
    """)

    # Menyisipkan data sample jika tabel masih kosong
    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] == 0:
        # Menambahkan data tugas berdasarkan minggu
        data_tugas = [
            # Oktober 2024
            ('Tugas 1', '2024-10-01', 'Completed'),
            ('Tugas 2', '2024-10-02', 'Completed'),
            ('Tugas 3', '2024-10-02', 'Completed'),
            ('Tugas 4', '2024-10-03', 'Completed'),
            ('Tugas 5', '2024-10-03', 'Completed'),
            ('Tugas 6', '2024-10-04', 'Completed'),
            ('Tugas 7', '2024-10-10', 'Completed'),
            ('Tugas 8', '2024-10-10', 'Completed'),
            ('Tugas 9', '2024-10-11', 'Completed'),
            ('Tugas 10', '2024-10-17', 'Completed'),

            # November 2024
            ('Tugas 11', '2024-11-01', 'Completed'),
            ('Tugas 12', '2024-11-05', 'Completed'),
            ('Tugas 13', '2024-11-06', 'Completed'),
            ('Tugas 14', '2024-11-10', 'Completed'),
            ('Tugas 15', '2024-11-11', 'Completed'),
            ('Tugas 16', '2024-11-12', 'Completed'),
            ('Tugas 17', '2024-11-13', 'Completed'),
            ('Tugas 18', '2024-11-14', 'Completed'),
            ('Tugas 19', '2024-11-16', 'Completed'),
            ('Tugas 20', '2024-11-20', 'Completed'),
            ('Tugas 21', '2024-11-22', 'Completed'),
            ('Tugas 22', '2024-11-23', 'Completed'),
            ('Tugas 23', '2024-11-25', 'Completed'),
            ('Tugas 24', '2024-11-26', 'Completed'),

            # Desember 2024
            ('Tugas 25', '2024-12-01', 'Completed'),
            ('Tugas 26', '2024-12-02', 'Completed'),
            ('Tugas 27', '2024-12-03', 'Completed'),
            ('Tugas 28', '2024-12-09', 'Completed'),
            ('Tugas 29', '2024-12-10', 'Completed'),
            ('Tugas 30', '2024-12-12', 'Completed'),
            ('Tugas 31', '2024-12-14', 'Completed'),
            ('Tugas 32', '2024-12-16', 'Completed'),
            ('Tugas 33', '2024-12-17', 'Completed'),
            ('Tugas 34', '2024-12-20', 'Completed'),
            ('Tugas 35', '2024-12-23', 'Completed'),
            ('Tugas 36', '2024-12-24', 'Completed'),
        ]
        
        cursor.executemany("INSERT INTO tasks (title, due_date, status) VALUES (?, ?, ?)", data_tugas)

    conn.commit()
    conn.close()

