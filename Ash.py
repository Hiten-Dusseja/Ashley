import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
import pyjokes
import pywhatkit
from email.message import EmailMessage
import time
import pyautogui
import keyboard as k
from datetime import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def set_gender(n=1):
    engine.setProperty('voice', voices[n].id)


message_recipient_dict = {'hello': "+919881010419", 'personal': '+917262994270',
                          'jack': '+917051522003', 'max': '+919867240151', 'pablo': '+919867240151'}


def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()


def sendmesage(phnnumber, message_sent):
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    hour = int(current_time[:2])
    minu = int(current_time[3:5])
    print("Current Time =", hour, " ", minu)
    if(minu == 59 or minu == 60):
        minu = 0
        hour = hour + 1
    else:
        minu = minu+1
    print("Time after 1 min =", hour, " ", minu)
    pywhatkit.sendwhatmsg(phnnumber, message_sent, hour, minu)
    pyautogui.click(1050, 950)
    time.sleep(1)
    k.press_and_release('enter')


def greetme():
    speak("Hello there This is Ashley,how can I help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.9
        r.phrase_threshold = 0.4
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        query = query.lower()
        if 'exit ashley' in query:
            speak("Exiting Ashley")
            exit()
        else:
            query = query.replace("ashley", "")

    except Exception as e:
        print("Couldn't recognize that, can you please repeat")
        speak("Couldn't recognize that, can you please repeat")
        return "none"
    return query


def dowork():
    greetme()
    if True:
        query = takeCommand().lower()
        if 'who is' in query:
            try:
                print("Searching....wait")
                query = query.replace("wikipedia", "")
                query = query.replace("according to", "")
                query = query.replace("who is", "")
                query = query.replace("what is", "")
                results = wikipedia.summary(query, sentences=1)
                speak("So wikipedia says  ")
                print(results)
                speak(results)
            except Exception as e:
                speak("Couldn't find that, sorry!")
                print("Couldn't find that")

        elif 'open browser' in query:
            browserpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome")
            print("Opening chrome..")
            os.startfile(browserpath)

        elif 'open instagram' in query:
            speak("opening instagram")
            print("Opening instagram...")
            webbrowser.open('instagram.com')

        elif 'open youtube' in query:
            speak("starting youtube")
            print("Opening youtube...")
            webbrowser.open('youtube.com')

        elif 'open github' in query:
            speak("opening github")
            print("Opening github..")
            webbrowser.open('github.com')

        elif 'open google' in query:
            speak("opening google")
            print("Opening google...")
            webbrowser.open('google.com')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif 'play' in query:
            if 'play music' in query:
                print("Playing music...")
                speak("Playing music")
                music_dir = "D:\\College Docs\\Microproject\\music"
                songslist = os.listdir(music_dir)
                songlistlen = len(songslist) - 1
                r = random.randint(0, songlistlen)
                os.startfile(os.path.join(music_dir, songslist[r]))

            elif 'play songs' in query:
                print("Playing music...")
                speak("playing music")
                music_dir = "D:\\College Docs\\Microproject\\music"
                songslist = os.listdir(music_dir)
                songlistlen = len(songslist) - 1
                r = random.randint(0, songlistlen)
                os.startfile(os.path.join(music_dir, songslist[r]))

            else:
                query = query.replace("play", "")
                speak(f"Playing {query}")
                print(f"Playing {query}")
                pywhatkit.playonyt(query)

        elif 'current time' in query:
            crnttime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {crnttime}")
            print(f"The current time is {crnttime}")

        elif 'open torrent' in query:
            tpath = "C:\\Users\\Komal\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            speak("Opening torrent")
            os.startfile(tpath)

        elif 'search' in query:
            query = query.replace("search", "")
            query = query.replace("about", "")
            query = query.replace("for", "")
            speak(f"searching {query}")
            pywhatkit.search(query)

        elif 'message' in query:
            message_tobe_sent = 'none'
            recipient = 'none'
            while(message_tobe_sent == 'none'):
                speak("What should be the message?")
                message_tobe_sent = takeCommand()
            while(recipient == 'none'):

                speak("Who should I send the message to?")
                recipient_key = takeCommand()
                try:
                    recipient = message_recipient_dict[recipient_key]
                except Exception as e:
                    print(e)
                    recipient = 'none'
                if(recipient == 'none'):
                    print("Can't find that person, please try again")
            try:
                sendmesage(recipient, message_tobe_sent)
            except Exception as e:
                print(e)

        else:
            if query != 'none':
                speak("I am not able to do that, sorry!")
            else:
                dowork()
