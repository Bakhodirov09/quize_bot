from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from states import RegisterStates
api_token = "6470957998:AAE-UAuVWKb2MeEB9gE3WTkvEggoBc-CcNk"
storage = MemoryStorage()
bot = Bot(token=api_token)
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"Assalomu Alaykum: {message.from_user.full_name} Iltimos Botdan Foydalanishingiz Uchun Ismingizni Kiriting!"
    await message.answer(text=text)
    await RegisterStates.name.set()

@dp.message_handler(state=RegisterStates.name)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "ism": message.text
    })
    text = f"Iltimos: {message.from_user.full_name} Yoshingizni Kiriting!"
    await message.answer(text=text)
    await RegisterStates.age.set()

@dp.message_handler(state=RegisterStates.age)
async def get_age_handler(message: types.Message, state: FSMContext):
    try:
        await state.update_data({
            "yosh": int(message.text)
        })
        text = f"Iltimos: {message.from_user.full_name} Qanday Kitobni Yoqtirasiz Shuni Kiriting!"
        await message.answer(text=text)
        await RegisterStates.book.set()
    except Exception as exc:
        print(exc)
        text = f"Iltimos: {message.from_user.full_name} Yoshingizni Tog'ri Kiriting! 😕"
        await message.answer(text=text)

@dp.message_handler(state=RegisterStates.book)
async def get_favourite_book(message: types.Message, state: FSMContext):
    await state.update_data({
        "kitob": message.text
    })
    data = await state.get_data()
    text = f"""Xurmatli: {data["ism"]} Botdan Ro'yxatdan Otganingiz Uchun Raxmat!"""
    await message.answer(text=text)
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)