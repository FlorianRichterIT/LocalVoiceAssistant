from pocketsphinx import LiveSpeech
from pocketsphinx import AudioFile


def speech_to_text(mp3FilePath):
    # Initialisiere den AudioFile-Recognizer für die MP3-Datei
    audio = AudioFile(audio_file=mp3FilePath)

    # Warte auf Spracheingabe und erkenne den Text
    for phrase in audio:
        print("Erkannter Text:", phrase)


def transcribe_mp3():
    # Initialisiere den LiveSpeech-Recognizer
    speech = LiveSpeech()

    print("Spreche etwas... (Drücke Ctrl+C zum Beenden)")

    # Warte auf Spracheingabe und erkenne den Text
    for phrase in speech:
        print("Erkannter Text:", phrase)