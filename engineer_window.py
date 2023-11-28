from PyQt6.QtWidgets import *
import mysql.connector


class EngineerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inform_sys"
        )

        self.cursor = self.connection.cursor()

        self.setWindowTitle("Инженер")
        self.setGeometry(300, 300, 600, 400)

        self.init_ui()

    def init_ui(self):
        pass
