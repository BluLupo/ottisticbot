from utils import decorator
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text='Here the rules of Otter Space:\n- be an ott\n- be over 18\n- be nice\n- no shapeshifter\n- no drama\n- no flood\n- no scat\n- no irl nswf without admin consent\n- have fun', parse_mode='HTML')