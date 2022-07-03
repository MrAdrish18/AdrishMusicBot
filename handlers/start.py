import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 𝑯𝒆𝒚 {message.from_user.mention()} !

        𝑻𝒉𝒊𝒔 𝒊𝒔 [{bn}](t.me/{bu}), 𝒔𝒖𝒑𝒆𝒓 𝒇𝒂𝒕𝒔 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒎𝒖𝒔𝒊𝒄 𝒃𝒐𝒕 𝒇𝒐𝒓 𝒗𝒊𝒅𝒆𝒐 𝒄𝒉𝒂𝒕𝒔...

𝑨𝒍𝒍 𝒎𝒚 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒄𝒂𝒏 𝒃𝒆 𝒖𝒔𝒆𝒅 𝒃𝒚 𝒘𝒊𝒕𝒉 𝒎𝒚 𝒄𝒐𝒎𝒎𝒂𝒏𝒅 𝒉𝒂𝒏𝒅𝒍𝒆𝒓 : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [𝗢𝘄𝗻𝗲𝗿](t.me/{me})
┣★
┗━━━━━━━━━━━━━━┛

💞 𝒊𝒇 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒂𝒏𝒚 𝒒𝒖𝒆𝒓𝒚 𝒕𝒉𝒆𝒏 𝒅𝒎 𝒎𝒚 𝒐𝒘𝒏𝒆𝒓 [ᴏᴡɴᴇʀ](t.me/{me}) 𝐁𝐚𝐛𝐲...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 𝐀𝐝𝐝 𝐦𝐞 𝐛𝐚𝐛𝐲​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "💔 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 💔", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "🍒 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 𝐈𝐧𝐥𝐢𝐧𝐞 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "🤯 𝐍𝐨𝐭𝐞𝐬 🤯", url="https://t.me/Aimers_Notes"
                    )]
            ]
       ),
    )

