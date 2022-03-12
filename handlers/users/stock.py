from aiogram import types

from keyboards import *
from loader import dp, db


@dp.message_handler(text=["Акции"])
async def load_name(message: types.Message):
    await message.answer("Наши акции", reply_markup=await back_kb())

    markup = types.InlineKeyboardMarkup()
    types.InlineKeyboardMarkup()

    photo = await db.get_stock()
    for photo_i in photo:
        await message.answer_photo(photo_i[1], reply_markup=markup)
        await message.answer(f'Описание: {photo_i[2]}')