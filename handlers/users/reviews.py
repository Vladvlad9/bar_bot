
from aiogram import types
from aiogram.dispatcher import FSMContext

from states import reviewST

from loader import dp


@dp.message_handler(text="Оставить отзыв")
async def review_name(message: types.Message):
    await message.answer("Поставте вашу оценку от 1 до 5")
    await reviewST.grade.set()


@dp.message_handler(state=reviewST.grade)
async def grade_review(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(grade=message.text)
        if 1 <= int(message.text) <= 3:
            await message.answer('Нам очень жаль, что именно вам не понравилось?')
        elif 4 <= int(message.text) <= 5:
            await message.answer('Нам очень приятно, можете описать что именно вам понравилось?')
        else:
            while 1 <= int(message.text) >= 5:
                await message.answer('Введите оценку от 1 до 5')
                await message.text

        await reviewST.next()
        await reviewST.description.set()
    else:
        await message.answer('Вы ввели некорректную оценку')


@dp.message_handler(state=reviewST.description)
async def description_review(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Спасибо, ваш отзыв очень важен для нас')
    await state.finish()
