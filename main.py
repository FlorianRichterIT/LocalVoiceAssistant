from speechToText.speechToText import speech_to_text


def file_exists(file_path):
    try:
        with open(file_path):
            return True
    except FileNotFoundError:
        return False


mp3_file_path = "./voiceRecordings/Licht schalten.wav"

if file_exists(mp3_file_path):
    # It is using the google speech to text api
    print(speech_to_text(mp3_file_path))
