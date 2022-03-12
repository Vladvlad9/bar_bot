from aiogram import types

from keyboards import *
from keyboards.default.user.contacts import contacts_kb
from loader import dp, db


@dp.message_handler(text="Контакты")
async def back_main_menu(message: types.Message):
    await message.answer('Наши контакты', reply_markup= await contacts_kb())