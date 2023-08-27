import datetime
import os
import webbrowser
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
from playsound import playsound

print("Mind Starting up")

#playsound('Starting1.wav')
#playsound('Starting2.wav')
#playsound('Starting3.wav')
#playsound('Starting4.wav')
#playsound('Starting5.wav')
#playsound('Starting6.wav')

url = 'https://www.bbc.com/news'
news = requests.get(url)

soup = BeautifulSoup(news.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'glados' in command:
                command = command.replace('glados', '')

    except:
        pass
    return command


def run_glados():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        playsound('GetForU.wav')
        talk(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        playsound('DoingTask1.wav')
        talk(time)
    elif 'search' in command:
        lookup = command.replace('search', '')
        info = wikipedia.summary(lookup, 1)
        playsound('DoingTask2.wav')
        print(info)
        talk(info)
    elif 'good morning' in command:
            import time
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(time)
            webbrowser.open_new_tab(
                'https://www.youtube.com/watch?v=YyV2k8Almuk&list=PLfFBZBQAEaXlRsly8vkC11rVKWGkjYY-c&index=7&ab_channel=PizzaMusic')
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=tXWh-dowiLg&list=PLfFBZBQAEaXk2iw4dxx4PKNzdPfqfGCj1")
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            for x in list(dict.fromkeys(headlines)):
                if x.text.strip() not in unwanted:
                    talk(x.text.strip())
    elif 'close browser' in command:
        os.system("taskkill /im chrome.exe /f")
    elif 'movies and shows' in command:
        playsound('GetForU.wav')
        webbrowser.open_new_tab('https://kisscartoon.xyz/')
    elif 'spotify' in command:
        playsound('DoingTask1.wav')
        playsound('DoingTask2.wav')
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=YyV2k8Almuk&list=PLfFBZBQAEaXlRsly8vkC11rVKWGkjYY-c&index=7&ab_channel=PizzaMusic')
    else:
        talk(' ')


while True:
    try:
        run_glados()
    except UnboundLocalError:
        print("no command given")
        command = "."

