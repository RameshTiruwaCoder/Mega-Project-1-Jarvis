import webbrowser
from logging import exception
import speech_recognition as sr
from wikipedia import PageError
import musicLib
import musicLib as songLib
import requests
import random
import wikipedia as wiki
import winsound
import subprocess
import pyjokes as jokes
import datetime
from time import sleep
import pyttsx3

own_intro = "I am Jarvis, an AI assistant created by my master Ramesh"
about_creator = f"This AI assistant jarvis, is created my Ramesh Tiruwa. A python programmer. 15 year old python master."

description = {
    "your_info": own_intro,
    "creator_info": about_creator
}

apps = {
    "google": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "vs code": r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "pycharm": r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.3\bin\pycharm64.exe",
    "sublime text": r"C:\Program Files\Sublime Text 3\sublime_text.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "cmd": r"C:\Windows\System32\cmd.exe",
    "powershell": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
    "calculator": r"C:\Windows\System32\calc.exe",
    "paint": r"C:\Windows\System32\mspaint.exe",
    "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
    "spotify": r"C:\Users\dell\AppData\Roaming\Spotify\Spotify.exe",
    "discord": r"C:\Users\dell\AppData\Local\Discord\app-1.0.9002\Discord.exe",
    "zoom": r"C:\Users\dell\AppData\Roaming\Zoom\bin\Zoom.exe",
    "teams": r"C:\Users\dell\AppData\Local\Microsoft\Teams\Update.exe",
    "telegram": r"C:\Users\dell\AppData\Roaming\Telegram Desktop\Telegram.exe"
}

def beep():
    duration = 200  # milliseconds
    freq = 1000  # Hz
    winsound.Beep(freq, duration)

def get_random_news_title(api_key, query=None):
    url = f"https://newsapi.org/v2/everything?apiKey={api_key}&pageSize=100"
    if query:
        url += f"&q={query}"  # optional keyword filter

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    titles = [article.get("title") for article in articles if article.get("title")]

    if titles:
        return random.choice(titles)
    else:
        return "No news titles found today."

