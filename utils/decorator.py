#DEFINIZIONE COMANDI ADMIN
from functools import wraps


LIST_OF_ADMINS = [63346884,605363037,285558712,587595490]

def restricted(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped

#CANCELLA COMANDI
def cancellacomandi(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(update, context)
    return wrapped
#OWNERBOT
OWNER_LIST= [605363037]

def ownerbot(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped