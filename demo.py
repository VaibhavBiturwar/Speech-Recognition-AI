import wave
import pyaudio
import speech_recognition as sr

import os


def ossay(text):
    os.system("say "+text)
    #print("Voice: "+"say "+text)



def play_audio(filename):
    chunk =1024
    wf = wave.open(filename , "rb")
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()




r = sr.Recognizer()

def initSpeech():
    play_audio("./audio/Bass-Drum-1.wav")
    command = "Nothing Recevied"
    print("Listening.....")

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio("./audio/Bass-Drum-1.wav")

    try:
        command = r.recognize_google(audio)
    except:
        print("Error Occurred")

    print(f"Your command :{command}")
    ossay("You Said  "+command)

initSpeech()

