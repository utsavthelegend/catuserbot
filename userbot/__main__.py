import sys

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import himiub
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("HimiUserbot")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    Himiub.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class HimiCheck:
    def __init__(self):
        self.sucess = True


Himicheck = HimiCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Himicheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫")
    print("Congratulations! 😁😎🎗🎗💫Himi Bot is ready to assist you. ❣❣❣")
    print(
        f"Hurray, now type {cmdhr}alive to see message if 💫himub is live\
        \nIf you need assistance, head to https://t.me/hosthejosh"
    )
    print("💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫🧡🤍💚💫")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Himicheck.sucess = True
    return


Himiub.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
    himiub.disconnect()
elif not Himicheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        himiub.run_until_disconnected()
    except ConnectionError:
        pass
