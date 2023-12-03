import time
import pygame


def play_mp3(file_path):
    # Initialisiere den Pygame-Mixer (Audio-Engine von Pygame)
    pygame.mixer.init()

    # Lade die MP3-Datei in den Pygame-Mixer
    pygame.mixer.music.load(file_path)

    # Starte die Wiedergabe der geladenen MP3-Datei
    pygame.mixer.music.play()

    # Warte, bis die Wiedergabe abgeschlossen ist
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    print("File played")