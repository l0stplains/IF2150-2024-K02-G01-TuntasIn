from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QToolBar, QLabel, QSizePolicy, QDialog, QComboBox, QDialogButtonBox
)
from PyQt5.QtGui import QColor, QFont, QPainter, QCursor, QGuiApplication
from PyQt5.QtChart import (
    QChart, QChartView, QBarSet, QBarSeries, QPieSeries, QBarCategoryAxis, QValueAxis
)
from PyQt5.QtCore import Qt, QDate
from datetime import datetime


class ProgressWindow(QWidget):
    def __init__(self, progress_controller=None):
        super().__init__()
        self.setWindowTitle("Progress Tugas")

        # Save reference to ProgressController (if available)
        self.progress_controller = progress_controller

        # Setup UI
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create a main layout if not already done
        layout = QVBoxLayout(self)
        # Add the central widget to the main layout
        layout.addWidget(self.central_widget)

        # "Chart View" and "Period" buttons
        button_layout = QHBoxLayout()

        # "Chart View" buttons
        self.view_button = QPushButton("Chart View")
        self.view_button.setObjectName("viewButton")
        self.view_button.setFixedSize(120, 40)
        self.view_button.setCursor(QCursor(Qt.PointingHandCursor))

        # "Period" buttons
        self.period_button = QPushButton("Period")
        self.period_button.setObjectName("periodButton")
        self.period_button.setFixedSize(120, 40)
        self.period_button.setCursor(QCursor(Qt.PointingHandCursor))

        # Add buttons to layout and stretch to right
        button_layout.addStretch()
        button_layout.addWidget(self.view_button)
        button_layout.addWidget(self.period_button)
        self.main_layout.addLayout(button_layout)

        # Margin and padding for layout
        self.main_layout.setContentsMargins(20, 20, 20, 20)

        # Chart setup
        self.chart = QChart()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.main_layout.addWidget(self.chart_view)

        # Button connections
        self.view_button.clicked.connect(self.change_view_type)
        self.period_button.clicked.connect(self.select_period)

        # Default initial values
        self.selected_month = QDate.currentDate().month()  # Current month
        self.selected_year = datetime.now().year
        self.view_type = "Bar Chart"


    def set_progress_controller(self, controller):
        """Set the ProgressController to link the ProgressWindow with its controller."""
        self.progress_controller = controller

    def change_view_type(self):
        """Dialog untuk memilih jenis tampilan (Grafik Batang atau Lingkaran)."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Chart View")

        dialog.setMinimumWidth(300)
        dialog.setMinimumHeight(150)

        layout = QVBoxLayout()

        view_combo = QComboBox()
        view_combo.addItems(["Bar Chart", "Pie Chart"])
        view_combo.setCurrentText(self.view_type)

        view_combo.setObjectName("viewComboBox")

        view_combo.setFixedSize(250, 40)

        layout.addWidget(view_combo)

        # "OK" and "Cancel" buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # Set ObjectName untuk tombol
        buttons.button(QDialogButtonBox.Ok).setObjectName("okButton")
        buttons.button(QDialogButtonBox.Cancel).setObjectName("cancelButton")

        layout.addWidget(buttons)

        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        dialog.setLayout(layout)

        if dialog.exec_() == QDialog.Accepted:
            selected_view = view_combo.currentText()
            if self.view_type != selected_view:
                self.view_type = selected_view
                self.apply_filters()

    def select_period(self):
        """Dialog untuk memilih periode (bulan dan tahun)."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Choose Period")

        dialog.setMinimumWidth(300)
        dialog.setMinimumHeight(200)

        layout = QVBoxLayout()

        # Layout for month
        month_layout = QHBoxLayout()
        month_label = QLabel("Month:")
        month_label.setObjectName("Month")
        month_layout.addWidget(month_label)
        month_combo = QComboBox()
        month_combo.setObjectName("monthComboBox")
        month_combo.addItems([
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        ])
        month_combo.setCurrentIndex(self.selected_month - 1)
        month_layout.addWidget(month_combo)
        layout.addLayout(month_layout)

        # Layout for year
        year_layout = QHBoxLayout()
        year_label = QLabel("Year:")
        year_label.setObjectName("Year")
        year_layout.addWidget(year_label)
        year_combo = QComboBox()
        year_combo.setObjectName("yearComboBox")
        current_year = datetime.now().year
        year_combo.addItems([str(year)
                            for year in range(2000, current_year + 1)])
        year_combo.setCurrentText(str(self.selected_year))
        year_layout.addWidget(year_combo)
        layout.addLayout(year_layout)

        # "OK" and "Cancel" buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # Objectname for "OK" and "Cancel" buttons
        buttons.button(QDialogButtonBox.Ok).setObjectName("okButton")
        buttons.button(QDialogButtonBox.Cancel).setObjectName("cancelButton")

        layout.addWidget(buttons)

        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        dialog.setLayout(layout)

        dialog.setLayout(layout)

        if dialog.exec_() == QDialog.Accepted:
            self.selected_month = month_combo.currentIndex() + 1
            self.selected_year = int(year_combo.currentText())
            self.apply_filters()

    def apply_filters(self):
        """Terapkan filter berdasarkan bulan, tahun, dan jenis tampilan."""
        if self.chart.series():
            self.clear_previous_display()
        self.progress_controller.load_progress(
            month=self.selected_month,
            year=self.selected_year,
            view_type=self.view_type
        )

    def clear_previous_display(self):
        """Hapus tampilan sebelumnya (grafik) dengan aman."""
        self.chart.removeAllSeries()

        # Clear X-axis if exists
        axis_x = self.chart.axisX()
        if axis_x:
            self.chart.removeAxis(axis_x)

        # Clear Y-axis if exists
        axis_y = self.chart.axisY()
        if axis_y:
            self.chart.removeAxis(axis_y)

    def update_chart(self, progress_data, view_type, title):
        self.chart.removeAllSeries()
        self.chart.setTitle(title)

        title_font = QFont("Segoe UI", 16, QFont.Bold)
        self.chart.setTitleBrush(QColor("#00008B"))
        self.chart.setTitleFont(title_font)

        # Clear X-axis and Y-axis before changing the chart type if they exist
        axis_x = self.chart.axisX()
        if axis_x is not None:
            self.chart.removeAxis(axis_x)

        axis_y = self.chart.axisY()
        if axis_y is not None:
            self.chart.removeAxis(axis_y)

        if view_type == "Bar Chart":
            # Make a bar chart
            bar_set = QBarSet("Task Completed")
            bar_set.append(list(progress_data.values()))
            series = QBarSeries()
            series.append(bar_set)
            self.chart.addSeries(series)

            # X-axis (Minggu)
            categories = list(progress_data.keys())
            axis_x = QBarCategoryAxis()
            axis_x.append(categories)
            self.chart.setAxisX(axis_x, series)
            axis_x.setTitleText("Week")

            # Font untuk label sumbu X
            axis_x_font = QFont("Segoe UI", 10)
            axis_x.setLabelsFont(axis_x_font)
            axis_x.setLabelsBrush(QColor("#4B77BE"))

            # Font untuk judul sumbu X (opsional)
            axis_x_title_font = QFont("Segoe UI", 12, QFont.Bold)
            axis_x.setTitleFont(axis_x_title_font)
            axis_x.setTitleBrush(QColor("#3A539B"))

            # Sumbu Y (Jumlah Tugas)
            axis_y = QValueAxis()
            axis_y.setRange(0, max(progress_data.values()) + 1)
            # Menggunakan bilangan bulat untuk sumbu Y
            axis_y.setTickCount(max(progress_data.values()) + 2)
            axis_y.setTitleText("Task Count")
            axis_y.setLabelFormat("%d")

            # Font untuk label sumbu Y
            axis_y_font = QFont("Segoe UI", 10)
            axis_y.setLabelsBrush(QColor("#4B77BE"))
            axis_y.setLabelsFont(axis_y_font)

            # Font untuk judul sumbu Y (opsional)
            axis_y_title_font = QFont("Segoe UI", 12, QFont.Bold)
            axis_y.setTitleFont(axis_y_title_font)
            axis_y.setTitleBrush(QColor("#3A539B"))

            self.chart.setAxisY(axis_y, series)

        elif view_type == "Pie Chart":
            # Create a pie chart
            pie_series = QPieSeries()
            total_tasks = sum(progress_data.values())
            for week, count in progress_data.items():
                if count > 0:
                    percentage = (count / total_tasks) * 100
                    slice_item = pie_series.append(
                        f"{week} ({percentage:.2f}%)", count)
                    slice_item.setLabelVisible(True)

                    pie_label_font = QFont("Segoe UI", 10)
                    pie_label_font.setBold(True)
                    slice_item.setLabelFont(pie_label_font)
                    slice_item.setLabelColor(QColor("#4B77BE"))

            self.chart.addSeries(pie_series)

            # Delete X-axis and Y-axis on pie chart
            axis_x = self.chart.axisX()
            if axis_x is not None:
                self.chart.removeAxis(axis_x)

            axis_y = self.chart.axisY()
            if axis_y is not None:
                self.chart.removeAxis(axis_y)
