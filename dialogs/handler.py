import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import decorator
from . import welcome
from . import define
from . import customhandler


#fish
def fish(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("pheesh"):
			bot.send_message(update.message.chat_id, text="PHEESH!!!", parse_mode='HTML')

def hello(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("hello ottistic"):
			bot.send_message(update.message.chat_id, "Beep Boop {username}".format(username=update.message.from_user.first_name))
def buonasera(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("good evening"):
			bot.send_message(update.message.chat_id, "Good evening {username}".format(username=update.message.from_user.first_name))
#Buongiorno
def buongiorno(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("good morning"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampagiorno.webp')
			bot.send_message(update.message.chat_id, "Good morning {username}".format(username=update.message.from_user.first_name))
#Buonanotte
def buonanotte(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("good night"):
			#bot.sendSticker(update.message.chat_id, 'https://furryden.it/immagini/stickerbot/zampanight.webp')
			bot.send_message(update.message.chat_id, "Good night {username}".format(username=update.message.from_user.first_name))

#send nudes
def sendnudes(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("ottistic send nudes"):
			bot.send_photo(update.message.chat_id, 'https://furryden.it/immagini/sendnudes2.png')
#come stai
def comestai(update, context):
	bot = context.bot
	if update.message.text is not None:
		if str(update.message.text).lower().startswith("how are you ottistic?"):
			bot.send_message(update.message.chat_id, "{username} I'm a robot i don't feel nothing".format(username=update.message.from_user.first_name))

#DICHIARAZIONE FUNZIONI
def init(update, context):
	welcome.init(update, context)
	buongiorno(update, context)
	buonanotte(update, context)
	hello(update, context)
	sendnudes(update, context)
	comestai(update, context)
	define.init(update, context)
	buonasera(update, context)
	fish(update, context)
	customhandler.init(update, context)
	


