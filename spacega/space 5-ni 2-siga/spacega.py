from aiogram import Bot, Dispatcher, executor, types

api_token = "6470957998:AAE-UAuVWKb2MeEB9gE3WTkvEggoBc-CcNk"
bot = Bot(token=api_token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"Assalomu Alaykum: {message.from_user.full_name} Botga Xush Kelibsiz!"
    await message.answer(text=text)

@dp.message_handler(commands="info")
async def info_bot_handler(message: types.Message):
    text = f"""
Botdan Foydalanish Uchun: /start Bosas,\n
Yordam Uchun: /help Bosaz,\n
Bot Haqida Ma'lumot Uchun: /info Bosas\n
Lekin Botda Hech Narsa Mavjud Emas!\n
"""
    await message.answer(text=text)

@dp.message_handler(commands="help")
async def help_handler(message: types.Message):
    text = f"Botda Hech Narsa Mavjud Emas!"
    await message.answer(text=text)

@dp.message_handler(text="Qandaysiz")
async def how_are_you_handler(message: types.Message):
    text = f"Yaxshi Raxmat: {message.from_user.full_name} Ozizda Nma Gap?"
    await message.answer(text=text)

@dp.message_handler(text="Qandaysan")
async def how_are_you_handler(message: types.Message):
    text = f"Yaxshi Raxmat: {message.from_user.full_name} Ozizda Nma Gap?"
    await message.answer(text=text)

@dp.message_handler(text="Qanday")
async def how_are_you_handler(message: types.Message):
    text = f"Yaxshi Raxmat: {message.from_user.full_name} Ozizda Nma Gap?"
    await message.answer(text=text)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def video_handler(message: types.Message):
    text = f"Video Yuborganingiz Uchun Tashakkur: {message.from_user.full_name}"
    await message.answer(text=text)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def video_handler(message: types.Message):
    text = f"Rasm Yuborganingiz Uchun Tashakkur: {message.from_user.full_name}"
    await message.answer(text=text)

@dp.message_handler(content_types=types.ContentType.AUDIO)
async def video_handler(message: types.Message):
    text = f"Ovozlik Xabar Yuborganingiz Uchun Tashakkur: {message.from_user.full_name}"
    await message.answer(text=text)

@dp.message_handler(content_types=types.ContentType.STICKER)
async def video_handler(message: types.Message):
    text = f"Sticker Yuborganingiz Uchun Tashakkur: {message.from_user.full_name}"
    await message.answer(text=text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)