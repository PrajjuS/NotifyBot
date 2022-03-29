from NotifyBot import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@ubot.on_message(filters.chat(FINGERPRINT_CHAT) & filters.incoming, group=2)
async def fingerprint_check(client, message):
    check_texts = ["raven:12", "redfin:12"]
    text = message.text
    if text:
        for texts in check_texts:
            check = text.lower().find(texts)
            if check != -1:
                LOG.info("New Fingerprint Update detected!")
                INFO = {}
                URL = {}
                info_index = 0
                url_index = 0
                CUT = text.split("\n")
                for info in CUT:
                    find = info.find(":")
                    INFO[f'{info_index}'] = info[find+1:].replace(" ", "")
                    info_index += 1
                for i in message.entities:
                    URL[f'{url_index}'] = i.url
                    url_index += 1
                COMMIT_URL = URL['1']
                REPO_URL = URL['2']
                BRAND = INFO['0']
                DEVICE = INFO['1']
                VERSION = INFO['2']
                FINGERPRINT = INFO['3']
                content = f""
                content += f"<b>New Fingerprint Update detected!</b>\n"
                content += f"<b>Brand:</b> <code>{BRAND}</code>\n"
                content += f"<b>Device:</b> <code>{DEVICE}</code>\n"
                content += f"<b>Version:</b> <code>{VERSION}</code>\n"
                content += f"<b>Fingerprint:</b> <code>{FINGERPRINT}</code>\n"
                BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="Commit", url=COMMIT_URL), InlineKeyboardButton(text="Repo", url=REPO_URL)]])
                LOG.info(f"Notifying in the following chats: {CHAT_ID}")
                for chats in CHAT_ID:
                    msg = await bot.send_message(chat_id=chats, text=content, reply_markup=BUTTONS)
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
