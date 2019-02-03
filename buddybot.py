from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('BuddyBot')
trainer = ListTrainer(bot)

for files in os.listdir ('./chatterbot_corpus\data\english/'):
    data = open ('./chatterbot_corpus\data\english/' +files, 'r').readlines()
    trainer.train(data)

while True:
    message = input ('User:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('Buddy:',reply)

    if message.strip() == 'Bye':
        print('Buddy: Bye! Had a great time interacting with you :)')
        break



