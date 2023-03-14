import re
import os
import requests
import pyperclip
import subprocess
import configparser

def read_config():
        config = configparser.ConfigParser()
        config.read("./config.ini")
        return config["config"]["save_path_folder"]

def get_videoID(videoLink):
    pattern = r"https://www\.youtube\.com/watch\?v=(.{11})|https://youtu\.be/(.{11})"
    try:
        videoID = re.findall(pattern, videoLink)[0]
        if videoID[0]:
            return videoID[0]
        else:
            return videoID[-1]
    except:
        return

def save_image(path, videoID, content):
    file_name = os.path.join(path, videoID + ".jpg")
    with open(file_name, 'wb') as image:
        image.write(content)
    subprocess.Popen(f'explorer /select, {file_name}')



def get_image(videoLink):
    videoID = get_videoID(videoLink)
    path = read_config()
    # print(path)
    if videoID:
        previewLink = (f'https://i.ytimg.com/vi/{videoID}/maxresdefault.jpg')
        src = requests.get(previewLink)
        if not src.status_code == 404:
            save_image(path, videoID, src.content)
        else:
            previewLink = (f'https://i.ytimg.com/vi/{videoID}/hqdefault.jpg')
            src = requests.get(previewLink)
            save_image(path, videoID, src.content)
        return True

def check_clickboard(videoLink):
    if get_videoID(videoLink):
        return True





        





def main():
    if get_image(videoLink="https://www.youtube.com/watch?v=yG8OCfPYSrs"):
        print("link")
    else:
        print('anime')
    # print(check_clipboard())

if __name__ == "__main__":
    main()