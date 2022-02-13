from  ipaddress import ip_address
from  unittest import result
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import random
from  requests import get
import sys


Listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
      engine.say(text)
      engine.runAndWait()
      

            

def take_command():
  try:
           with sr.Microphone() as source:
               print('Listening.....')
               voice   = Listener.listen(source)
               command = Listener.recognize_google(voice)
               command = command.lower()
               if 'alexa' in command:
                   command = command.replace('alexa', '')
                   print(command)
  except: 
      pass 
  return command

#
def run_alexa():
               command = take_command()
               print(command)

               if 'play ' in command:
                   song = command.replace('play', '')
                   talk('playing  ' + song )
                   pywhatkit.playonyt(song)
               elif 'time' in command: 
                   time =datetime.datetime.now().strftime('%H:%M %p') 
                   talk('current time is '+time)
                   print(time)
                
             
               elif 'wikipedia' in command: 
                   talk("searching wikipedia.......")
                   command = command.replace("wikipedia","")
                   result = wikipedia.summary(command,sentences=2)
                   talk("according to wikipedia")
                   talk(result)
                   print(result)
                     
                   
                   
               elif 'date'   in command:
                   talk ('sorry,   I am not intersting')
               elif  'are you single' in command:
                   talk(' no I am in  a relationship with wifi ')
               elif 'joke' in command:
                   talk(pyjokes.get_joke())
               elif  ' open notepad' in command:
                    npath= "C:\\Windows\\system32\\notepad.exe "
                    os.startfile(npath)
               elif  'open cmd ' in command:
                    os.system("start cmd")
               elif ' music' in command:
                   music_dir ="C:\\Users\\Nabeela\\Desktop\\song"
                   songs =os.listdir(music_dir)
                   talk('playing  ' + music_dir )
                   rd = random.choice(songs)
                   os.startfile(os.path.join(music_dir,rd))
               elif 'ip address' in command:
                    ip = get("https://api.ipfy.ord").text
                    talk(f"your IP address is{ip}")
               
               elif "open youtube" in command:
                    webbrowser.open("www.youtube.com")
               elif "open facbook" in command:
                     webbrowser.open("www.facebook.com") 
               elif "open google" in command:
                   talk("what should i  search on google") 
                   cm = take_command().lower() 
                   webbrowser.open(f"{cm}") 
               elif "send message" in command:
                   pywhatkit.sendwhatmsg("+922192038817","happy birthday",2,50)  

               elif"no thanks" in command:
                   talk("thanks for using me. have a good day.") 
                   sys.exit()

                   
            
               talk("do you have any other work ")

               
                   

while True:             
       run_alexa() 
               