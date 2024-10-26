import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Hey I'm alexa
# Kind da dreamy, How can I help you today?
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            # Hey I'm alexa
            # Kind da dreamy, How can I help you today?
            print('Clearing background noise:')
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Waiting for your message...")

            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command  = command.replace('alexa', '')
                print(command)
    except:        
        pass
    return command

def run_alexa():
    command= take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('It is: ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'marry' in command:
        talk('sorry, I am not the marrying type')
    elif 'do you love me' in command:
        talk('There are people I admire,But human love is way off racks')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I am not able to understand you, please repeat..')
        


while True:
    run_alexa()