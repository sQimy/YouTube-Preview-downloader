from re import findall
from time import sleep
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import requests
import os.path, inspect, subprocess

Form, Window = uic.loadUiType("MainWindow.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def main(inputLink):
    #Ищем где запускаеться файл https://stackoverflow.com/a/44592299
    filename  = inspect.getframeinfo(inspect.currentframe()).filename
    exec_path = os.path.dirname(os.path.abspath(filename))

    #Получаем ссылку на превью 
    #inputLink = input('Youtube url: ')
    pattern = r"=(...........)"
    videoID = list(findall(pattern, inputLink))
    previewLink = (f'https://i.ytimg.com/vi/{videoID[0]}/maxresdefault.jpg')

    #Сохраняем изображение
    src = requests.get(previewLink)

    fullpath = os.path.join(exec_path, videoID[0] + ".jpg")
    image = open(fullpath, "wb")
    image.write(src.content)
    image.close()

    #выделяем файл в проводнике
    subprocess.Popen(f'explorer /select, {fullpath}')
'''
    print("Success")
    sleep(1)
    #status = input("Success ")
    print(videoID)
    print(exec_path)
    print(fullpath)
'''

def Button():
    inputLink = str(form.lineEdit.text())
    main(inputLink)

form.pushButton.clicked.connect(Button)
app.exec_()