import pyttsx3
texttospecch = pyttsx3.init()
speech = input ("type in a word: ")
texttospecch.say(speech)
texttospecch.runAndWait()
# txtenv