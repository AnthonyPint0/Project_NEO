import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("   ")

def GoogleSearch(term):
    query = term.replace("neo","")
    query = query.replace("what is","")
    query = query.replace("what is ","")
    query = query.replace("how to","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    opn = open("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\Text-Features\\Data.txt","a")
    opn.write(writeab)
    opn.close()
    
    Query = str(term)
    pywhatkit.search(Query)
    os.startfile("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\ExtraPro\\start.py")

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_result=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Main.Speak(how_to_func[0].summary)

    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query,2)
        Main.Speak(f": According to the Internet : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    Speak('This is what I found for your search')

    pywhatkit.playonyt(term)

    Speak('This may also help you')

def Alarm(query):

    TimeHere=  open('C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\Text-Features\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\YouTube Downloads\\')


    Download(Link)


    Speak("Done , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\YouTube Downloads\\')

def SpeedTest():

    os.startfile("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\Gui_Programs\\SpeedTestGui.py")

def WolfRam(query):

    
    api_key = '8WYQU6-4266QYW68L'

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer

    except:
        Speak("No Data Found.") 

def Calculator(query):

    Term = str(query)
    Term = Term.replace("neo","")
    Term = Term.replace("multiplied","*")
    Term = Term.replace("add","+")
    Term = Term.replace("substract","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divided","/")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Final = str(Term)

    try:
        result = WolfRam(Final)
        Speak(f"{result}")

    except:
        Speak("No Data Found.")    

def Temp(query):

    Term = str(query)

    Term = Term.replace("neo ","")
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature ","")
    Term = Term.replace("in ","")

    temp_query = str(Term)

    if 'outside' in temp_query:

        var1 = "temperature in Bengaluru"
        
        answer = WolfRam(var1)

        Speak(f"{var1} is {answer}")

    else:

        var2 = "temperature in " + temp_query

        ans = WolfRam(var2)

        Speak(f"{var2} is {ans}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)







    




