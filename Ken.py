import pyttsx3
import openai
import datetime
import speech_recognition as sr
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Yo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Evening...")
    speak("I'm Ken... how you doin'!? Want help with something...!?")


def takeCommmand():
    # takes microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return query


def chattohbottoh_dattebayo(query):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
    print(response.choices[0].message.content)
    speak(response.choices[0].message.content)


if __name__ == "__main__":
    Yo()
    # speak("It's more fun to chase than be chased.. that's why young girls grow up to be adults falling in love with love...")
    
    while True:
        query = takeCommmand().lower()
    
        # logic for xecuting tasks based on query 
        
        if "open one piece" in query:
            webbrowser.open("https://sanji.to/one-piece-100")

        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "google" in query:
            webbrowser.open("https://www.google.com/")

        elif 'chat gpt' in query:
            openai.api_key = "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"
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input('Ask ur questions: ')}])
            print(completion.choices[0].message.content)
            speak(completion.choices[0].message.content)

        elif "spotify" in query:
            webbrowser.open("https://open.spotify.com/")
            PathToMusic = "C:\\Users\\Buri Buri\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify"
            os.startfile(PathToMusic)

        elif "linkedin" in query:
            webbrowser.open("https://in.linkedin.com/")
            
        # elif "play music" in query:
        #     music_dir = "D:\bleh.."
        #     songs = os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif "whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "telegram" in query:
            webbrowser.open("https://web.telegram.org/a/")

        elif "open ai" in query:
            webbrowser.open("https://openai.com/")

        elif "quit" in query:
            exit()

        else:
            chattohbottoh_dattebayo(query)