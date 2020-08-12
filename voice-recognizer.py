from threading import Thread
import time
import codecs
import speech_recognition as sr

messages_stack = []
path = ""
language = "ru-RU"

class ListenerThread(Thread):
    global messages_stack
    voice_recognizer = None
    def __init__(self, name):
        print("listener created")
        Thread.__init__(self)
        self.name = name
        self.voice_recognizer = sr.Recognizer()
        self.voice_recognizer.non_speaking_duration = 0.001
        self.voice_recognizer.pause_threshold = 0.001
        self.voice_recognizer.phrase_threshold = 0.001
    
    def run(self):
        while True:
            with sr.Microphone() as source:
                audio_text = self.voice_recognizer.listen(source)

                try:
                    text = self.voice_recognizer.recognize_google(audio_text, language=language)
                    if bool(text):
                        messages_stack.append(text)
                        write_text(messages_stack.pop())
                        print(text)
                except Exception as exception:
                    nope = 0
                    #print(str(exception))

def create_threads(): 
    listener_thread = ListenerThread("listener-thread")
    listener_thread.start()

def write_text(text):
    f = codecs.open(path, "a", "utf-8")
    f.write(str(text).upper()+'\n')
    f.close()

create_threads()