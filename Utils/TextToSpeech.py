import pyttsx3


class TextToSpeech:

    def __init__(self, rate=None, volume=None, voice=None):
        self.engine = pyttsx3.init()  # object creation

        if rate is None:
            rate = 150

        if volume is None:
            volume = 1.0

        if voice is None or voice > 1:
            voice = 1

        # RATE
        self.engine.setProperty('rate', rate)  # setting up new voice rate

        # VOLUME
        self.engine.setProperty('volume', volume)  # setting up volume level, range [0, 1]

        # VOICE
        voices = self.engine.getProperty('voices')  # getting details of current voices
        self.engine.setProperty('voice', voices[voice].id)  # 0 for female, 1 for male

    def say(self, string):
        self.engine.say(string)
        self.engine.runAndWait()
        self.engine.stop()


text_1 = "Hello World Sentence Is False"

TextToSpeech().say("Heya Fool, Stop Playing Minecraft, It's Been An Hour Already")
