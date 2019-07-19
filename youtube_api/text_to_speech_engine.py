from playsound import playsound
import random


def text_to_speech(message):
    from gtts import gTTS

    # define variables
    file = 'audio_files/file{id}.mp3'.format(id=random.randint(1, 10000000))
    print("Defined Variables")
    # initialize tts, create mp3 and play
    tts = gTTS(message, 'en')
    tts.save(file)
    print("Saved TTS File")
    playsound(file)
    print("Played TTS File")


text_to_speech("Hello World")
print("TTS Completed")
