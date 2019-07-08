
# pip3 install SpeechRecognition


import speech_recognition as sr
import os

r=sr.Recognizer()



def initSpeech():
    command = ""
    os.system("say What application you want to open")
    print("Listening...")

    with sr.Microphone() as source:
        audio = r.listen(source)

    print("...")

    try:
        command = r.recognize_google(audio)
    except:
        print("Can't reach google at the moment. Try again later!")

    return command



def commander(text):


    if "open" in text:
        app_name = text.split(" ",1)[-1]
        print(app_name)
        app_name = app_name.lower()
        os.system("say  Opening  " +app_name)
        return_value =  os.system(""+app_name)
        if return_value  != 0:
            os.system("say Application Not Found!")

        print(return_value)

    else:
        app_name = text
        print(app_name)
        app_name = app_name.lower()
        os.system("say  Opening  " + app_name)
        return_value = os.system("" + app_name)
        if return_value == 1:
            os.system("say Application Not Found!")

name = initSpeech()
commander(name)
