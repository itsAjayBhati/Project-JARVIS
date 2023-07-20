
import pyttsx3                         # pip install pyttsx3
import datetime                        # Built in moudule
import speech_recognition as sr        # pip install speechRecognition
import wikipedia                       # pip install wikipedia
import webbrowser                      # Built in module
import os                              # Built in moudule
import smtplib                         # Built in

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!!, Har Har Mahadex")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
        
    speak("I am Jarvis Sir. Please Tell me how may I help you")
        
def takeCommand():
    # It takes Microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again plese...")
        return "None"
    return query
        
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password-here")
    server.sendmail("youremail@gmail.com", to , content)
    server.close()
    
        
    
        
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
        # Logic for Executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "play music" in query:
            music_dir = "F:\\Python\\Harry Brother\\Python Projects CWH\\Project Jarvis\\Favsongs"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            
        elif "open code" in query:
            codePath = "C:\\Users\\ajayb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)        
            
        elif "email to ajay" in query:
            try:
                speak("What shoud i say")
                content = takeCommand()
                to = "jaibhervnath@yahoo.com"
                sendEmail(to,content)
                speak ("Email Has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send able to send this email")
        
        elif "quit" in query:
            speak("Ok sir i will see you very soon")
            exit()