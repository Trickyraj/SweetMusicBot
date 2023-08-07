import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from SweetXMusic import LOGGER, app, userbot
from SweetXMusic.core.call import SweetX
from SweetXMusic.plugins import ALL_MODULES
from SweetXMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("SweetXMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("SweetXMusic").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SweetXMusic.plugins." + all_module)
    LOGGER("SweetXMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await SweetX.start()
    try:
        await SweetX.stream_call(
            "https://te.legra.ph/file/43796f8902e4e945d7c64.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("SweetXMusic").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await SweetX.decorators()
    LOGGER("SweetXMusic").info("Sweet Music start ")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("SweetXMusic").info("Stopping Music Bot...")
