from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ

SESSION_NAME = "PunyaChael"
DB_NAME = "db.sqlite3"
API_ID = 123456
API_HASH = "abcd12345"
ARQ_API_URL = "https://arq.hamker.in"

if exists("config.py"):
    from config import *
else:
    from sample_config import *

session = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

conn = connect(DB_NAME)

PunyaChael = Client(
    SESSION_NAME,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)
with PunyaChael:
    bot = PunyaChael.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username
