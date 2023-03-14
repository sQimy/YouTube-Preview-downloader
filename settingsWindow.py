import os
import sys
import subprocess
import configparser
import requests
import platform
import processing
import pyperclip
from re import findall
from PyQt5 import QtWidgets, QtGui, QtCore


class SettingsWindow(QtWidgets.QDialog):
    def __init__(self, path=None, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.path = path
        self.setWindowTitle("Settings")
        self.setWindowIcon(QtGui.QIcon('resource/settings512_dark.png'))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(QtWidgets.QSizePolicy.Fixed,  QtWidgets.QSizePolicy.Fixed)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.layout()

        
    def layout(self):
            
            vlayout = QtWidgets.QVBoxLayout()
            # https://pythonbasics.org/pyqt-groupbox/
            path_groupbox = QtWidgets.QGroupBox("Download folder")
            path_Hbox = QtWidgets.QHBoxLayout()
            self.path_lineEdit = QtWidgets.QLineEdit()
            self.path_lineEdit.setFixedSize(200, 20)
            self.path_lineEdit.setText(self.path)
            self.path_lineEdit.setSizePolicy(QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Minimum)

            self.btn_Browse = QtWidgets.QPushButton()
            self.btn_Browse.setFixedHeight(22)
            self.btn_Browse.setSizePolicy(QtWidgets.QSizePolicy.Maximum,  QtWidgets.QSizePolicy.Minimum)
            self.btn_Browse.setText("Browse")
            self.btn_Browse.clicked.connect(self.pushed_btn_Browse)
            path_Hbox.addWidget(self.path_lineEdit)
            path_Hbox.addWidget(self.btn_Browse)

            theme_groupbox = QtWidgets.QGroupBox("Theme")
            themeHbox = QtWidgets.QHBoxLayout()

            self.btn_theme_dark = QtWidgets.QPushButton()
            self.btn_theme_dark.setFixedHeight(23)
            self.btn_theme_dark.setText("Dark")
            self.btn_theme_dark.clicked.connect(self.pushed_btn_theme_dark)
            
            self.btn_theme_light = QtWidgets.QPushButton()
            self.btn_theme_light.setFixedHeight(23)
            self.btn_theme_light.setText("Light")
            self.btn_theme_light.clicked.connect(self.pushed_btn_theme_light)
            themeHbox.addWidget(self.btn_theme_dark)
            themeHbox.addWidget(self.btn_theme_light)
            
            controlHbox = QtWidgets.QHBoxLayout()
            controlHbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            self.btn_OK = QtWidgets.QPushButton()
            self.btn_OK.setFixedHeight(23)
            self.btn_OK.setText('Apply')
            self.btn_OK.clicked.connect(self.pushed_btn_OK)

            self.btn_Cancel = QtWidgets.QPushButton()
            self.btn_Cancel.setFixedHeight(23)
            self.btn_Cancel.setText('Cancel')
            self.btn_OK.clicked.connect(self.pushed_btn_Cancel)
            controlHbox.addWidget(self.btn_OK)
            controlHbox.addWidget(self.btn_Cancel)
            
            vlayout.addWidget(path_groupbox)
            path_groupbox.setLayout(path_Hbox)

            vlayout.addWidget(theme_groupbox)
            theme_groupbox.setLayout(themeHbox)

            vlayout.addLayout(controlHbox)

            self.setLayout(vlayout)

    def pushed_btn_Browse(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder for previews", 'C:\\')
        return path
    
    def pushed_btn_theme_dark(self):
        ...

    def pushed_btn_theme_light(self):
        ...

    def pushed_btn_OK(self):
         ...

    def pushed_btn_Cancel(self):
         ...


def winapp():
    app = QtWidgets.QApplication(sys.argv)
    settings = SettingsWindow()
    settings.show()
    app.exec()

if __name__=="__main__":
    winapp()