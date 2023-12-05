from PyQt6.QtWidgets import *


class AdminChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.currentUser = None

        self.setWindowTitle("Выбор")
        self.setGeometry(0, 0, 200, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.excel_button = QPushButton('Excel')
        self.excel_button.clicked.connect(self.to_excel)
        self.main_button = QPushButton('Database')
        self.main_button.clicked.connect(self.to_main)
        self.back_button = QPushButton('Back')
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

    def to_main(self):
        try:
            from admin_main import AdminDatabase
            if self.currentUser:
                self.currentUser.close()
            self.currentUser = AdminDatabase()
            self.currentUser.show()
        except:
            self.error_message('Ошибка подключения к бд')

    def to_excel(self):
        try:
            from admin_main import AdminExcel
            if self.currentUser:
                self.currentUser.close()
            self.currentUser = AdminExcel()
            self.currentUser.show()
        except:
            self.error_message('Ошибка')

    def error_message(self, text):
        QMessageBox.information(self, "Ошибка", text)
