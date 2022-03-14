from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db


async def edit_inline_keyboard(name_BD) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1
    )
    #keyboard.add(*[InlineKeyboardButton(text="Изменить", callback_data=f"change_{name_BD}")])
    keyboard.add(*[InlineKeyboardButton(text="Удалить", callback_data=f"delete_{name_BD}")])

    return keyboard