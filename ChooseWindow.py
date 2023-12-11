from PyQt6.QtWidgets import *
from admin_main import AdminExcel
from admin_main import AdminDatabase


class AdminChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.currentUser = None

        self.setWindowTitle("Выбор")
        self.setGeometry(0, 0, 200, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.excel_button = QPushButton('Отчёты')
        self.excel_button.clicked.connect(self.to_excel)
        self.main_button = QPushButton('База данных')
        self.main_button.clicked.connect(self.to_main)
        self.back_button = QPushButton('Назад')
        self.back_button.clicked.connect(self.close)

        layout.addWidget(self.excel_button)
        layout.addWidget(self.main_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        self.center()

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def open_window(self, window_class):
        try:
            if self.currentUser:
                self.currentUser.close()
            self.currentUser = window_class()
            self.currentUser.show()
        except Exception as e:
            self.error_message(f'Ошибка: {str(e)}')

    def to_main(self):
        self.open_window(AdminDatabase)

    def to_excel(self):
        self.open_window(AdminExcel)

    def error_message(self, text):
        QMessageBox.warning(self, "Ошибка", text)
