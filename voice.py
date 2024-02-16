import re
import speech_recognition as sr
from vosk import Model
import pyttsx3


class VoiceRecognize:
    def __init__(self, model_path):
        # 创建一个Recognizer对象
        self.audio = None
        self.bot = BotSpeak()
        self.r = sr.Recognizer()
        self.r.vosk_model = Model(model_path=model_path)
        if "en" in model_path:
            self.language = 'en'
        else:
            self.language = 'zh-cn'

    def get_audio(self):
        print("begin record audio...")
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=1)
            self.audio = self.r.listen(source)
        print("finish record audio")

    def recognize(self, audio=None):
        if audio:
            self.audio = audio
            self.bot = BotSpeak()
        print("begin recognize audio...")
        text = self.r.recognize_vosk(self.audio, language=self.language)
        text = eval(text).get("text")
        print("you said:", text)
        my_re = re.compile(r'[A-Za-z]', re.S)
        alpha_num = len(re.findall(my_re, text))
        if text == "":
            text = "Not recognize"
            self.bot.speak_out("不好意思请再说一遍")
        elif alpha_num:  # english
            pass
            self.bot.speak_out(text)
        else:            # chinese
            text = text.replace(' ', '')
            self.bot.speak_out(text)
        print("finish recognize audio")
        return text


class BotSpeak:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak_out(self, text):
        self.engine.say(text)
        self.engine.runAndWait()



