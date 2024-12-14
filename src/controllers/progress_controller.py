from src.models.progress import ProgressModel
from datetime import datetime
from src.ui.progress_ui import ProgressWindow

class ProgressController:
    def __init__(self, progress_window, db_path):
        self.progress_window = progress_window
        self.db_path = db_path
        self.progress_model = ProgressModel(db_path)  # Inisialisasi model untuk akses data

    def load_progress(self, month=None, year=None, view_type="Grafik Batang"):
        try:
            # Jika bulan dan tahun tidak diberikan, gunakan nilai saat ini
            if month is None or year is None:
                current_date = datetime.now()
                month = current_date.month
                year = current_date.year

            month_name_indonesia = [
                "Januari", "Februari", "Maret", "April", "Mei", "Juni",
                "Juli", "Agustus", "September", "Oktober", "November", "Desember"
            ]
            month_str = month_name_indonesia[month - 1]
            year_str = str(year)

            # Ambil data dari model
            data = self.progress_model.get_completed_tasks_per_week(f"{month:02}", year_str)

            # Format data untuk minggu dan progress
            weeks = [f"Minggu {i + 1}" for i in range(4)]
            progress = {week: 0 for week in weeks}

            # Mengisi data progress berdasarkan minggu yang ditemukan
            for week, count in data:
                week_index = int(week) - 1
                if 0 <= week_index < 4:
                    progress[weeks[week_index]] = count

            # Hapus minggu tanpa tugas untuk tampilan grafik lingkaran
            if view_type == "Grafik Lingkaran":
                progress = {k: v for k, v in progress.items() if v > 0}

            # Notifikasi jika tidak ada data tugas selesai
            if not progress:
                title2 = f"Tugas Selesai selama Periode {month_str} {year_str}"
                self.progress_window.update_chart({}, view_type, title2)
                return

            title = f"Tugas Selesai selama Periode {month_str} {year_str}"
            self.progress_window.update_chart(progress, view_type, title)

        except Exception as e:
            # Tangani error dan beri notifikasi ke pengguna
            self.progress_window.update_chart({}, view_type, "Terjadi kesalahan saat memuat data.")
            print(f"Error: {e}")
