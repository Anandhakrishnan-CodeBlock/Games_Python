from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('kern')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")


#for _file in os.listdir('english'):
#    chat = open(_file, 'r').readline()
#    trainer.train(chat)

while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Kern: ', response)