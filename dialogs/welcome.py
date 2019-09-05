#OTTISTIC WELCOME
def init(update, context):
	bot = context.bot
	for new in update.message.new_chat_members:
		update.message.reply_text("Welcome fellow ott to the Otter Space! this is an exclusive place for otters of all kinds, even hybrids!\nWe provide feesh, puns and protections to our otters.I'm here to protect all otts from ottn´ts ;)")