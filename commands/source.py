from utils import decorator
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="<b>     OtterBot</b>\n"
                                          "====================\n\n"
                                          "<b>Language:</b> <em>Python</em>\n\n"
                                          "<b>Version</b>:<em> v.8.0 - Hoatzin</em>\n\n"
                                          "<b>Developer</b>:<em>Hersel Giannella</em>\n\n"
                                            "<b>Based on</b>:<a href=\"https://github.com/hersel91/ottisticbot\"> GitHub</a>\n\n"
                                          "<b>Website</b>:  <a href=\"https://hersel.it\">hersel.it</a> ", parse_mode = 'HTML')