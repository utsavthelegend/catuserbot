import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import himialive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, himiub, himiversion, mention

plugin_category = "utils"


@himiub.himi_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    start = datetime.now()
    await edit_or_reply(event, "Checking...")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**✯💫𝗛𝗶𝗺𝗶💎𝗕𝗼𝘁🥀 𝗶𝘀 𝗥𝗲𝗮𝗱𝘆 𝘁𝗼 𝘀𝗲𝗿𝘃𝗲 𝘆𝗼𝘂 𝗺𝗮𝘀𝘁𝗲𝗿 **"
    HIMI_IMG = gvarstatus("ALIVE_PIC")
    Himi_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = hjmi_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        Himiver=himiversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if HIMI_IMG:
        HIMI = [x for x in HIMI_IMG.split()]
        PIC = random.choice(HIMI)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(event, caption)


temp = "{ALIVE_TEXT}\n\n\
**{💫💫} 𝗢𝘄𝗻𝗲𝗿 : {mention}**\n\
**{💫💫} Uptime :** `{uptime}`\n\
**{💫💫} Telethon version :** `{telever}`\n\
**{💫💫} Python Version :** `{pyver}`\n\
**{💫💫} Database :** `{dbhealth}`\n"
**{💫💫} 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗨𝘀 :** `{@hosthejosh}`\n"


@himiub.himi_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}ialive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    ALIVE_TEXT = "** ℍ𝕚𝕞𝕚 𝕚𝕤 𝕒𝕝𝕚𝕧𝕖 𝕒𝕟𝕕 𝕖𝕒𝕘𝕖𝕣 𝕥𝕠 𝕙𝕖𝕝𝕡 𝕪𝕠𝕦**"
    Himi_caption = f"{ALIVE_TEXT}\n"
    Himi_caption += f"**{💫💫} Telethon version :** `{version.__version__}\n`"
    Himi_caption += f"**{💫💫} 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗨𝘀 :** `{@hosthejosh}`\n"
    Himi_caption += f"**{💫💫} Python Version :** `{python_version()}\n`"
    Himi_caption += f"**{💫💫} Owner:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, himi_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@himiub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await himialive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
