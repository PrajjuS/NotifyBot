import os
import logging
from dotenv import load_dotenv
from distutils.util import strtobool as sb
from pyrogram import Client

log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    format='[%(asctime)s - %(levelname)s] - %(name)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[logging.FileHandler(f'{__name__}.log'), logging.StreamHandler()],
    level=log_level
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOG = logging.getLogger(__name__)

load_dotenv("config.env")

def getConfig(config_name):
    return os.environ[config_name]
try:
    API_ID = getConfig("API_ID")
    API_HASH = getConfig("API_HASH")
    TG_SESSION = getConfig("TG_SESSION")
    BOT_TOKEN = getConfig("BOT_TOKEN")
    CHAT_ID = {int(x) for x in getConfig("CHAT_ID").split(" ")}
    ENABLE_TAG = sb(getConfig("ENABLE_TAG"))
except KeyError:
    print(f"Fill all the configs plox...\nExiting")
    exit(0)

SECURITY_CHAT = -1001409015783
FINGERPRINT_CHAT = -1001395287785

ubot = Client(
    plugins=dict(root=f"{__name__}/modules"),
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=TG_SESSION,
    parse_mode='html'
)

bot = Client(
    ":memory:",
    plugins=dict(root=f"{__name__}/modules"),
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode='html'
)