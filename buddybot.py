from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_handler as speech
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

bot = ChatBot('BuddyBot')
trainer = ListTrainer(bot)

#BuddyBot = pyttsx3.init()
for files in os.listdir ('./chatterbot_corpus/data/english/'):
    data = open ('./chatterbot_corpus/data/english/' +files, 'r').readlines()
    trainer.train(data)

name = input("Buddy: What is your name?\n")
while True:
    message = input (name + ':')
    if message.strip() != 'Bye':
     reply = bot.get_response(message)
     speech.BuddyBot.say(reply)
     print('Buddy:',reply)
     speech.BuddyBot.runAndWait()

    if message.strip() == ('Bye'):
     speech.BuddyBot.say("Bye! Had a great time interacting with you")
     print('Buddy: Bye! Had a great time interacting with you :)')
     speech.BuddyBot.runAndWait()
     break



