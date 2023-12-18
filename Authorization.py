from PyQt6.QtWidgets import *
import sys


class AuthorizationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.currentUser = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Авторизация")
        self.setGeometry(0, 0, 400, 200)

        self.username_label = QLabel("Логин:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        close_button = QPushButton('Завершить программу')
        close_button.clicked.connect(sys.exit)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(close_button)
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
                self.to_admin_window()
            elif username.startswith('driver') and username.split()[1].isdigit() and username == password:
                self.to_driver_window()
            else:
                QMessageBox.warning(self, 'Предупреждение об ошибке', 'Не существующий логин или пароль')
                self.username_input.clear()
                self.password_input.clear()
        except:
            QMessageBox.warning(self, 'Предупреждение об ошибке', 'Проверьте введенные значения')
            self.username_input.clear()
            self.password_input.clear()

    def to_new_window(self, user):
        if self.currentUser:
            self.currentUser.close()
        self.currentUser = user
        self.currentUser.show()
        self.username_input.clear()
        self.password_input.clear()

    def to_admin_window(self):
        self.to_new_window(AdminChooseWindow())

    def to_driver_window(self):
        self.to_new_window(DriverWindow(self.username_input.text().split()[1]))


if __name__ == "__main__":
    from ChooseWindow import AdminChooseWindow
    from Driver import DriverWindow
    app = QApplication(sys.argv)
    app_window = AuthorizationWindow()
    app_window.show()
    sys.exit(app.exec())
