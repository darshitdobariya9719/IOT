from twilio.rest import Client
from geopy import Nominatim
import geocoder
import os
import time
#from gtts import gTTS
import speech_recognition as s
from espeak import espeak
import pyttsx3
import pygame
from playsound import playsound
#engine = pyttsx3.init()
#engine.say("I will speak this text")
#engine.runAndWait()
#at=gTTS('hello how are you  ',lang='en',slow=True)
#at.save('wel.mp3')
def speech():
    os.system('vlc auth.mp3 &')
    time.sleep(6)
    
    #engine = pyttsx3.init()
    #engine.say("I will speak this text")
    #engine.runAndWait()
    #espeak.synth("su tame barabar cho!")
    #espeak.s
    #time.sleep(4)
    #engine.stop()
speech()
g=geocoder.ip('me')
late=str(g.lat)
lang=str(g.lng)
print(late)
print(lang)
#time.sleep(2)
#late=str(53.2734)
#lang=str(-7.77832031)
locar=late+','+lang
geolocator=Nominatim(user_agent='test/1')
location=geolocator.reverse(locar)
location.address
From_number='+917818030388'
To_number='+919512545434'
client=Client("AC88b70ba7628a21c83604365e5d77bc28","6b75b6982c68e52ed0900d10fd8d1acb")
dar=location.address
dar=dar.replace('Gita','Geeta')
#dar='geeta mandeer vrundavan park madhav mall'
darshit='<Response><Gather timeout="30" action="darshit2"><Play>https://voicedot.000webhostapp.com/Voicecall1.mp3</Play><Say voice="Polly.Raveena"><prosody rate="x-slow" volume="x-loud">'+dar+'</prosody></Say><Play>https://voicedot.000webhostapp.com/Voicecall2.mp3</Play></Gather><Gather finishOnKey="#"><Say voice="Polly.Raveena"><prosody rate="x-slow" volume="x-loud">'+dar+'</prosody></Say></Gather></Response>'
darshit1=darshit
print(darshit1)
call=client.calls.create(twiml=darshit1,to=To_number,from_=From_number,method='GET')
print(call.sid)

                 