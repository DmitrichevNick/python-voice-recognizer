from threading import Thread
import time
import codecs
import speech_recognition as sr

subtitles = ""
class WriterThread(Thread):
    def __init__(self, name):
        print("create")
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        messages = []
        global subtitles

        while True:
            time.sleep(0.1)
            if len(subtitles) > 0 :
                messages.insert(len(messages), "   "+subtitles+"\n")
                if len(messages) == 4:
                    messages.pop(0)
                print("write")
                f = codecs.open("path of govno", "w", "utf-8")
                f.writelines(messages)
                f.close()
                subtitles = ""

def create_threads(): 
    name = "WriterThread"
    thread = WriterThread(name)
    thread.start()


voiceRecognizer = sr.Recognizer()
voiceRecognizer.non_speaking_duration = 0.1
voiceRecognizer.pause_threshold = 0.1
voiceRecognizer.phrase_threshold = 0.1

create_threads()

while True:
    with sr.Microphone() as source:
        audio_text = voiceRecognizer.listen(source)

        try:
            subtitles = voiceRecognizer.recognize_google(audio_text, language="ru-RU",show_all=True)

        except:
            t = 1