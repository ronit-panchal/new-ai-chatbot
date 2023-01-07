"//write a python code for ai chatbot?"
undefinedCode:
# To be able to convert text to Speech
! pip install SpeechRecognition  #(3.8.1)
#To convey the Speech to text and also speak it out
!pip install gTTS  #(2.2.3)
# To install our language model
!pip install transformers  #(4.11.3)
!pip install tensorflow #(2.6.0, or pytorch)

undefinedWe will start by importing some basic functions:
import numpy as np

undefinedWe will begin by creating an empty class which we will build step by step. To build the chatbot, we would need to execute the full script. The name of the bot will be “ Dev”
# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name
# Execute the AI
if __name__ == "__main__":
    ai = ChatBot(name="Dev")

undefinedCode:
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

undefinedNote: The first task that our chatbot must work for is the speech to text conversion. Basically, this involves converting the voice or audio signals into text data. In summary, the chatbot actually ‘listens’ to your speech and compiles a text file containing everything it could decipher from your speech. You can test the codes by running them and trying to say something aloud. It should optimally capture your audio signals and convert them into text.
# Execute the AI
if __name__ == "__main__":
     ai = ChatBot(name="Dev")
     while True:
         ai.speech_to_text()

undefinedCode:
def wake_up(self, text):
    return True if self.name in text.lower() else False

undefinedCode:
from gtts import gTTS
import os
@staticmethod
def text_to_speech(text):
    print("AI --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
    os.remove("res.mp3")

undefinedCode :
#Those two functions can be used like this
# Execute the AI
if __name__ == "__main__":
     ai = ChatBot(name="Dev")
     while True:
         ai.speech_to_text()
         ## wake up
         if ai.wake_up(ai.text) is True:
             res = "Hello I am Dev the AI, what can I do for you?"
         ai.text_to_speech(res)

undefinedCode:
import datetime
@staticmethod
def action_time():
    return datetime.datetime.now().time().strftime('%H:%M')
#and run the script after adding the above function to the AI class

undefinedimport datetime
undefined@staticmethod
undefineddef action_time():
undefined    return datetime.datetime.now().time().strftime('%H:%M')
undefined#and run the script after adding the above function to the AI class
# Run the AI
if __name__ == "__main__":
ai = ChatBot(name="Dev")
while True:
         ai.speech_to_text()
         ## waking up
         if ai.wake_up(ai.text) is True:
             res = "Hello I am Dev the AI, what can I do for you?"
         ## do any action
         elif "time" in ai.text:
            res = ai.action_time()
         ## respond politely
         elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(
                  ["you're welcome!","anytime!",
                   "no problem!","cool!",
                   "I'm here if you need me!","peace out!"])
         ai.text_to_speech(res)

undefinedCode:
import transformers
nlp = transformers.pipeline("conversational", 
                            model="microsoft/DialoGPT-medium")
#Time to try it out
input_text = "hello!"
nlp(transformers.Conversation(input_text), pad_token_id=50256)

undefinedCode:
chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
res = str(chat)
res = res[res.find("bot >> ")+6:].strip()

undefinedFinal Code:
# for speech-to-text
import speech_recognition as sr
# for text-to-speech
from gtts import gTTS
# for language model
import transformers
import os
import time
# for data
import os
import datetime
import numpy as np
# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Me  --> ", self.text)
        except:
            print("Me  -->  ERROR")
    @staticmethod
    def text_to_speech(text):
        print("Dev --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        statbuf = os.stat("res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        os.system('start res.mp3')  #if you are using mac->afplay or else for windows->start
        # os.system("close res.mp3")
        time.sleep(int(50*duration))
        os.remove("res.mp3")
    def wake_up(self, text):
        return True if self.name in text.lower() else False
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
# Running the AI
if __name__ == "__main__":
    ai = ChatBot(name="dev")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    ex=True
    while ex:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Dave the AI, what can I do for you?"
        ## action time
        elif "time" in ai.text:
            res = ai.action_time()
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
        elif any(i in ai.text for i in ["exit","close"]):
            res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
            ex=False
        ## conversation
        else:   
            if ai.text=="ERROR":
                res="Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()
        ai.text_to_speech(res)
    print("----- Closing down Dev -----")

