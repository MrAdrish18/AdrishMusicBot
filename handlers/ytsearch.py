# the logging things
import logging

from pyrogram.types import Message
from search_engine_parser import GoogleSearch
from youtube_search import YoutubeSearch

from pyrogram import Client as app, filters

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(pyrogram.filters.command(["search"]))
async def ytsearch(_, message: Message):
    await message.delete()
    try:
        if len(message.command) < 2:
            await message.reply_text("» 𝐊𝐨𝐢 𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 𝐭𝐨 𝐝𝐨 𝐬𝐞𝐚𝐫𝐜𝐡 𝐤𝐚𝐫𝐧𝐞 𝐤𝐞 𝐥𝐢𝐲𝐞 𝐁𝐚𝐛𝐲!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"📌 𝐓𝐢𝐭𝐥𝐞 : {results[i]['title']}\n"
            text += f"⏱ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : {results[i]['duration']}\n"
            text += f"👀 𝐕𝐢𝐞𝐰𝐬 : {results[i]['views']}\n"
            text += f"📣 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : {results[i]['channel']}\n"
            text += f"🔗 𝐋𝐢𝐧𝐤 : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
