""""
install the module (pip install pyttsx3)
"""
import pyttsx3
friend = pyttsx3.init()
speech = raw_input("Type Something:")
friend.say(speech)
friend.runAndWait()

