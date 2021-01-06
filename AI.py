import speech_recognition as sr
import random
import webbrowser
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("gelsappa")
speak('hello sir')
print('hello sir,this is your assistant , welcomes you')
print('to search something from google just say ')
print('_____ search from google -- or -- search from google_____ ')
print('')
print('to search anything from you tube just say')
print('_____ search in you tube -- or -- search in you tube_____')
print('')
while'bye':

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('')
        print('Listening...........')
        print('')
        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)
            print('you said:{}'.format(text))
            print('')

            if 'Aishwarya marriage' in text:
                print('jarvis-9 dec , it would be awesome')
                speak( '9 dec , it would be awesome')
                print('')
                

            if 'who are you' in text:
                print('jarvis-i am jarvis an AI')
                speak('i am jarvis an AI')
                
            if 'who made you' in text:
                print('jarvis-i am made by yashwardhan')
                speak('i am made by yashwardhan')
            if 'who created you' in text:
                print('jarvis-yashwardhan created me')
                speak('yashwardhan created me')
            if 'by whom you are created' in text:
                print('jarvis-i am created by yashwardhan')
                speak('i am created by yashwardhan')

            if 'hello' in text:
                print(' jarvis - hi , what do you want to know')
                speak('hi , what do you want to know')
            if text=='jarvis':
                print('ya , i am here')
                speak('jarvis-ya , i am here')
            if 'thanks' in text:
                ans5=('never mind','it is my work','no problem','anytime',' i am always there for you','its OK')
                print('jarvis-' + random.choice(ans5))
                speak(random.choice(ans5))
            if 'thank you' in text:
                ans2=('never mind','it is my work','no problem','anytime',' i am always there for you','its OK')
                print('jarvis-' + random.choice(ans2))
                speak(random.choice(ans2))

            if 'what can you do' in text:
                print('jarvis-')
                print('')
                print('i can open and search in several websites like- you tube , google etc')
                speak('i can open and search in several websites like- you tube , google etc')
                print('')
                print('i can chat with you')
                speak('i can chat with you')
                print('')
                print('provide you several information')
                speak('provide you several information')
                print('')
                print('and ofcourse conver your speech to text')
                speak('and ofcourse conver your speech to text')

            if 'bye' in text or 'close yourself' in text or 'met you later' in text:
                print('jarvis-met you later , sir')
                speak('met you later , sir')
                print('')
                speak('press enter to QUIT')
                input()
                break
            
            if 'what is' in text:
                webbrowser.open('https://www.google.com/?#q=' + text)
                speak('this is what that i got from web')
            if 'what do' in text:
                webbrowser.open('https://www.google.com/?#q=' + text)
                speak('this is what i got from web')
            if 'what does' in text:
                text=text.replace('what does','')
                webbrowser.open('https://www.google.com/?#q=' + text)
            if 'open YouTube' in text:
                webbrowser.open('https://www.youtube.com/')
                speak('opening youtube')
            if 'open Google' in text:
                webbrowser.open('https://www.google.com/')
                speak('opening google')
            if 'open WhatsApp' in text:
                webbrowser.open('https://web.whatsapp.com/')
                speak('opening whatsapp')
            if 'open my School website' in text:
                webbrowser.open('https://theshantiniketan.com/dashboard')
                speak('opening your school website')
            if 'open my homework website' in text:
                webbrowser.open('https://www.tiwariacademy.com/ncert-solutions/class-9')
                speak('opening your homework website')
            if 'search from Google' in text:
                text=text.replace('search from Google' , '')
                webbrowser.open('https://www.google.com/?#q=' + text)
                speak('searching')
            if 'search from YouTube' in text:
                text=text.replace('search in YouTube' , '')
                webbrowser.open('https://www.youtube.com/results?search_query='+text)
                speak('searching')

        except:
            'print("hello)'
            
                                
