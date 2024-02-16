import os

import tkinter as tk
from tkinter import messagebox, filedialog

import speech_recognition as sr

from voice_thread import VoiceThread
from voice import VoiceRecognize, BotSpeak

cn_model_path = "model\\vosk-model-small-cn-0.22"
en_model_path = "model\\vosk-model-small-en-us-0.15"


class RollCallApp:
    def __init__(self, master):
        self.thread_cn = None
        self.thread_en = None

        self.master = master
        self.master.title("voice recognize system")
        # self.master.resizable(False, False)
        self.master.protocol("WM_DELETE_WINDOW", self.display_messagebox)  # 弹窗提示确认退出
        self.master.attributes('-topmost', True)

        # bot speak
        self.bot = BotSpeak()

        self.rec = sr.Recognizer()

        # load two model at the same time
        self.english = VoiceRecognize(en_model_path)
        self.chinese = VoiceRecognize(cn_model_path)
        self.file_use = None

        # Chinese button
        self.cn_button = tk.Button(self.master, text="中文", font=("宋体", 20, 'bold'),
                                   width=7, cursor="hand2",
                                   command=self.chinese_recognize)
        self.cn_button.pack(fill="x", expand=True, side="left", padx=11)

        # English button
        self.cn_button = tk.Button(self.master, text="English", font=("宋体", 20, 'bold'),
                                   width=7, cursor="hand2",
                                   command=self.english_recognize)
        self.cn_button.pack(fill="x", expand=True, side="left", padx=11)

        # upload .wav file
        self.file_button = tk.Button(self.master, text="Upload", font=("宋体", 20, 'bold'), width=7, cursor="hand2",
                                     command=self.open_file)
        self.file_button.pack(fill="x", expand=True, side="left", padx=11)

        # Stop button
        self.cn_button = tk.Button(self.master, text="Pause&Clear", font=("宋体", 15, 'bold'),
                                   width=7, cursor="hand2",
                                   command=self.pause_work)
        self.cn_button.pack(fill="x", expand=True, side="left", padx=11)

        # show voice result
        self.text_show = tk.Text(self.master, width=40, height=15)
        self.text_show.pack(fill="x", expand=True, side="bottom", padx=11)

    def open_file(self):
        if self.thread_en:
            self.thread_en.pause()
            print("thread_en paused")
        if self.thread_cn:
            self.thread_cn.pause()
            print("thread_cn paused")

        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        print('已经打开文件：', file_path)
        if "en" in file_path:
            self.file_use = self.english
        else:
            self.file_use = self.chinese
        if file_path is None:
            print("file_path is not exit")
            return
        source_file = sr.AudioFile(file_path)
        with source_file as source:
            audio = self.rec.record(source)
        result = self.file_use.recognize(audio)
        print("file recognize result:", result)
        self.refreshText(result)

    def chinese_recognize(self):
        if self.thread_en:
            self.thread_en.pause()
            print("thread_en paused")

        if self.thread_cn is None:
            self.thread_cn = VoiceThread(args=(self.chinese, self.text_show, tk))
            self.thread_cn.start()
            self.bot.speak_out("请说汉语")
        else:
            self.thread_cn.resume()
            self.bot.speak_out("请说汉语")

    def english_recognize(self):
        if self.thread_cn:
            self.thread_cn.pause()
            print("thread_cn paused")

        if self.thread_en is None:
            self.thread_en = VoiceThread(args=(self.english, self.text_show, tk))
            self.thread_en.start()
            self.bot.speak_out("please speak english")
        else:
            self.thread_en.resume()
            self.bot.speak_out("please speak english")

    def pause_work(self):
        if self.thread_en:
            self.thread_en.pause()
            print("thread_en paused")
        if self.thread_cn:
            self.thread_cn.pause()
            print("thread_cn paused")

        self.text_show.delete(0.0, tk.END)
        self.text_show.update()

    def display_messagebox(self):
        """弹窗提示是否确认退出程序"""
        if messagebox.askokcancel("退出程序", "确定要退出程序吗？"):
            self.master.destroy()

    def refreshText(self, new_text):
        self.text_show.delete(0.0, tk.END)
        self.text_show.insert(tk.INSERT, new_text)
        self.text_show.update()


if __name__ == "__main__":
    main_ui = tk.Tk()
    main_ui.config(background="blue")
    main_ui.geometry("1000x500")
    app = RollCallApp(main_ui)
    main_ui.mainloop()
