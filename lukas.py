import numpy as np
# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name
# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="Dev")

undefinedCode: speech_to_text
import speech_recognition as sr
def speech_to_text(self):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
         print("listening...")
         audio = recognizer.listen(mic)
    try:
         self.text = recognizer.recognize_google(audio)
         print("me --> ", self.text)
    except:
         print("me -->  ERROR")