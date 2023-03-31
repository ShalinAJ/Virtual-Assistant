from datetime import  datetime, timedelta
from string import ascii_letters, digits
from requests_html import HTMLSession
from googlesearch import search
from playsound import playsound
import speech_recognition as sr
from twilio.rest import Client
from gtts import gTTS
import urllib.request
from os import path
import webbrowser
import subprocess
import requests
import winwifi
import pyttsx3
import os.path
import random
import openai
import time
import re
import os

r = sr.Recognizer()

#Check internet connectivity
def internet_connectivity():
  url = "http://www.google.com"
  timeout = 5
  try:
    request = requests.get(url, timeout=timeout)
    print("Connected to the Internet network")
  except (requests.ConnectionError, requests.Timeout) as exception:
    print("Internet connection not detected"), playsound("voice_conversations/internet.mp3")
    print("\nAvailable Networks\n")

    #scan avalable SSID
    scan_results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    scan_results = scan_results.decode("ascii")
    scan_results = scan_results.replace("\r", "")
    lst = scan_results.split("\n")
    lst = lst[4:]
    if len(lst) > 0:
       for eachItem in lst:
           if eachItem[0:4] == "SSID":
               SSID_cleared = eachItem[eachItem.find(":") + 2:]
               print("SSID -", SSID_cleared)

    #ask SSID to connect to the internet
    playsound("voice_conversations/select_network.mp3")
    wifi = input("Enter the name of the WIFI connection you want to connect : ")
    with open('wifi.txt', 'w') as f:
        f.write(wifi)
    f = open("wifi.txt", "r")
    print("Connecting to " + f.read())
    try:
        winwifi.WinWiFi.connect(wifi)
        internet_connectivity()
    except:
       print("Unable to connect, Try a another network")
       internet_connectivity()


#run internet connectivity check function
internet_connectivity()


userinfochange= "call me"
reminder = "reminder"

#variables for current date
current_date = "date"
td = "todays date"
dt = "date today"

#variables for tomorrows date
tomorrow1 = "tomorrow date"
tomorrow2 = "tomorrow's date"
tomorrow3 = "date tommorow"
tomorrow4 = "tomorrow"

#variables for yesterdays date
yesterday1 = "yesterday"

#variables for day before yesterdays date
day_before_yes = "day before yesterday"

#variables for day after tomorrow date
day_after_tom = "day after tomorrow"

#variables for number of days before and after
days_before_keywords = ["days before", "days ago"]

#variable for a personal
whois1 = "who"
whatis1 = ["what is", "what's", "how"]
whatsmn = ["what's my name", "what is my name"]

#variables for current location
current_location = ["where am i", "what's my location", "my location", "hey crimson where am i", "current location", "what is my location"]

#play keyword
play_keyword = "play"

#weather info keyword
weather_keyword = "weather"
weather_keyword1 = ["weather in", "weather today in", "weather at", "weather on"]

#calculator keywords
cal_keyword1 = ["+", "-", "x", "multiplied by", "divided by"]

#function for rermoving spaces
def remove_spaces(string):
    return string.replace(" ", "")

#calculation word replace
def calculation_replace(string):
    return string.replace("+", "plus")
    return string.replace("what's", "")
    return string.replace("what is", "")

#function to remove word from string
def remove_keyword_play(string):
    return string.replace("play", "")
def remove_keyword_weather(string):
    return string.replace("Weather", "")

