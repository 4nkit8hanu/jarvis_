import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Jarvis at your duty sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('User said: ', query)
    except Exception as e:
        print('Please Repeat...')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ankitbhansingh2020@gmail.com', 'bhanu9876')
    server.sendmail('ankitbhansingh.com', to, content)
    server.close()   

email_list = {"manish": "mawatwalmanish1997@gmail.com", "ankit":"mt2102121001@iiti.ac.in", "lekhraj": "lekhrajsaini1403@gmail.com", "santosh": "mt2102121003@iiti.ac.in"}     

if __name__ == '__main__':
    wishMe()
    if 1:
    #while True:
        query =  takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Internet Sir...')
            query = query.replace('Wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia...")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com') 

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')  

        elif 'play music' in query:
            music_dir = 'D:\\Music_bhanu'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) 

        elif 'email to manish' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = email_list("manish")
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry Sir, this email was not sent")            






    
