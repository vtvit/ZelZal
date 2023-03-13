import contextlib
import sys

import zthon
from zthon import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import mybot
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)


LOGS = logging.getLogger("IQ")
cmdhr = Config.COMMAND_HAND_LER

print(zthon.__copyright__)
print(f"امەرجەکان  {zthon.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("⌭ دەستی کرد بە دابەزاندنی بۆتی زیرەك ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("⌭ بۆت دەستی بەکارکردن کرد ⌭")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


try:
    LOGS.info("⌭ دۆخی لەسەرهێڵ چالاك دەبێت ⌭")
    zedub.loop.run_until_complete(mybot())
    LOGS.info("✓ بە سەرکەوتوویی چالاککرا ✓")
except Exception as e:
    LOGS.error(f"- {e}")


try:
    LOGS.info("⌭ داگرتنی ئێکسسوارات ⌭")
    zedub.loop.create_task(saves())
    LOGS.info("✓ داگرترا بە سەرکەوتویی ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info(f"⌔┊ بە سەرکەوتوویی بۆتی زیرەك دامەزرا ✓")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return


zedub.loop.run_until_complete(startup_process())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        zedub.run_until_disconnected()
else:
    zedub.disconnect()
