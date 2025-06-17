# file_bot.py
import os
from pyrogram import Client, filters
from pyrogram.types import Message

FILE_TOKEN  = os.getenv("FILE_BOT_TOKEN")
API_ID      = int(os.getenv("API_ID"))
API_HASH    = os.getenv("API_HASH")
FILE_CHANNEL = os.getenv("FILE_CHANNEL")

app = Client("file_bot", api_id=API_ID, api_hash=API_HASH, bot_token=FILE_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    if len(message.command) == 1:
        return await message.reply_text("Send me a movie name or use the button from the Search Bot.")
    
    file_id = message.command[1]
    # 1) Validate the payload
    # 2) Retrieve the actual file: file_id could be a media file_id or a database key
    await client.send_cached_media(
        chat_id=message.chat.id,
        file_id=file_id  # if you stored Telegram’s file_id
    )

if __name__ == "__main__":
    app.run()
