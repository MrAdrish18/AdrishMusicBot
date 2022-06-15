import os
import asyncio
import requests
import aiohttp
import yt_dlp

from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP
from config import SESSION_NAME

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command(["song", "music", " vsong", "video"]) & ~filters.private & ~filters.channel)
def song(client, message):

    message.delete()
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    chutiya = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("🔎")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "» 𝐍𝐚𝐡𝐢 𝐦𝐢𝐥𝐚🥺,  𝐬𝐨𝐧𝐠 𝐧𝐚𝐦𝐞 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐬𝐞𝐚𝐫𝐜𝐡 𝐤𝐚𝐫𝐨."
        )
        print(str(e))
        return
    m.edit(f"» 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐬𝐨𝐧𝐠 𝐟𝐫𝐨𝐦 𝐬𝐞𝐫𝐯𝐞𝐫 {bn} 𝐬𝐞𝐫𝐯𝐞𝐫 𝐁𝐚𝐛𝐲​.")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**• 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲​ » [{bn}](t.me/{bu}) 💕\n• 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 » {chutiya}\n• 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 𝐟𝐨𝐫 » {query}**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit("**» 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐞𝐫𝐫𝐨𝐫 𝐚𝐚𝐡𝐚 𝐫𝐞𝐩𝐨𝐫𝐭 𝐤𝐚𝐫𝐨​ » [{bn} sᴜᴩᴩᴏʀᴛ](t.me/{bu}) 💕**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
