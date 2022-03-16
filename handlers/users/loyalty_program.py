import cv2
from aiogram import types

import pyqrcode as pq
from keyboards import *
from keyboards.default.user.menu import menu_kb
from keyboards.inline.user import loyality_program_IKB
from loader import dp, db, bot


@dp.message_handler(text=["Программа лояльности"])
async def loyalty_program(message: types.Message):
    bot_username = (await bot.get_me()).username

    id_referral = message.from_user.id

    bot_link = f'https://t.me/{bot_username}?start={id_referral}'

    balance = await db.check_balance(message.from_user.id)
    current_balance = balance[0]
    loyalty_txt = f'Ваша реферальная ссылка:\n{bot_link}\n' \
                  f'Ваш баланс: {current_balance[0]} р.'

    await message.answer(loyalty_txt, reply_markup= await loyality_program_IKB())


@dp.callback_query_handler(lambda call: "referral_" in call.data)
async def my_referral(call: types.callback_query):
    rows = await db.check_referrals(call.from_user.id)
    text = ''
    for num, row in enumerate(rows):
        #chat = await bot.get_chat(row)
        #user_link = chat.get_mention(as_html=True)
        text += f'{str(num)}. {str(row)}\n'
    await call.message.answer(text)