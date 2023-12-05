import speech_recognition as sr


# Using https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
def speech_to_text(mp3FilePath):
    recognizer = sr.Recognizer()

    with sr.AudioFile(mp3FilePath) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, None, "de-DE")
        return text

