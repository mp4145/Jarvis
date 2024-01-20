import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #To get the wiki definitions
import smtplib

engine = pyttsx3.init() #engine = pyttsx3.init('dummy') - worked but had no audio output

#Installed py3-tts instead, yet, audio output is not efficient when connected to the TV but works

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

#speak('Hello, world!') #The string here is not converted to speech instead the string within the function is converted

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(str(date))
    speak(str(month))
    speak(str(year)) #Works only when converted to string

def wishme():
    speak("Welcome, Maria!")
    time()
    date()

    #Greeting based on the hour of the day

    hour = datetime.datetime.now().hour

    if hour >= 5 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17: 
        speak("Good Afternoon!")
    elif hour >=17 and hour < 23:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("Test Jarvis at your service. How can I help you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you speak.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-US') #Supported langauges: https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
        print(query)
    
    except Exception as e:
        print(e)
        print('Sorry, I did not get that, please say that again')
        return "None"
    return query

# TakeCommand() - to make this work I installed brew; brew install portaudio, pip install pyaudio, brew install flac 
if __name__ == "__main__":
    
    wishme()

    while True:
        query = TakeCommand().lower() #For easy recognition everything is converted to the lower case
        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        #elif 'wikipedia' or 'definition' or 'mean' in query: not very effective only works well when you say "Python wikipedia" does not work when you ask "What is the Wikipedia definition of python?" for example
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'bye' in query:
            exit()


