import pyttsx3

engine = pyttsx3.init()

text = "Hello! i am a btech student."

engine.say(text)
engine.runAndWait()