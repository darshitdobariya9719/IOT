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
you=''
doc=['haa','yes I am okay','yes I am','yes','okay','I am okay','I am','Done']
mic = s.Microphone(device_index=1,chunk_size=8192, sample_rate=44100)
pi_ear=s.Recognizer()
with mic as source:
    pi_ear.adjust_for_ambient_noise(source, duration=0.5)
    print("i am lisning")
    audio=pi_ear.listen(source)
    print("done")
    try:
        you=pi_ear.recognize_google(audio,language='eng-in')
        print(you)
    except s as e:
        print(e)
    if you not in doc:
        speech()
        #mic = s.Microphone(device_index=1,chunk_size=8192, sample_rate=44100)
        #pi_ear=s.Recognizer()
        #with mic as source:
        pi_ear.adjust_for_ambient_noise(source, duration=0.5)
        print("i am lisning")
        audio=pi_ear.listen(source)
        print("done")
        try:
            you=pi_ear.recognize_google(audio,language='eng-in')
            print(you)
        except s as e:
            print(e)
        if you not in doc:
            i=1
            if i==1:
                speech()
                #mic = s.Microphone(device_index=1,chunk_size=8192, sample_rate=44100)
                #pi_ear=s.Recognizer()
                #with mic as source:
                if i==1:
                    pi_ear.adjust_for_ambient_noise(source, duration=0.5)
                    print("i am lisning")
                    audio=pi_ear.listen(source)
                    print("done")
                try:
                    you=pi_ear.recognize_google(audio,language='eng-in')
                    print(you)
                except s as e:
                    print(e)
                if you not in doc:
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
