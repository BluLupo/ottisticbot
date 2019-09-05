import config
from utils import decorator

@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False
    )