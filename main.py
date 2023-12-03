import pyttsx3
import pygame
import time


def file_exists(file_path):
    try:
        with open(file_path):
            return True
    except FileNotFoundError:
        return False


def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


mp3_file_path = "./voiceRecordings/Licht schalten.mp3"
if file_exists(mp3_file_path):
    play_mp3(mp3_file_path)
    print("File played")
else:
    print(file_exists(mp3_file_path))
