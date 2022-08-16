import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from TBH.modules.clientbot.clientbot import client
from TBH.modules.helpers.command import commandpro
from TBH.modules.helpers.decorators import sudo_users_only, errors
from TBH.utilities.misc import SUDOERS

@Client.on_message(commandpro(["op", "x", ".op"]) & filters.me)
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await client.download_media(targetcontent)
    send = await client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)


__MODULE__ = "Sᴇʟғ"
__HELP__ = f"""
**🥀 Dᴏᴡɴʟʟᴏᴀᴅ Aɴʏ Sᴇʟғ-Dᴇsᴛʀᴜᴄᴛ Mᴇᴅɪᴀ Aɴᴅ Sᴀᴠᴇ Iᴛ Tᴏ Yᴏᴜʀ Sᴀᴠᴇ Mᴇssᴀɢᴇ ✨**

**ᴜsᴀɢᴇ:**
`op|.op` - **Rᴇᴘʟʏ Tᴏ Sᴇʟғ-Dᴇsᴛʀᴜᴄᴛ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Tᴏ Dᴏᴡɴʟᴏᴀᴅ.**
"""
