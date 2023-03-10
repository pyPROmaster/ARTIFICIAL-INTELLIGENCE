from tkinter import *
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from time import *
import pyautogui

print('DYNAMIX SYSTEMS / TERMINATOR ...')
sleep(0.5)
print('welcome to DYNAMIX TERMINATOR / TERMINATOR AI')
sleep(0.5)
print('Started TERMINATOR sys / Dynamix')
print()

engine = pyttsx3.init()

def speak(what_to_speak) :

    engine.say(what_to_speak)
    engine.runAndWait()

def wishme() :

    hour = (datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12 :

        speak('good morning sir')

    elif hour >=12 and hour <= 18 :

        speak('good afternoon sir')

    else :

        speak('good evening sir')

    speak('i am TERMINATOR')

def take_command () :

    r = sr.Recognizer()

    with sr.Microphone() as source :

        print('listening ...')
        audio = r.listen(source)

        try :

            cmd = r.recognize_google(audio)
            print('you said : {}'.format(cmd))

        except Exception as e :

            speak('please speak again')
            print('please speak again')

            return 'None'

        return cmd

if __name__ == '__main__' :

    wishme()

    while True :

        cmd = take_command().lower()

        if 'open notepad' in cmd :

            speak('opening notepad')
            webbrowser.open('notepad.exe')

        elif 'open paint' in cmd :

            speak('opening paint')
            webbrowser.open('mspaint.exe')

        elif 'command' in cmd :

            speak('opening command prompt')
            webbrowser('cmd.exe')

        elif 'open youtube' in cmd :

            speak('opening youtube')
            webbrowser.open('https://youtube.com/')

        elif 'open chrome' in cmd :

            speak('opening chrome')
            webbrowser.open('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')

        elif 'open zoom' in cmd :

            speak('opening zoom')
            webbrowser.open('C:\\Users\\ss\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

        elif 'who are you' in cmd :

            speak('i am terminator, an AI built by HARSH to operate on devices and controllation of multiple functioners')

        elif 'matrix' in cmd :

            speak('matrix , on')

            webbrowser.open('cmd.exe')

            sleep(2)

            pyautogui.write('color a')

            sleep(0.5)

            pyautogui.press('Enter')

            sleep(0.5)

            pyautogui.write('dir/s')

            sleep(0.5)

            pyautogui.press('Enter')

        elif 'destroy code' in cmd :

            speak('initiating destroy code sequence in 5 seconds')
            print('initiating destroy code sequence in 5 seconds')

            sleep(5)

            pyautogui.hotkey('Ctrl' , 'a')

            sleep(0.5)

            pyautogui.press('Backspace')

            speak('code sucessfully destroyed')
            print('code sucessfully destroyed')

        elif 'recover code' in cmd :

            speak('recovering code in 5 seconds')
            print('recovering code in 5 seconds')

            sleep(5)

            pyautogui.hotkey('Ctrl' , 'z')

            speak('code sucessfully recovered')
            print('code sucessfully recovered')

        elif 'open code' in cmd :

            speak('opening visual studio code')
            webbrowser.open('C:\\Users\\ss\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif 'open nasa' in cmd :

            speak('opening nasa')
            webbrowser.open('www.nasa.gov.in')

        elif 'generate ai' in cmd :

            def wait() :

                sleep(0.5)

            def enter() :

                pyautogui.press('Enter')

            def write(what_to_write) :

                pyautogui.write(what_to_write)

            speak('generating code to create ai in 5 seconds')
            print('generating code to create AI in 5 seconds')

            sleep(5)

            write('from time import *')

            wait()
            enter()
            wait()

            write('import speech_recognition as sr')

            wait()
            enter()
            wait()

            write('import pyttsx3')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('import webbrowser as web')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('def speak(what_to_say) :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('engine = pyttsx3.init()')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('engine.say(what_to_say)')

            wait()
            enter()
            wait()

            write('engine.runAndWait()')

            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace') 

            wait()
            
            write('def wishme () :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write("speak('welcome sir, i am terminator')")

            wait()
            enter()
            wait()
            enter()
            wait()
            pyautogui.press('Backspace')

            wait()

            write('def take_command () :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('r = sr.Recognizer()')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('with sr.Microphone() as source :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write("print('listening ...')")

            wait()
            enter()
            wait()

            write("audio = r.listen(source)")

            wait()
            enter()
            wait()
            enter()
            wait()

            write('try :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write('cmd = r.recognize_google(audio)')

            wait()
            enter()
            wait()

            write("print('you said : {}'.format(cmd))")

            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace')

            wait()

            write('except Exception as e :')

            wait()
            enter()
            wait()
            enter()
            wait()

            write("speak('please speak again')")
            
            wait()
            enter()
            wait()

            write("print('please speak again')")

            wait()
            enter()
            wait()
            enter()
            wait()

            write("return 'None'")

            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace')

            wait()

            write('return cmd')

            wait()
            enter()
            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace')

            wait()

            pyautogui.press('Backspace')

            wait()

            write("if __name__ == '__main__' :")

            wait()
            enter()
            wait()
            enter()
            wait()

            write("wishme()")

            wait()
            enter()
            wait()
            enter()
            wait()

            write("while True :")

            wait()
            enter()
            wait()
            enter()
            wait()

            write('cmd = take_command().lower()')

            wait()
            enter()
            wait()
            enter()
            wait()

            write("if 'open notepad' in cmd :")

            wait()
            enter()
            wait()

            write("speak('opening notepad')")

            wait()
            enter()
            wait()

            write("web.open('notepad.exe')")

            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace')

            wait()

            write("elif 'open command' in cmd :")

            wait()
            enter()
            wait()

            write("speak('opening command prompt')")
            
            wait()
            enter()
            wait()

            write("web.open('cmd.exe')")

            wait()
            enter()
            wait()
            enter()
            wait()

            pyautogui.press('Backspace')

            wait()

            write("elif 'terminate' in cmd :")

            wait()
            enter()
            wait()

            write("speak('terminating terminator')")

            wait()
            enter()
            wait()
            enter()
            wait()

            write('break')

            speak('code successfully written')
            print('code successfully written')

        elif 'open cad' in cmd :

            speak('opening Fuison 360')
            webbrowser.open('C:\\Users\\ss\\AppData\\Local\\Autodesk\\webdeploy\\production\\6a0c9611291d45bb9226980209917c3d\\FusionLauncher.exe')
   
        elif 'terminate' in cmd :

            speak('terminating TERMINATOR')
            
            break