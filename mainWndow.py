import os
import sys
import subprocess
import configparser
import requests
import platform
import processing
import pyperclip
from re import findall
from settingsWindow import SettingsWindow
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.save_path_folder = self.config["config"]["save_path_folder"]
        self.setFixedSize(350, 200)
        self.setWindowTitle("Youtube Preview Downloader")
        # # self.setStyleSheet('background-color:#160b21')
        self.setWindowIcon(QtGui.QIcon('resource\main_icon.png'))
        
        # if processing.check_clickboard(pyperclip.paste()):
        #     self.text_filed.setText(pyperclip.paste())
        #     self.label.setText("Pasted link from clipboard")

        self.layout()

        # self.show()

    def layout(self):
        # https://stackoverflow.com/questions/37304684/qwidgetsetlayout-attempting-to-set-qlayout-on-mainwindow-which-already
        widget = QtWidgets.QWidget()

        vlayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Youtube Preview Downloader")

        url_groupbox = QtWidgets.QGroupBox("URL")
        url_btn_layout = QtWidgets.QVBoxLayout()
        url_hbox = QtWidgets.QHBoxLayout()
        self.url = QtWidgets.QLineEdit()
        self.url.setFixedHeight(20)
        self.url.setSizePolicy(QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Minimum)
        url_hbox.addWidget(self.url)

        btn_hbox = QtWidgets.QHBoxLayout()
        self.btn_download = QtWidgets.QPushButton()
        self.btn_download.setFixedHeight(40)
        self.btn_download.setSizePolicy(QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Minimum)
        self.btn_download.setText("Download")
        self.btn_download.clicked.connect(self.pushed_btn_download)
        
        self.btn_open_dir = QtWidgets.QPushButton()
        self.btn_open_dir.setFixedSize(40, 40)
        self.btn_open_dir.setIcon(QtGui.QIcon('resource/folder512_dark.png'))
        self.btn_open_dir.setToolTip('Open Previews Folder') 
        self.btn_open_dir.clicked.connect(self.pushed_btn_open_dir)

        self.btn_settings = QtWidgets.QPushButton()
        self.btn_settings.setFixedSize(40, 40)
        self.btn_settings.setToolTip('Configure') 
        self.btn_settings.setIcon(QtGui.QIcon('resource/settings512_dark.png'))
        self.btn_settings.clicked.connect(self.pushed_btn_settings)
        btn_hbox.addWidget(self.btn_download)
        btn_hbox.addWidget(self.btn_open_dir)
        btn_hbox.addWidget(self.btn_settings)

        url_btn_layout.addLayout(url_hbox)
        url_btn_layout.addLayout(btn_hbox)
        
        vlayout.addWidget(self.label)
        vlayout.addWidget(url_groupbox)
        url_groupbox.setLayout(url_btn_layout)

        # vlayout.addLayout(url_hbox)
        # vlayout.addSpacing(10)
        # vlayout.addLayout(btn_hbox)

        widget.setLayout(vlayout)
        self.setCentralWidget(widget)

    def pushed_btn_download(self):
        if processing.get_image(self.url.text()):
            self.label.setText('Preview successfully downloaded!\nOpening Folder')
            

    def pushed_btn_settings(self):
        self.settings = SettingsWindow(path=self.save_path_folder)
        self.settings.show()
        return self.settings

    def pushed_btn_open_dir(self):
        # print(f'explorer', f'{self.save_path_folder}')
        subprocess.Popen(f'explorer {self.save_path_folder}')
        self.label.setText('Opening Folder')
        


def winapp():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    winapp()