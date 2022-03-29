from NotifyBot import ubot, bot, LOG
from pyrogram import idle

if __name__ == "__main__":
    ubot.start()
    bot.start()
    LOG.info("NotifyBot Started!")
    idle()
    ubot.stop()
    bot.stop()