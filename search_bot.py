import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("SEARCH_BOT_TOKEN")
FILE_BOT_USERNAME = os.getenv("FILE_BOT_USERNAME")

app = Client("search_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("search") & filters.private)
async def search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("Please provide a movie name to search.")

    # Simulate a movie found (replace with DB logic)
    fake_file_id = "abc12345"

    url = f"https://t.me/{FILE_BOT_USERNAME}?start={fake_file_id}"
    await message.reply(
        f"Movie found for **{query}**:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🎬 Get File", url=url)]]
        )
    )

app.run()
