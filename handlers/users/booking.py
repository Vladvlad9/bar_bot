import re
from datetime import datetime

import aiogram_calendar.dialog_calendar

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from keyboards import *
from loader import dp, db
from states import bookingST


@dp.message_handler(state='*', commands="Назад")
@dp.message_handler(Text(equals='Назад', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_data()

    if current_state is None:
        return
    await state.finish()


@dp.message_handler(text=["Забронировать столик"])
async def load_name(message: types.Message):
    await message.answer("Введите Ваше имя", reply_markup=await back_kb_mn())
    await bookingST.fname_user.set()


@dp.message_handler(state=bookingST.fname_user)
async def fname_user_stock(message: types.Message, state: FSMContext):
    await state.update_data(fname=message.text)
    await bookingST.next()
    await bookingST.lname_user.set()
    await message.answer('Введите вашу фамилию')


@dp.message_handler(state=bookingST.lname_user)
async def fname_user_stock(message: types.Message, state: FSMContext):
    await state.update_data(lname=message.text)
    await bookingST.next()
    await bookingST.date.set()
    await message.answer("Пожалуйста, выберите дату: ", reply_markup=await SimpleCalendar().start_calendar())


@dp.callback_query_handler(simple_cal_callback.filter(), state=bookingST.date)
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'Вы выбрали: {date.strftime("%d/%m/%Y")}'

        )
    result_select_date_user = date.strftime("%d/%m/%Y")
    await state.update_data(dateST=result_select_date_user)
    await bookingST.next()
    await bookingST.time.set()
    await callback_query.message.answer('Введите время посещения')


def is_valid_time(time) -> bool:
    return bool(re.search(r'\d{2}:?\d{2}$', time))


@dp.message_handler(state=bookingST.time)
async def timeST_stock(message: types.Message, state: FSMContext):
    await state.update_data(timeST=message.text)
    await message.answer(f'Выберите время: ')
    #key = True
    # while key:
    #     if is_valid_time(message.text):
    #         key = False
    #     else:
    #         print('Введтье в формате "Часы:минуты"')
    #

    await bookingST.next()
    await bookingST.number_people.set()
    await message.answer('Введите количество человек:')


@dp.message_handler(state=bookingST.number_people)
async def number_people_stock(message: types.Message, state: FSMContext):
    await state.update_data(number_people=message.text)

    data_booking = await state.get_data()
    lname = data_booking['lname']
    fname = data_booking['fname']
    date_booking = data_booking['dateST']
    time_booking = data_booking['timeST']
    number_people = data_booking['number_people']

    if await db.add_booking_user(message.from_user.id, lname, fname, date_booking, time_booking, number_people):
        await message.answer(f'{fname} вы успешно забронировали столик')

    await state.finish()







