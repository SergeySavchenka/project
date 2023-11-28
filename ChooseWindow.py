from PyQt6.QtWidgets import *
# import mysql.connector


class AdminChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.currentUser = None

        self.setWindowTitle("Выбор")
        self.setGeometry(400, 400, 200, 300)

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

    def to_main(self):
        from admin_main import AdminDatabase
        if self.currentUser:
            self.currentUser.close()
        self.currentUser = AdminDatabase()
        self.currentUser.show()

    def to_excel(self):
        from admin_main import AdminExcel
        if self.currentUser:
            self.currentUser.close()
        self.currentUser = AdminExcel()
        self.currentUser.show()


