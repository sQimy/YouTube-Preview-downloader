from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from re import findall


import subprocess
import requests
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Preview")
        self.setGeometry(650, 400, 600, 250)

        #хуй знает
        self.new_text = QtWidgets.QLabel(self)

        #Надпись URL
        self.header = QtWidgets.QLabel(self)
        self.header.setText("URL")
        self.header.move(100, 100)
        self.header.adjustSize()

        #Кнопка скачать
        self.button_download = QtWidgets.QPushButton(self)
        self.button_download.setText("Download")
        self.button_download.move(300, 100)
        self.button_download.adjustSize()
        self.button_download.clicked.connect(self.script)

    def script(self):
        self.new_text.setText("ХУй")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()