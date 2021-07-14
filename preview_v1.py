from re import findall
import subprocess
import requests


#Получаем ссылку на превью 
inputLink = input('Youtube url: ')
pattern = r"=(.*)?="
videoID = list(findall(pattern, inputLink))
previewLink = (f'https://i.ytimg.com/vi/{videoID[0]}/maxresdefault.jpg')

#Сохраняем изображение
src = requests.get(previewLink)
with open(str(videoID[0]) + ".jpg", "wb") as image:
  image.write(src.content)

#Открываем папку с изображением
path = f'D:\Downloads\Preview\{videoID[0]}.jpg'
print(path)

#Выделяем файл в проводнике
subprocess.Popen(f'explorer /select, {path}')

status = input("Success")