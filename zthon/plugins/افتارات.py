#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ

import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from zthon import zedub

from zthon.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@zedub.zed_cmd(pattern="ุญุงูุงุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุญูุงูุงุช ูุงุชูุณ ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@RSHDO5", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**๐โุญูุงูุงุช ูุงุชูุณ ูุตููุฑุฉ ๐งธโฅ๏ธ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุณุชูุฑู ุงููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุณุชููุฑู ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**๐โุณุชููุฑูุงุช ุขูููู ูุตููุฑุฉ ๐ค๐งง**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูููู ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@Rqy_1", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โููุงุทูุน ุฑูููู ุดุฑุนููุฉ โง๐๐ธโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑูุงุฏู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shababbbbR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุดุจูุงุจ เขชููุงุฏูู โง๐๐คโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑูุงุฏูู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banatttR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุจููุงุช เขชููุงุฏูู โง๐๐คโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุจูุณุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎ . ุงูุชูุงุฑุงุช ุจูุณุช ุจููุงุช ...๐ง๐ปโโ๐ง๐ปโโโฐ**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@Tatkkkkkim", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุจูุณุช ุชุทูููู ุจููุงุช โง๐๐ง๐ปโโ๐ง๐ปโโโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุญุจ$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎ . ุงูุชูุงุฑุงุช ุชุทูููู ุญุจ ...โฅ๏ธโฐ**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@tatkkkkkimh", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุญูุจ ุชูุจููุฑเขช โง๐โฅ๏ธโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑูุงูุดู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูุงูุดูู ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** ๐ฌโุฑูุงูุดูู ุชุญุดููุด โง๐๐นโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุงุฏุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ููุทูุน ุงุฏุช ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**๐ฌโููุงุทูุน ุงููุฏุช ูููุนูู โง ๐ค๐ญโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุบูููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูููุทูุน ...**")
    try:
        zedgan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชูุงเขช ุงูุงุบูููู ูู ๐๐ถ**ูดโ โ โ โ โ โ โ โ โ โ โ โย?โ โ\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        

@zedub.zed_cmd(pattern="ุดุนุฑ$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุดุนูุฑ ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชููุงุฑ ููุทูุน ุงูุดุนูุฑ ููุฐุง ูู**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ูููุฒ$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูููููุฒ ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชููุงุฑ ููุทูุน ุงูููููุฒ ููุฐุง ูู**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑู ุงูุดู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูุงูุดูู ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**๐โุฑูุงูุดูู ุชุญุดููุด โง๐๐นโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ูุนูููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุตููุฑุฉ ููุนููููุฉ ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**๐โุตููุฑุฉ ููุนููููุฉ โง ๐ค๐กโ**\n\n[โง??๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุชููุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ููุช ุชูููุช ุจุงูุตููุฑ ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**โฆโููุช ุชูููุช ุจุงูุตููุฑ โงโ๏ธ๐โ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฎูุฑูู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ููู ุฎููุฑูู ุจุงูุตููุฑ ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โฆโููู ุฎููุฑูู  โงโ๏ธ๐โ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ููุฏ ุงููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎ . ุงูุชูุงุฑุงุช ุงูููู ุดุจูุงุจ ...๐ซโฐ**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@dnndxn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุขููู ุดุจูุงุจ โง๐๐๐ปโโโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุจูุช ุงููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎ . ุงูุชูุงุฑุงุช ุงูููู ุจููุงุช ...๐ซโฐ**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุขููู ุจููุงุช โง๐๐ง๐ปโโโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุจูุงุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎ . ุงูุชูุงุฑุงุช ุจููุงุช ุชูุจููุฑ ...๐ซโฐ**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banaaaat1", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โุงูุชูุงุฑุงุช ุจููุงุช ุชูุจููุฑเขช โง๐๐ง๐ปโโโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


