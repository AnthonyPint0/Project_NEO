import pyttsx3
from gtts import gTTS
from win10toast import ToastNotifier
import speech_recognition as sr
from Features import GoogleSearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening......")
        r.pause_treshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f': Your Command : {query}\n')

    except:
        return ""
    return query.lower()

toast = ToastNotifier()
toast.show_toast(" Neo ","Neo Is Now Active",duration=3)

def TaskExe():

    while True:

        query = TakeCommand()

        if 'google search' in query:

            GoogleSearch(query)

        elif 'youtube search' in query:

            Query = query.replace("neo","")

            query = Query.replace("youtube search","")

            from Features import YouTubeSearch

            YouTubeSearch(query)

        elif 'set alarm' in query:

            from Features import Alarm

            Alarm(query)

        elif 'download' in query:

            from Features import DownloadYouTube

            DownloadYouTube()
            
        elif 'speed test' in query:

            from Features import SpeedTest

            SpeedTest()
         
        elif 'temperature' in query:

            from Features import Temp

            Temp(query)

        elif 'calculate' in query:

            from Features import Calculator

            Calculator(query)

        elif 'wolfram' in query:

            from Features import WolfRam

            Result = WolfRam(query)

            Speak(Result) 

        elif 'chrome' in query:

            from Automations import ChromeAuto

            ChromeAuto(query)
    
        elif 'youtube' in query:

            from Automations import YouTubeAuto

            YouTubeAuto(query)

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa_Api import NasaNews

            NasaNews(Value) 

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

TaskExe()





