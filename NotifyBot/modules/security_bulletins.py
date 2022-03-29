from NotifyBot import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@ubot.on_message(filters.chat(SECURITY_CHAT) & filters.incoming, group=1)
async def security_check(client, message):
    check_text = "security"
    text = message.text
    if text:
        check = text.lower().find(check_text)
        if check != -1:
            LOG.info("New Security Patch detected!")
            for i in message.entities:
                URL = i.url
            CUT = text.split("\n")
            MSG = CUT[0]
            PATCH = CUT[1]
            DATE_FROM = CUT[3]
            DATE_TO = CUT[4]
            content =  ""
            content += f"\n<b>{MSG}</b>\n"
            content += f"<b>Patch:</b> \n<code>{DATE_FROM}\n{DATE_TO}</code>\n"
            BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton(text=f"{PATCH}", url=URL)]])
            LOG.info(f"Notifying in the following chats: {CHAT_ID}")
            for chats in CHAT_ID:
                msg = await bot.send_message(chat_id=chats, text=content, reply_markup=BUTTON)
                LOG.info(f"Successfully notified in the chat: {chats}")
                try:
                    await bot.pin_chat_message(chat_id=chats, message_id=msg.message_id)
                    LOG.info(f"Successfully pinned message in the chat: {chats}")
                except Exception:
                    LOG.info(f"Not enough rights to pin message in the chat: {chats}")
                if ENABLE_TAG:
                    tag = ""
                    members = bot.iter_chat_members(chat_id=chats, filter="administrators")
                    async for member in members:
                        username = member.user.username or None
                        if username:
                            if not member.user.is_bot:
                                tag += f"@{username}\n"
                        else:
                            pass
                    await bot.send_message(chat_id=chats, text=tag, reply_to_message_id=msg.message_id)
                    LOG.info(f"Successfully tagged admins in the chat: {chats}")
                else:
                    pass
