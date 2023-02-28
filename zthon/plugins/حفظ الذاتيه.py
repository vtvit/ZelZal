import os
import shutil
from asyncio import sleep
from telethon import events

from zthon import zedub
from zthon.core.logger import logging
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.echo_sql import addecho, get_all_echos, get_echos, is_echo, remove_all_echos, remove_echo, remove_echos

from zthon.core.logger import logging
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)
zedself = True

POSC = gvarstatus("Z_POSC") or "(وێنەی قفڵ)"

ZelzalSelf_cmd = (
    "𓆩 [ᯓ 𝗦𝗼𝘂𝗿𝗰𝗲 𝙄𝙌  - سەیڤکردنی وێنەی قفڵ 🧧](t.me/MGIMT) 𓆪\n\n"
    "**⪼** `.چالاککردنی وێنەی قفڵ`\n"
    "**بۆ چالاککردنی سەیڤکردنی وێنەی قفڵ بە خودکار**\n"
    "**ئەکاونتەکەت بە شێوەیەکی ئۆتۆماتیکی خۆی لە نامە سەیڤکراوەکانی ئەکاونتەکەت سەیڤی دەکات کاتێك هەرکەسێك وێنەی قفڵ یان ڤیدیۆت بۆ دەنێرێت**\n\n\n"
    "**⪼** `.ناچالاککردنی وێنەی قفڵ `\n"
    "**بۆ ناچالاککردنی سەیڤکردنی وێنەی قفڵ بە خودکار**\n\n\n"
    "**⪼** `.وێنەی قفڵ`\n"
    "**بە وەڵامدانەوەی ئەو وێنە یان ڤیدیۆیە کە بەکات نێردراوە بۆ سەیڤکردنی**\n\n"
    "\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 ﮼ﺣّ͠ــەمــە ](t.me/MGIMT) 𓆪"
)


@zedub.zed_cmd(pattern="وێنەی قفڵ")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalSelf_cmd)

@zedub.zed_cmd(pattern=f"{POSC}(?: |$)(.*)")
async def oho(event):
    if not event.is_reply:
        return await event.edit("**- ❝ ⌊بە وەڵامدانەوەی وێنەی بە کات نێردراو 𓆰...**")
    zzzzl1l = await event.get_reply_message()
    pic = await zzzzl1l.download_media()
    await zedub.send_file("me", pic, caption=f"**- ❝ ⌊وێنەی بە کات نێردراو سەیڤکرا ☑️ 🥳𓆰...**")
    await event.delete()

@zedub.zed_cmd(pattern="چالاککردنی وێنەی قفڵ")
async def start_datea(event):
    global zedself
    if zedself:
        return await edit_or_reply(event, "**- سەیڤکردنی وێنەی بە کات نێردراو .. پێشتر چالاککراوە ☑️**")
    zedself = True
    await edit_or_reply(event, "**- سەیڤکردنی وێنەی بە کات نێردراو چالاککرا .. بە سەرکەوتوویی ☑️**")

@zedub.zed_cmd(pattern="ناچالاککردنی وێنەی قفڵ")
async def stop_datea(event):
    global zedself
    if zedself:
        zedself = False
        return await edit_or_reply(event, "**- تم سەیڤکردنی وێنەی بە کات نێردراو نالاچالاککرا .. بە سەرکەوتوویی ☑️**")
    await edit_or_reply(event, "**- سەیڤکردنی وێنەی بە کات نێردراو .. پێشتر ناچالاککراوە  ☑️**")

#code for @R0R77
@zedub.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread))
async def sddm(event):
    global zedself
    zelzal = event.sender_id
    malath = zedub.uid
    if zelzal == malath:
        return
    if zedself:
        sender = await event.get_sender()
        chat = await event.get_chat()
        pic = await event.download_media()
        await zedub.send_file("me", pic, caption=f"[ᯓ 𝗦𝗼𝘂𝗿𝗰𝗲 𝙄𝙌 - سەیڤکردنی وێنەی قفڵ 🧧](t.me/MGIMT) .\n\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⌔╎بەخێربێی سەرۆك 🫂\n⌔╎ تـم سەیڤکردنی وێنەی بەکات نێردراو  .. سەرکەوتووە ☑️** ❝\n**⌔╎نێردراو** {_format.mentionuser(sender.first_name , sender.id)} .")

@zedub.zed_cmd(
    pattern="نامەی قفڵ(\d*) ([\s\S]*)",
    command=("نامەی قفڵ", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time.",
        "بەکارهێنان": "{tr}sdm [number] [text]",
        "نموونە": "{tr}نامەی قفڵ 10 چۆنی",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()

@zedub.zed_cmd(
    pattern="selfdm(\d*) ([\s\S]*)",
    command=("selfdm", plugin_category),
    info={
        "header": "To self destruct the message after paticualr time. and in message will show the time.",
        "بەکارهێنان": "{tr}selfdm [number] [text]",
        "نموونە": "{tr}selfdm 10 چۆنی",
    },
)
async def selfdestruct(destroy):
    "To self destruct the sent message"
    cat = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = cat[1]
    ttl = int(cat[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()
