import speechToText.playMp3 as playMp3
import speechToText.speechToText as speechToText


def file_exists(file_path):
    try:
        with open(file_path):
            return True
    except FileNotFoundError:
        return False


mp3_file_path = "./voiceRecordings/Licht schalten.mp3"
if file_exists(mp3_file_path):
    playMp3.play_mp3(mp3_file_path)
    speechToText.speech_to_text(mp3_file_path)
    #transcribe_mp3()
else:
    print(file_exists(mp3_file_path))
