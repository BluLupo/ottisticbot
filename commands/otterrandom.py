import random
import os
from utils import decorator

@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    directory = "/home/admin/pythonserver/otterbot/img/"
    random_image = random.choice(os.listdir(directory))
    bot.send_photo(update.message.chat_id, photo=open(directory + random_image,'rb'))