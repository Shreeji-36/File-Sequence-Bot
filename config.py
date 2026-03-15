import os
from os import environ

TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "7548602942:AAH2ALGFpUMsv4KgeJ_JuEFy3xx9jFOZdzo")
APP_ID = int(os.environ.get("APP_ID", "38528447"))
API_HASH = os.environ.get("API_HASH", "a0b76b9ff89c3f30adbb2696438c6581")
OWNER_ID = int(os.environ.get("OWNER_ID", "7355641270"))
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URI", "mongodb+srv://orewashreeji36_db_user:62rzR9xUC8Qj9UyQ@cluster0.xpqa45v.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Galaxy_Sequence_bot")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Nami_File_Sequence_Bot")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://i.ibb.co/gbywcmVJ/7355641270-28081.jpg")
START_PIC =os.environ.get("START_PIC", "https://i.ibb.co/Nn7sYk5X/7355641270-28079.jpg")
START_MSG = os.environ.get("START_MSG", """<b>Bᴀᴋᴀᴀᴀ...!!!{mention}</b> \n<blockquote><b><i>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs. I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ʏᴏᴜʀ ғɪʟᴇs ᴇᴀsɪʟʏ ɪɴ ᴀ sᴇᴄᴏɴᴅ...!!</i></b></blockquote>\n"""
"<b>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : </b><a href='https://t.me/Prince_Vegeta_36'>𝗖𝗵𝗿𝗼𝗹𝗹𝗼</a>")
ABOUT_TXT = os.environ.get("ABOUT_MESSAGE", "<i><b><blockquote>◈ ғᴏʀ ᴍᴏʀᴇ: <a href=https://t.me/Cosmic_Bots>Cᴏsᴍɪᴄ Bᴏᴛs</a>\n◈ Nᴇᴛᴡᴏʀᴋ: <a href=https://t.me/Galaxy_Networkk>Gᴀʟᴀxʏ Nᴇᴛᴡᴏʀᴋᴋ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Prince_Vegeta_36'>𝗖𝗵𝗿𝗼𝗹𝗹𝗼</a>\n◈ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n◈ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ</a></blockquote></b></i>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "⁉️ Hᴇʟʟᴏ {mention} \n<blockquote expandable><b><i>➪ Iᴀᴍ ᴀ ᴘᴜʙʟɪᴄ ғɪʟᴇ(s) sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇ ғɪʟᴇs ᴀɴᴅ ᴀʟsᴏ I ᴄᴀɴ sᴇɴᴅ ᴛʜᴀᴛ ғɪʟᴇs ɪɴ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ. </i></b></blockquote>")
TG_BOT_WORKERS = 10000
FSUB_LINK_EXPIRY = 300
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003723410492"))
LOG_FILE_NAME = "links-sharingbot.txt"
SEASON_PATTERN = r'[Ss](\d{1,2})'
EPISODE_PATTERN = r'[Ee][Pp]?(\d{1,3})'
QUALITY_PATTERN = r'(480p|720p|1080p|HDRip|2k|4k)'

TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

SORTING_MODES = {
  'Quality': lambda x: (x['quality_order']),
  'All': lambda x: (x['season'], x['episode'], x['quality_order']),
  'Episode': lambda x: (x['episode']),
  'Season': lambda x: (x['season'])
}
QUALITY_ORDER = {
  '480p': 1,
  '720p': 2,
  '1080p': 3,
  'HDRip': 4,
  '2k': 5,
  '4k': 6,
  'unknown': 7
}