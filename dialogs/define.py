import wikipedia as wiki
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import util


def init(update, context):
    if update.message is not None and update.message.text is not None:
        if str(update.message.text).lower().startswith("ottistic define"):
    # Recupero della definizione
            arg = update.message.text[15:]
            wiki.set_lang('en')
            pg = wiki.page(wiki.search(arg)[0])
            title = pg.title
            pg_url = pg.url
            definizione = pg.summary
            button_list = [InlineKeyboardButton("Check on Wikipedia", url=pg_url)]
            reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=1))
            text = "*{}:*\n\n{}".format(title, definizione)
            # Risposta del Bot
            update.message.reply_markdown(text, reply_markup=reply_markup)
            # LOG del bot
            user = update.message.from_user
            messagetime = datetime.strftime(datetime.today(), '%H:%M del %d/%m/%Y')
            print('User: {} con ID: {} '.format(user['username'], user['id'])
                + "Ha appena eseguito il seguente comando: OTTISTIC DEFINISCI alle ore " + messagetime)