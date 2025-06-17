import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("FILE_BOT_TOKEN")
FILE_CHANNEL = os.getenv("FILE_CHANNEL")

app = Client("file_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if len(message.command) == 1:
        return await message.reply("Send movie name or use Search Bot.")

    file_id = message.command[1]
    try:
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=int(FILE_CHANNEL),
            message_id=int(file_id)
        )
    except Exception as e:
        await message.reply(f"Error: {e}")

app.run()
