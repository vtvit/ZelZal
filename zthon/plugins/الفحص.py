import random
import re
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from zthon import StartTime, zedub, zedversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"
STATS = gvarstatus("STATS") or "پشکنین"


@zedub.zed_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    zedevent = await edit_or_reply(event, "**⿻┊‌ پشکنین بۆ بۆتی تایبەت بە تۆ ..**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** بـۆتـی زیـرەك  𝙄𝙌 𝙐𝙎𝙀𝙍𝘽𝙊𝙏  کاردەکات .. بە سەرکەوتوویی ☑️ 𓆩 **"
    ZED_IMG = gvarstatus("ALIVE_PIC")
    zed_caption = gvarstatus("ALIVE_TEMPLATE") or iq_temp
    caption = zed_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        zdver=iqversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ZED_IMG:
        ZED = [x for x in ZED_IMG.split()]
        PIC = random.choice(IQ)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await zedevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                zedevent,
                f"**میدیا هەڵەیە **\nبەستەر نییە بۆ بەکارهێنانی فەرمانەکە    \n `.زیادکردنی وێنەی پشکنین`\n\n**ناتوانی بەستەری وێنەکە وەربگریت  :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            zedevent,
            caption,
        )


iq_temp = """{ALIVE_TEXT}
**‎{Z_EMOJI}‌‎𝙽𝙰𝙼𝙴 𖠄 {mention}** ٫
**‌‎{Z_EMOJI}‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 {pyver}** ٫
**‌‎{Z_EMOJI}‌‎𝙸𝚀 𖠄 {telever}** ٫
**‌‎{Z_EMOJI}‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 {uptime}** ٫
‌‎**{Z_EMOJI}‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 {ping}** ٫
**{Z_EMOJI} چەناڵی سەرچاوە🖤 :** [ئێرە دابگرە](https://t.me/IQUSER0)"""
**𖠄 𝙄𝙌 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𖠄**"""

@zedub.zed_cmd(
    pattern="پشکنینن$",
    command=("پشکنینن", plugin_category),
    info={
        "header": "- ـۆ پشکنین کە بۆتەکە بە سەرکەوتوویی کار دەکات تایبەتمەندی سەرهێڵ ✓",
        "بەکارهێنان": [
            "{tr}پشکنینن",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    zed_caption = "** بـۆتی زیـرەك 𝙄𝙌 𝘽𝙊𝙏  کاردەکات .. بە سەرکەوتوویی ☑️ 𓆩 **\n"
    zed_caption += f"**{Z_EMOJI} وەشانی تێلثۆن :** `{version.__version__}\n`"
    zed_caption += f"**{Z_EMOJI} وەشانی بـۆتی زیرەك :** `{iqversion}`\n"
    zed_caption += f"**{Z_EMOJI} وەشانی پایثۆن :** `{python_version()}\n`"
    zed_caption += f"**{Z_EMOJI} بەکارهێنەر :** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, zed_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await zedalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