def speak(text):
    """
    Speaks the given Nepali text using pyttsx3.
    Adjusts voice, rate, and volume for clarity.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()

def open_app(app_name):
    app_name = app_name.lower().strip()
    matched_app = None
    for key in apps:
        if app_name in key:  # partial match
            matched_app = apps[key]
            app_name = key
            break

    if matched_app:
        try:
            # Use Windows 'start' command for system apps
            subprocess.Popen(f'start "" "{matched_app}"', shell=True)
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Failed to open {app_name}")
            print(f"Error opening app: {e}")
    else:
        speak(f"Sorry, I don't know how to open {app_name}")

def open_website(link):
    webbrowser.open(link)

def take_command(prompt):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(prompt)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return ""

    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

    except Exception as e:
        print(f"Error: {e}")
        return ""

def command_func(c):
    c = c.lower().strip()

    if "open google" in c:
        speak("Opening Google")
        open_website("https://www.google.com")
        sleep(2)
        speak("Google opened.")

    elif "open youtube" in c:
        speak("Opening YouTube")
        open_website("https://www.youtube.com")
        sleep(2)
        speak("YouTube opened.")

    elif "open facebook" in c:
        speak("Opening Facebook")
        open_website("https://www.facebook.com")
        sleep(2)
        speak("Facebook opened.")

    elif "open instagram" in c:
        speak("Opening Instagram")
        open_website("https://www.instagram.com")
        sleep(2)
        speak("Instagram opened.")

    elif "open twitter" in c or "open x" in c:
        speak("Opening Twitter")
        open_website("https://www.twitter.com")
        sleep(2)
        speak("Twitter opened.")

    elif "open reddit" in c:
        speak("Opening Reddit")
        open_website("https://www.reddit.com")
        sleep(2)
        speak("Reddit opened.")

    elif "open amazon" in c:
        speak("Opening Amazon")
        open_website("https://www.amazon.com")
        sleep(2)
        speak("Amazon opened.")

    elif "open netflix" in c:
        speak("Opening Netflix")
        open_website("https://www.netflix.com")
        sleep(2)
        speak("Netflix opened.")

    elif "open gmail" in c:
        speak("Opening Gmail")
        open_website("https://mail.google.com")
        sleep(2)
        speak("Gmail opened.")

    elif "open wikipedia" in c:
        speak("Opening Wikipedia")
        open_website("https://www.wikipedia.org")
        sleep(2)
        speak("Wikipedia opened.")

    elif("what are you doing" in c):
        speak("I am here to support you and assist you")


    elif c.startswith("play"):
        try:
            song_name = c.split(" ", 1)[1].strip().lower()
            song_lists = list(musicLib.musics.keys())
            if song_name in song_lists:
                song_link = musicLib.musics[song_name]
                speak(f"Playing song {song_name}")
                open_website(song_link)
            else:
                speak("This song is not present at the moment.")
        except IndexError:
            speak("Please specify the song name after 'play'.")

    elif "news" in c:
        random_title = get_random_news_title("9f618a57b73f43a1bee6c690ace53180", query="Nepal")
        speak(random_title)

    elif "who created you" in c:
        message = description["creator_info"]
        speak(message)

    elif "who are you" in c:
        message = description["your_info"]
        speak(message)

    elif "exit" in c:
        exit()

    elif c.startswith("who"):
        main_word = c.split(" ")[2]
        main_word = main_word.capitalize()
        context = wiki.summary(main_word, sentences=4)
        speak(context)

    elif c.startswith("what"):
        try:
            main_word = c.split(" ")[2:]
            main_word = main_word[0].capitalize()
            context = wiki.summary(main_word, sentences=4)
            speak(context)
        except PageError as p:
            print("Page Error")
        else:
            print("Error Occurred")
    elif "joke" in c:
        joke = jokes.get_joke()
        speak(joke)

    elif "search" in c:
        try:
            search_query = c.replace("search", "").strip()
            if search_query:
                speak(f"Searching for {search_query}")
                link = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
                webbrowser.open(link)
            else:
                speak("Please tell me what you want to search.")
        except Exception as e:
            print(f"Search error: {e}")
            speak("Sorry, I couldn’t perform the search.")

    elif "date" in c:
        if "date" in c:
            date = datetime.date.today()
            speak(date.strftime("%B %d, %Y"))
        elif "time" in c:
            time = datetime.datetime.now().time()
            speak(time.strftime("%I:%M"))

    elif any(word in c for word in ["open app", "start app"]):
        for keyword in ["open app", "start app"]:
            if keyword in c:
                app_name = c.replace(keyword, "").strip().lower()
                matched_app = None
                for key in apps:
                    if app_name in key:
                        matched_app = apps[key]
                        app_name = key
                        break
                if matched_app:
                    try:
                        subprocess.Popen(f'start "" "{matched_app}"', shell=True)
                        speak(f"Opening {app_name}")
                    except Exception as e:
                        speak(f"Failed to open {app_name}")
                        print(f"Error opening app: {e}")
                else:
                    speak(f"Sorry, I don't know how to open {app_name}")
                break

    else:
        speak("Sorry, I don't know that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        beep()
        wake_word = take_command("Listening for wake word...")
        if "exit" in wake_word:
            speak("Exiting Jarvis...")
            exit()
        else:
            print(f"Detected: {wake_word}")
            if "jarvis" in wake_word.lower():
                speak("Yes master.")
                icommand = take_command("Listening for command...")
                if icommand:
                    if "exit" in icommand:
                        speak("goodbye.")
                        exit()
                    else:
                        print(f"Command: {icommand}")
                        command_func(icommand)
                else:
                    speak("I did not catch that. Please try again.")
