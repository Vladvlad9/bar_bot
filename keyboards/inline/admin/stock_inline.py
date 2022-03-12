from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db


async def stock_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1
    )
    keyboard.add(*[InlineKeyboardButton(text="Да", callback_data=f"yes_")])
    keyboard.add(*[InlineKeyboardButton(text="Нет", callback_data=f"no_")])

    return keyboard