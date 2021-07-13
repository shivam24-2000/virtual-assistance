import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import calendar
import random
import wikipedia


def recordAudio():  # Record audio and return it as a string

    r = sr.Recognizer()   # Records the audio

    with sr.Microphone() as source:    # Uses the microphone and record
        print("Listening!")
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' +data)
    except sr.UnknownValueError:    # Checks for error
        print('Google Speech Recognition could not understand the audio')
    except sr.RequestError as e:     # looks for error due to connectivity issue
        print('Request result from Google Speech Recognition service error ',+e)
    return data

def assistanceResponse(text):
    print(text)

    myobj = gTTS(text=text,lang='en',slow=False )   # Converts text into speech
    myobj.save('assistant_response.mp3')   # Saves audio to file

    os.system('afplay assistant_response.mp3')    # Plays the file

def wakeWords(text):

    WAKEWORDS = ['lucy']
    text = text.lower()

    for phrases in WAKEWORDS:
        if phrases in text:
            return True

    return False

def getdate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    day_Num = now.day

    month_name = ['January','February','March','April','May','June','July','August','September',
                  'October','November','December']
    ordinal_num = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th'
                   '15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th'
                   '28th','29th','30th','31th']

    return 'Today is '+weekday+' '+month_name[monthNum - 1]+' the '+ordinal_num[day_Num - 1]+'.'

def greetings(text):

    greeting_inputs = ['hi','hello','hola','hey','wassup','greetings']
    greeting_response = ['whats good','hello','hey there']

    for words in text.split():
        if words.lower() in greeting_inputs:
            return random.choice(greeting_response)
    return ''

def getperson(text):

    wordList = text.split()

    for i in range(0,len(wordList)):
        if i+3 <= len(wordList)-1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2]+' '+wordList[i+3]


while True:

    text = recordAudio()
    response = ''

    if(wakeWords(text) == True):
        response = response + greetings(text)

        if('date' in text):
            get_date = getdate()
            response = response +' '+ get_date

        if('who is' in text):
            person = getperson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response +' '+wiki

        assistanceResponse(response)