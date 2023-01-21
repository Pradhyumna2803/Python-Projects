import speech_recognition as sr
import pyttsx3 
import wikipedia
import pywhatkit


listener=sr.Recognizer()
player=pyttsx3.init()

def listen():
    with sr.Microphone() as ipdev:
        print("I am ready")
        voice_content=listener.listen(ipdev)
        text_comm=listener.recognize_google(voice_content)
        text_comm=text_comm.lower()   
        print(text_comm)
        return text_comm


def talk(text):
    player.say(text)
    player.runAndWait()

def run_bot():
    comm=listen()
    if "what is" in comm:
        comm=comm.replace("what is","")
        info=wikipedia.summary(comm,5)
        talk(info)
    elif "who is" in comm:
        comm=comm.replace("who is","")
        info=wikipedia.summary(comm,5)
        talk(info)
    elif "play" in comm:
        comm=comm.replace("play","")
        pywhatkit.playonyt(comm)
    else:
        talk("Sorry I am unable to find what you are looking for")

run_bot()