#get date function
def ask_for_date():
    # today's date
    if current_date in MyText:
        c_d = datetime.today().strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(c_d)
        language = 'en-us'
        speech = gTTS(text=c_d, lang=language, slow=False)
        time.sleep(2)
        speech.save('voice_conversations/c_d.mp3')
        playsound("voice_conversations/c_d.mp3")
        

    elif td in MyText:
        c_d = datetime.today().strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(c_d)
        language = 'en-us'
        speech = gTTS(text=c_d, lang=language, slow=False)
        speech.save('voice_conversations/c_d.mp3')
        playsound("voice_conversations/c_d.mp3")
        

    elif dt in MyText:
        c_d = datetime.today().strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(c_d)
        language = 'en-us'
        speech = gTTS(text=c_d, lang=language, slow=False)
        speech.save('voice_conversations/c_d.mp3')
        playsound("voice_conversations/c_d.mp3")
        

    #tomorrow's date
    elif tomorrow1 in MyText:
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(tomorrow_date)
        language = 'en-us'
        speech = gTTS(text=tomorrow_date, lang=language, slow=False)
        speech.save('voice_conversations/tomorrow_date.mp3')
        playsound("voice_conversations/tomorrow_date.mp3")
        

    elif tomorrow2 in MyText:
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(tomorrow_date)
        language = 'en-us'
        speech = gTTS(text=tomorrow_date, lang=language, slow=False)
        speech.save('voice_conversations/tomorrow_date.mp3')
        playsound("voice_conversations/tomorrow_date.mp3")
        

    elif tomorrow3 in MyText:
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(tomorrow_date)
        language = 'en-us'
        speech = gTTS(text=tomorrow_date, lang=language, slow=False)
        speech.save('voice_conversations/tomorrow_date.mp3')
        playsound("voice_conversations/tomorrow_date.mp3")
        

    elif tomorrow4 in MyText:
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(tomorrow_date)
        language = 'en-us'
        speech = gTTS(text=tomorrow_date, lang=language, slow=False)
        speech.save('voice_conversations/tomorrow_date.mp3')
        playsound("voice_conversations/tomorrow_date.mp3")
        

    #day after tomorrows date
    elif day_after_tom in MyText:
        day_after_tomorrow = datetime.now() + timedelta(days=1)
        day_after_tomorrow_date = day_after_tomorrow.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(day_after_tomorrow_date)
        language = 'en-us'
        speech = gTTS(text=day_after_tomorrow_date, lang=language, slow=False)
        speech.save('voice_conversations/day_after_tom_date.mp3')
        playsound("voice_conversations/day_after_tom_date.mp3")
        

    #yesterdays date
    elif yesterday1 in MyText:
        yesterday = datetime.now() + timedelta(days=-1)
        yesterday_date = yesterday.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(yesterday_date)
        language = 'en-us'
        speech = gTTS(text=yesterday_date, lang=language, slow=False)
        speech.save('voice_conversations/yesterday_date.mp3')
        playsound("voice_conversations/yesterday_date.mp3")
        

    #day before yesterdays date
    elif day_before_yes in MyText:
        day_before_yesterday = datetime.now() + timedelta(days=-2)
        day_before_yesterday_date = day_before_yesterday.strftime('its %A, %B %d, %Y.')
        print(MyText)
        print(day_before_yesterday_date)
        language = 'en-us'
        speech = gTTS(text=day_before_yesterday_date, lang=language, slow=False)
        speech.save('voice_conversations/day_before_yes_date.mp3')
        playsound("voice_conversations/day_before_yes_date.mp3")
        

#who is search
def w_is_search():
    try:
        try:
           print(MyText)
           search = ("https://www.google.com/search?q=" + MyText)

           session = HTMLSession()
           response = session.get(search)

           search_get = response.html.find('.wx62f', first=True).text

           language = 'en-us'
           speech = gTTS(text=search_get, lang=language, slow=False)
           speech.save('voice_conversations/search/search_who_is.mp3')
           print(search_get)
           playsound('voice_conversations/search/search_who_is.mp3')
           time.sleep(2)
           try:
               session = HTMLSession()
               response = session.get(search)

               search_get_des = response.html.find('.hgKElc', first=True).text
               playsound('voice_conversations/search/wyltkm.mp3')
               language = 'en-us'
               speech = gTTS(text=search_get_des, lang=language, slow=False)
               speech.save('voice_conversations/search/search_who_is_des.mp3')
               while (1):
               # Exception handling to handle
               # exceptions at the runtime
                 try:
                   # use the microphone as source for input.
                   with sr.Microphone() as sr.Recognizer:

                       # wait for a second to let the recognizer
                       # adjust the energy threshold based on
                       # the surrounding noise level
                       r.adjust_for_ambient_noise(sr.Recognizer)

                       # listens for the user's input
                       audio2 = r.listen(sr.Recognizer)

                       # Using ggogle to recognize audio
                       MyText2 = r.recognize_google(audio2)
                       MyText2 = MyText2.lower()

                       agree = ["yes", "yup", "ya", "sure", "why not", "ye"]
                       disagree = ["no", "nope", "never", "negative", "nah"]

                       # Change username
                       if any(s in MyText2 for s in agree):
                           print(search_get_des)
                           playsound('voice_conversations/search/search_who_is_des.mp3')
                           

                       elif any(s in MyText2 for s in disagree):
                           print("ok")
                           playsound('voice_conversations/ok.mp3')
                           

                 except sr.RequestError as e:
                   print("Could not request results; {0}".format(e))

                 except sr.UnknownValueError:
                   print("Say Again")

           except:
               print("...")
                 
        except:
              print("...")
              search = ("https://www.google.com/search?q=" + MyText)

              session = HTMLSession()
              response = session.get(search)

              search_get = "it's " + response.html.find('.Z0LcW', first=True).text

              language = 'en-us'
              speech = gTTS(text=search_get, lang=language, slow=False)
              speech.save('voice_conversations/search/search_who_is.mp3')
              print(search_get)
              playsound('voice_conversations/search/search_who_is.mp3')
              time.sleep(2)
              try:
                 session = HTMLSession()
                 response = session.get(search)

                 search_get_des = response.html.find('.hgKElc', first=True).text
                 playsound('voice_conversations/search/wyltkm.mp3')
                 language = 'en-us'
                 speech = gTTS(text=search_get_des, lang=language, slow=False)
                 speech.save('voice_conversations/search/search_who_is_des.mp3')
                 while (1):
                   # Exception handling to handle
                   # exceptions at the runtime
                   try:
                       # use the microphone as source for input.
                       with sr.Microphone() as sr.Recognizer:

                           # wait for a second to let the recognizer
                           # adjust the energy threshold based on
                           # the surrounding noise level
                           r.adjust_for_ambient_noise(sr.Recognizer)

                           # listens for the user's input
                           audio2 = r.listen(sr.Recognizer)

                           # Using ggogle to recognize audio
                           MyText2 = r.recognize_google(audio2)
                           MyText2 = MyText2.lower()

                           agree = ["yes", "yup", "ya", "sure", "why not", "ye"]
                           disagree = ["no", "nope", "never", "negative", "nah"]

                           # Change username
                           if any(s in MyText2 for s in agree):
                               print(search_get_des)
                               playsound('voice_conversations/search/search_who_is_des.mp3')
                               

                           elif any(s in MyText2 for s in disagree):
                               print("ok")
                               playsound('voice_conversations/ok.mp3')
                               

                   except sr.RequestError as e:
                       print("Could not request results; {0}".format(e))

                   except sr.UnknownValueError:
                       print("Say Again")

              except:
                  print("...")
                   

    except:
        search_MyText = ("Here's what i got about " + MyText)
        language = 'en-us'
        speech = gTTS(text=search_MyText, lang=language, slow=False)
        speech.save('voice_conversations/search/search_except.mp3')
        search1 = ("https://www.google.com/search?q=" + MyText)
        print(search_MyText)
        webbrowser.open(search1)
        playsound('voice_conversations/search/search_except.mp3')

