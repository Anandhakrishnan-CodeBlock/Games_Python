from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot('kern')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")

while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Kern: ', response)