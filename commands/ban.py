from utils import decorator
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.kick_chat_member(update.message.chat_id, update.message.reply_to_message.from_user.id)
    bot.send_message(update.message.chat_id, 
    text="*charges a giant light sphere in its mouth then shoots a deadly laser beam on {username} that completely erase the body and soul from the reality*"
    .format(username=update.message.reply_to_message.from_user.first_name), 
    parse_mode='HTML')