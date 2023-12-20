from aiogram import Bot, Dispatcher, executor, types

api_token = "6470957998:AAE-UAuVWKb2MeEB9gE3WTkvEggoBc-CcNk"
bot = Bot(token=api_token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"Assalomu Alaykum: {message.from_user.full_name}"
    await message.answer(text=text)

@dp.message_handler(commands="help")
async def start_handler(message: types.Message):
    text = f"Assalomu Alaykum: {message.from_user.full_name}\nBu Bot Hozircha Jaaaaaa Kottamas Endi Kottaro Qilishga Harakat Qilamz!😊"
    await message.answer(text=text)

@dp.message_handler(commands="info")
async def start_handler(message: types.Message):
    text = f"Bu Botdan Hozircha Foydalana Olmaysiz Sabab Bu Bot Hozircha Yakuniga Yetmagan!😔"
    await message.answer(text=text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)