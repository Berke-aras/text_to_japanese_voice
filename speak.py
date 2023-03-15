import requests
from playsound import playsound
import os
from deep_translator import (GoogleTranslator)
import time


while True:
    try:
        try:
            os.remove("ses.mp3")
        except:
            os.remove("ses.wav")
    except:
        ("silinecek ses yok")
    translate = input("\nYaz: ")    

    translate = str(translate)


    translated = GoogleTranslator(source='auto', target='ja').translate(text=translate)


    url = 'https://api.tts.quest/v1/voicevox/?text={}&speaker=20'.format(translated)#13-20

    # A get request to the API
    response = requests.get(url)

    res = response.json()
    #print(res)
    
    time.sleep(2)
    from urllib.request import urlretrieve
    try:
        try:
            mfile = res.get("mp3DownloadUrl")
            print(mfile)
            print(type(mfile))
            urlretrieve(mfile, "ses.mp3")
        except:
            mfile = res.get("wavDownloadUrl")
            print(mfile)
            print(type(mfile))
            urlretrieve(mfile, "ses.wav")
    except:
        print("Ses hatası")
        
    try:
        playsound("ses.mp3")
    except:
        print("Ses oynatma hatası")



