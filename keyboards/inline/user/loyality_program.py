from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import db


async def loyality_program_IKB() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1
    )
    keyboard.add(*[InlineKeyboardButton(text="Мои рефирралы", callback_data=f"referral_")])

    return keyboard