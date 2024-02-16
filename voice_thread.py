import threading
import time


class VoiceThread(threading.Thread):
    def __init__(self, args):
        super(VoiceThread, self).__init__()

        print("VoiceThread args", args)
        self.voice = args[0]
        self.text_show = args[1]
        self.tk = args[2]
        print("VoiceThread args", self.voice)

        self.iterations = 0
        self.daemon = True  # Allow main to exit even if still running.
        self.paused = True  # Start out paused.

        self.state = threading.Condition()

    def run(self):
        self.resume()
        while True:
            with self.state:
                if self.paused:
                    self.state.wait()  # Block execution until notified.

            # Do work
            self.voice.get_audio()
            result = self.voice.recognize()
            # self.text_show.delete(0.0, self.tk.END)
            # self.text_show.insert(self.tk.INSERT, result)
            self.text_show.insert(self.tk.END, result)
            self.text_show.insert(self.tk.END, "\n")
            self.text_show.update()

            time.sleep(.1)
            self.iterations += 1
            print("chat times is:", self.iterations)

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.
