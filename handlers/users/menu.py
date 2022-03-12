from aiogram import types

from keyboards import *
from keyboards.default.user.menu import menu_kb
from loader import dp, db


@dp.message_handler(text="Меню")
async def back_main_menu(message: types.Message):
    await message.answer('Основное меню', reply_markup= await menu_kb())