


import codecs
import pyttsx3
import speech_recognition as sr
import datetime #to get present time
import wikipedia #to search in wikipedia
import pyaudio
import webbrowser  #for opening websites
import os  #for opening music etc
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Nagaraj. Please tell me How may I help You")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source, duration = 1)
        # r.pause_threshold=1
        # r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print('user said:',query,'\n')
    except Exception as e:
        print(e)
        print("Say that again Please.......")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nagarajullegaddi01@gmail.com','nagaraj@123')
    server.sendmail('nagarajullegaddi01@gmail.com',to,content)
    server.close()

if __name__ == '__main__':

    wishme()
    while True:
    #if 1:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia..")
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "stack overflow" in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")

        elif "open github" in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif "open gmail" in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")

        elif "play music" in query:
            speak("playing music")
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {strTime}")

        elif "open code" in query:
            codepath="C:\\Users\\Nagaraj U\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(codepath)

        elif "send mail" in query:
            try:
                speak("What should i say")
                content=takecommand()
                to="nagarajullegaddi01@gmail.com"
                sendEmail(to,content)
                speak("email has been sent !")
            except Exception as e:
                print(e)
                speak("sorry can't send email to nagaraj")



