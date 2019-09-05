#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config, commands, dialogs, utils

# Questo abilita i log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    logger.warning('Update "%s" genera errore: "%s"', update, context.error)

# Questa è la funzione che inizializza il bot
def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher

    # Qui "creo" i comandi e assegno una funzione
    dp.add_handler(CommandHandler("start", commands.start.init))
    dp.add_handler(CommandHandler("rules", commands.rules.init))
    dp.add_handler(CommandHandler("bang", commands.ban.init))
    dp.add_handler(CommandHandler("source", commands.source.init))
    dp.add_handler(CommandHandler("io", commands.io.init))
    dp.add_handler(CommandHandler("exit", commands.leave.init))
    dp.add_handler(CommandHandler("ott", commands.otterrandom.init))
    dp.add_handler(CommandHandler("say", commands.say.init))
    dp.add_handler(CommandHandler("mute", commands.muta.init))
    dp.add_handler(CommandHandler("unmute", commands.smuta.init))
    dp.add_handler(CommandHandler("setanswer", commands.insertcustomhandler.init))
    
    # Qui richiamo le funzioni senza comando, =>handler
    dp.add_handler(MessageHandler(None, dialogs.handler.init))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
