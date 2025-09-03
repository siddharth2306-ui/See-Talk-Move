
import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # listening duration 40 seconds
        audio = r.listen(source,0,40)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")
        print(query)
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")

    query = str(query).lower()
    return query

text1 = Listen()
print(text1)

def text_to_gcode(text):
    gcode_commands = []
    for char in text:
        if char == 'A':
            gcode_commands.append("G1 X10 Y10")
        elif char == 'B':
            gcode_commands.append("G1 X20 Y20")
        # Add more mappings as needed
    return gcode_commands


gcode = text_to_gcode(text1)
for command in gcode:
   print(command)

