# -*- coding: utf-8 -*-

import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.enums import ParseMode

# ========== CONFIG ==========
API_ID = 12345678        # your api id
API_HASH = "a0b76b9ff89c3f30adbb2696438c6581"
BOT_TOKEN = "YOUR_BOT_TOKEN"
# ============================

bot = Client(
    "photo_id_generator",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ---------- START ----------
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "📸 <b>Photo ID Generator</b>\n\n"
        "👉 Send me any <b>photo</b>\n"
        "👉 I will give you its <code>file_id</code>",
        parse_mode=ParseMode.HTML
    )

# ---------- PHOTO HANDLER ----------
@bot.on_message(filters.photo)
async def photo_handler(client, message):
    file_id = message.photo.file_id

    await message.reply_text(
        f"✅ <b>PHOTO FILE ID</b>\n\n"
        f"<code>{file_id}</code>",
        parse_mode=ParseMode.HTML
    )

# ---------- WEB SERVER (KEEP ALIVE) ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "Photo ID Generator Bot is running!"

def run_web():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

# ---------- RUN ----------
if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    bot.run()

