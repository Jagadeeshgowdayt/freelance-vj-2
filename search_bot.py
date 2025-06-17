# search_bot.py
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

SEARCH_TOKEN = os.getenv("SEARCH_BOT_TOKEN")
API_ID      = int(os.getenv("API_ID"))
API_HASH    = os.getenv("API_HASH")
# e.g., the channel/chat where you keep your movie files
FILE_CHANNEL = os.getenv("FILE_CHANNEL")

app = Client("search_bot", api_id=API_ID, api_hash=API_HASH, bot_token=SEARCH_TOKEN)

@app.on_message(filters.command("search") & filters.private)
async def search_handler(client, message):
    query = " ".join(message.command[1:])
    # 1) Use your existing search logic to find a matching movie link in your DB/Channel
    #    For example, query a MongoDB collection of available files.
    link = await lookup_movie_link(query)  # implement this helper
    
    if not link:
        await message.reply_text(f"No results for “{query}.”")
        return
    
    # 2) Build a button that opens your File Bot passing the file ID:
    file_bot_username = "YourFileBot"  # without @
    payload = link.file_id  # or some identifier
    url = f"https://t.me/{file_bot_username}?start={payload}"
    
    await message.reply_text(
        f"Found “{query}”:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("👉 Get File", url=url)]]
        )
    )

if __name__ == "__main__":
    app.run()
