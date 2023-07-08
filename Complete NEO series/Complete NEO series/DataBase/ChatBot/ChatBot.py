import random
import speech_recognition as sr
import pyttsx3

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


Hello = ('hello','hey','neo','hi')

reply_Hello = ('Hello , I Am Neo .',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello , Nice To Meet You Again .",
            "Of Course , Hello .")

Bye = ('bye','exit','sleep','go')

reply_bye = ("It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how are you','are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ['functions','abilities','what can you do','features','what are your features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")

def ChatterBot(Text):

    Text = str(Text)

    for word in Text.split():

        if word in Hello:

            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_bye)

            return reply

        elif word in How_Are_You:

            reply_ = random.choice(reply_how)

            return reply_

        elif word in Functions:

            reply___ = random.choice(reply_Functions)

            return reply___

        else:

            return random.choice(sorry_reply)

value = ChatterBot('hello')
Speak(value)
print(value)
