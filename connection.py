#!/usr/bin/ python3
import requests
from playsound import playsound
print("checking wifi...")
while True:
    try:
        if requests.get("http://google.com" , timeout = (10,10)).status_code == 200:
            print("wifi connected")
            playsound("wifi.mp3")
            break
        else:
            print("server error")
    except:
        print("not connected")
