from conf import conf
from chat import chat

config = conf.Config()
chat.bot.run(config.discord_token)