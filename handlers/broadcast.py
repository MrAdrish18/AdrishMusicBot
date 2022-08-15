import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as Anonymous
from config import SUDO_USERS

@Client.on_message(filters.command(["broadcast", "gcast"]))
async def broadcast(_, message: Message):
    await message.delete()
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`𝐇𝐚𝐫𝐥𝐞𝐲 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐛𝐚𝐛𝐲...`")
        if not message.reply_to_message:
            await wtf.edit("**__𝐦𝐚𝐬𝐬𝐚𝐠𝐞 𝐩𝐞 𝐫𝐞𝐩𝐥𝐲 𝐤𝐚𝐫𝐨 𝐛𝐚𝐛𝐲 𝐛𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐤𝐚𝐫𝐧𝐞 𝐤𝐞 𝐥𝐢𝐲𝐞__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in Anonymous.iter_dialogs():
            try:
                await Anonymous.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`𝐇𝐚𝐫𝐥𝐞𝐲 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠...` \n\n**𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐞𝐝 𝐓𝐨 :** `{sent}` **𝐂𝐡𝐚𝐭𝐬** \n**𝐅𝐚𝐢𝐥𝐞𝐝 𝐈𝐧 :** `{failed}` **𝐂𝐡𝐚𝐭𝐬**")
                await asyncio.sleep(0.3)
            except:
                failed=failed+1
        await message.reply_text(f"**𝐇𝐚𝐫𝐥𝐞𝐲 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲** \n\n**𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐞𝐝 𝐓𝐨 :** `{sent}` **𝐂𝐡𝐚𝐭𝐬** \n**𝐅𝐚𝐢𝐥𝐞𝐝 𝐈𝐧 :** `{failed}` **𝐂𝐡𝐚𝐭𝐬**")
