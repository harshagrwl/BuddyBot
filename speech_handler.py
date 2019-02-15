import pyttsx3

BuddyBot = pyttsx3.init()

sound = BuddyBot.getProperty('voices')

BuddyBot.setProperty('rate',170)
BuddyBot.setProperty('volume',10)