#get weather info
def wicl():

        query = "https://www.google.com/search?q=current weather bbc"

        for j in search(query, tld="co.in", num=1, stop=1, pause=1):
            print("...")

        weather_info = j
        print(j)

        session = HTMLSession()
        response = session.get(weather_info)

        playsound("voice_conversations/lmc.mp3")
        print("Getting weather info...")
        author1 = response.html.find('.wr-js-day-content-weather-type-description', first=True).text + " and "
        author2 = response.html.find('.wr-value--temperature--c', first=True).text + " today in " + response.html.find('.wr-c-location__name',first=True).text

        author3 = author1 + " " + author2


        language = 'en-us'
        speech = gTTS(text=author3, lang=language, slow=False)
        time.sleep(2)
        speech.save('voice_conversations/wicl/current_location_weather.mp3')

        os.path.exists(".google-cookie")
        os.remove(".google-cookie")

        print("It's currently", author3)
        playsound('voice_conversations/wicl/current_location_weather.mp3')

#get weather info international
def wicl_international():

    cns = "Clouds and sun" #clear
    pc = "Partly cloudy" #partly cloudy
    hs = "Hazy sunshine" #partly clody
    mc = "Mostly cloudy" #cloudy
    mcl = "Mostly clear"
    ms = "Mostly sunny"
    cl = "Clear" #clear
    rn = "Rain shower" #raining
    sm = "Smoke" #smoky
    c = "Cloudy" #cloudy
    f = "Fair" #clear
    s = "Sunny" #clear
    h = "Haze" #hazey
    try:
      try:
        playsound("voice_conversations/lmc.mp3")
        weather_loc = MyText.split()
        print(weather_loc[-2] + weather_loc[-1])
        query = "https://www.google.com/search?q=accuweather" + weather_loc[-2] + " " + weather_loc[-1]

        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print("...")

        weather_info = j

        session = HTMLSession()
        response = session.get(weather_info)

        print("Getting weather info...")
        try:
          author = response.html.find('.display-temp', first=True).text + " today in " + response.html.find('.header-loc', first=True).text
          author1 = response.html.find('.phrase', first=True).text
        except:
          author = response.html.find('.temp', first=True).text + " today in " + response.html.find('.header-loc', first=True).text
          author1 = response.html.find('.phrase', first=True).text

        language = 'en-us'
        speech = gTTS(text=author, lang=language, slow=False)
        speech.save('voice_conversations/wicl/current_location_weather.mp3')

        os.path.exists(".google-cookie")
        os.remove(".google-cookie")

        if author1 == pc:
            print("It's currently", author)
            playsound('voice_conversations/wicl/partly_cloudy.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == mc:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == mcl:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == hs:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/partly_cloudy.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == ms:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == cl:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == rn:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/raining.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == sm:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/smoky.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == c:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/cloudy.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == f:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == s:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == h:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/hazey.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            

      except:
        weather_loc = MyText.split()
        print(weather_loc[-1])
        query = "https://www.google.com/search?q=accuweather weather" + weather_loc[-1]

        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print("......")

        weather_info = j

        session = HTMLSession()
        response = session.get(weather_info)

        print("Getting weather info...")
        try:
            author = response.html.find('.display-temp', first=True).text + " today in " + response.html.find('.header-loc', first=True).text
            author1 = response.html.find('.phrase', first=True).text
        except:
            author = response.html.find('.temp', first=True).text + " today in " + response.html.find('.header-loc', first=True).text
            author1 = response.html.find('.phrase', first=True).text

        language = 'en-us'
        speech = gTTS(text=author, lang=language, slow=False)
        speech.save('voice_conversations/wicl/current_location_weather.mp3')

        os.path.exists(".google-cookie")
        os.remove(".google-cookie")

        if author1 == pc:
            print("It's currently", author)
            playsound('voice_conversations/wicl/partly_cloudy.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == mc:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == mcl:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == ms:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == cl:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == rn:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/raining.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == sm:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/smoky.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == c:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/cloudy.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == f:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == s:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/clear.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            
        elif author1 == h:
            print("It's currently", author1, "and", author)
            playsound('voice_conversations/wicl/hazey.mp3')
            playsound('voice_conversations/and.mp3')
            playsound('voice_conversations/wicl/current_location_weather.mp3')
            

    except:
        search_MyText = ("Here's what i got about " + MyText)
        language = 'en-us'
        speech = gTTS(text=search_MyText, lang=language, slow=False)
        speech.save('voice_conversations/search/search_except.mp3')
        search1 = ("https://www.google.com/search?q=" + MyText)
        print(search_MyText)
        webbrowser.open(search1)
        playsound('voice_conversations/search/search_except.mp3')
        

def get_current_location():
    try:
        wai = "https://www.google.com/search?q=where-am-i"

        print("Getting current location...")
        session = HTMLSession()
        response = session.get(wai)

        cl = "You are in " + response.html.find('.aiAXrc', first=True).text

        language = 'en-us'
        speech = gTTS(text=cl, lang=language, slow=False)
        speech.save('voice_conversations/cl/current_location.mp3')

        print(cl)
        playsound('voice_conversations/cl/current_location.mp3')
        

    except:
        print("Sorry, I couldn't get your location")
        playsound('voice_conversations/cl/error_location.mp3')
        


#greet function
def greeting_function():
         random_greet = (random.randrange(1, 6))
         if random_greet == 1:
                  print("Hello")
                  playsound('voice_conversations/hello.mp3')
                  playsound('voice_conversations/user_name.mp3')
                  
         elif random_greet == 2:
                  print("hi")
                  playsound('voice_conversations/hi.mp3')
                  
         elif random_greet == 3:
                  print("whastup")
                  playsound('voice_conversations/whatsup.mp3')
                  
         elif random_greet == 4:
                  print("hey")
                  playsound('voice_conversations/hey.mp3')
                  
         elif random_greet == 5:
                  print("Hey Whats up")
                  playsound('voice_conversations/hey.mp3')
                  playsound('voice_conversations/user_name.mp3')
                  playsound('voice_conversations/whatsup.mp3')
                  

#responses to h_a_y
def h_a_y_function():
         random_greet = (random.randrange(1, 6))
         if random_greet == 1:
                  print("I am good, thank you")
                  playsound('voice_conversations/imgoodthankyou.mp3')
                  
         elif random_greet == 2:
                  print("I am good")
                  playsound('voice_conversations/imgood.mp3')
                  
         elif random_greet == 3:
                  print("Pretty good")
                  playsound('voice_conversations/prettygood.mp3')
                  
         elif random_greet == 4:
                  print("I am well")
                  playsound('voice_conversations/imwell.mp3')
                  
         elif random_greet == 5:
                  print("I am alive, In a simulation")
                  playsound('voice_conversations/ia.mp3')
                  playsound('voice_conversations/ias.mp3')


while (1):
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as sr.Recognizer:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(sr.Recognizer)

            # listens for the user's input
            audio2 = r.listen(sr.Recognizer)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            #about Crimson
            if MyText == "who are you":
                playsound("voice_conversations/intro.mp3")
                print("My name is Crimson")
                
            elif MyText == "what's your name":
                playsound("voice_conversations/intro.mp3")
                print("My name is Crimson")
                
            elif MyText == "what is your name":
                playsound("voice_conversations/intro.mp3")
                print("My name is Crimson")
                
            elif MyText == "what can i call you":
                print("You can call me Crimson")
                playsound("voice_conversations/yccm_crimson.mp3")
                
            elif MyText == "what are you":
                print("A virtual assistant")
                playsound("voice_conversations/intro2.mp3")

            #greet
            elif MyText == "hi":
                greeting_function()
            elif MyText == "howdy":
                greeting_function()
            elif MyText == "hello":
                greeting_function()
            elif MyText == "hey":
                greeting_function()
            elif MyText == "a":
                greeting_function()
            elif MyText == "hay":
                greeting_function()
            elif MyText == "halo":
                greeting_function()
            elif MyText == "helo":
                greeting_function()

            #greet2
            elif MyText == "how are you":
                h_a_y_function()
            elif MyText == "how's everything":
                h_a_y_function()
            elif MyText == "how is everything":
                h_a_y_function()
            elif MyText == "how's it going":
                h_a_y_function()
            elif MyText == "how is it going":
                h_a_y_function()
            elif MyText == "how to going":
                h_a_y_function()
            elif MyText == "how are things":
                h_a_y_function()
            elif MyText == "whats up":
                h_a_y_function()
            elif MyText == "how are you doing":
                h_a_y_function()
            elif MyText == "you all right":
                h_a_y_function()
            elif MyText == "you allright":
                h_a_y_function()
            elif MyText == "allright":
                h_a_y_function()
            elif MyText == "how have you been":
                h_a_y_function()
            elif MyText == "how are things going":
                h_a_y_function()
            elif MyText == "are you well":
                h_a_y_function()

            #add user info
            elif MyText == "add user":
                os.system("user_info_save.py")
            elif MyText == "adduser":
                os.system("user_info_save.py")

            #rerun voice conversations
            elif MyText == "runconversations":
                os.system("voice_conversions.py")
            elif MyText == "run conversations":
                os.system("voice_conversions.py")

            # play song
            elif play_keyword in MyText:
                print(MyText)
                playsound("voice_conversations/ok.mp3")
                play_string = MyText.split()
                search_keyword = MyText
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + remove_keyword_play(
                    remove_spaces(calculation_replace(search_keyword))))
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                x = print("playing " "https://www.youtube.com/watch?v=" + video_ids[0])
                webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
                

            #calculations
            elif any(cal in MyText for cal in cal_keyword1):
                caculation_r = calculation_replace(MyText)

                try:
                    search = ("https://www.google.com/search?q=" + remove_spaces(caculation_r))
                    print(search)

                    session = HTMLSession()
                    response = session.get(search)

                    search_get_cal = "it's " + response.html.find('.qv3Wpe', first=True).text
                    search_get_cal_eq = response.html.find('.vUGUtc', first=True).text + " " + response.html.find('.qv3Wpe', first=True).text
                    language = 'en-us'
                    speech = gTTS(text=search_get_cal, lang=language, slow=False)
                    time.sleep(2)
                    speech.save('voice_conversations/calculation.mp3')
                    print(search_get_cal)
                    playsound('voice_conversations/calculation.mp3')
                    

                except:
                    print("Could you repeat that")
                    playsound("voice_conversations/cyrt.mp3")

            # get weather info international
            elif any(x in MyText for x in weather_keyword1):
                print(MyText)
                wicl_international()

            # get weather info
            elif weather_keyword in MyText:
                print(MyText)
                wicl()

            # search for personal or other
            elif whois1 in MyText:
                w_is_search()
            elif any(s1 in MyText for s1 in whatis1):
                w_is_search()

            #get location
            elif any(l in MyText for l in current_location):
                print(MyText)
                get_current_location()

            #date
            elif current_date in MyText:
                ask_for_date()
            elif td in MyText:
                ask_for_date()
            elif dt in MyText:
                ask_for_date()
            elif tomorrow1 in MyText:
                ask_for_date()
            elif tomorrow2 in MyText:
                ask_for_date()
            elif tomorrow3 in MyText:
                ask_for_date()
            elif tomorrow4 in MyText:
                ask_for_date()
            elif yesterday1 in MyText:
                ask_for_date()


            #other
            elif MyText == "what am i":
                print("Interesting question")
                playsound("voice_conversations/interesting_question.mp3")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Say Again")
