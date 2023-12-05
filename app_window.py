from PyQt6.QtWidgets import *
import sys


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.currentUser = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Authorization")
        self.setGeometry(0, 0, 400, 200)

        self.username_label = QLabel("login:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("sign_in")
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        close_button = QPushButton('Завершить программу')
        layout.addWidget(close_button)
        close_button.clicked.connect(sys.exit)
        self.setLayout(layout)

        self.center()

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        try:
            if username == 'admin' and password == 'admin':
                self.to_database_window()
            elif username.split()[0] == 'driver' and username.split()[1].isdigit() and username == password:
                self.to_driver_window()
            else:
                self.error_message('Не существующий логин или пароль')
        except:
            print('Введены некорректные значения')

    def error_message(self, text):
        QMessageBox.information(self, "Ошибка", text)

    def to_database_window(self):
        if self.currentUser:
            self.currentUser.close()
        self.currentUser = AdminChooseWindow()
        self.currentUser.show()

    def to_driver_window(self):
        if self.currentUser:
            self.currentUser.close()
        self.currentUser = DriverWindow(self.username_input.text().split()[1])
        self.currentUser.show()


if __name__ == "__main__":
    from ChooseWindow import AdminChooseWindow
    from driver_window import DriverWindow
    app = QApplication(sys.argv)

    app_window = AppWindow()
    app_window.show()

    sys.exit(app.exec())
