#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import OWNER_ID, OWNERS, KANAL
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], url=f"https://t.me/{KANAL}"
            ),
            InlineKeyboardButton(
                text=_["S_B_7"], url=f"tg://openmessage?user_id={OWNERS}"
            )
        ],
    ]


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_7"], url=f"tg://openmessage?user_id={OWNERS}"
            )
        ]
    )

    return buttons
