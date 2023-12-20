import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from statess import *
from default_keyboards import *
api_token = "6470957998:AAE-UAuVWKb2MeEB9gE3WTkvEggoBc-CcNk"
storage = MemoryStorage()
bot = Bot(token=api_token)
dp = Dispatcher(bot=bot, storage=storage)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute(f"""
CREATE TABLE IF NOT EXISTS notes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
note_text TEXT,
date_note TEXT,
chat_id INTEGER
)
""")

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"Assalomu Alaykum: {message.from_user.full_name} Siz Bu Bot Orqali Ozizga Eslatmalar Qoya Olasiz!\nEslatma Yasash Uchun /add_note Buyrugini Yozing!"
    await message.answer(text=text, reply_markup=my_notes)

@dp.message_handler(commands="add_note")
async def add_note_handler(message: types.Message, state: FSMContext):
    text = f"Iltimos: {message.from_user.full_name} Yangi Eslatmangizni Yozing!"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await Note.add_note.set()

@dp.message_handler(state=Note.add_note)
async def add_note_database_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "note": message.text,
        "date": message.date,
        "chat_id": message.chat.id
    })
    data = await state.get_data()
    note = data["note"]
    date = data["date"]
    chat_id = data["chat_id"]
    cursor.execute(f"""
INSERT INTO notes(note_text, date_note, chat_id) VALUES (?,?,?)
""", (note, date, chat_id))
    conn.commit()
    text = f"😊 Tabriklayman: {message.from_user.full_name} Sizning Yangi Eslatmangiz Mening Eslatmarim Bolimiga Qoshildi!"
    await message.answer(text=text, reply_markup=my_notes)
    await state.finish()

@dp.message_handler(text="Mening Eslatmalarim")
async def my_notes_handler(message: types.Message):
    notes = cursor.execute(f"SELECT * FROM notes WHERE chat_id={message.chat.id}").fetchall()
    if notes:
        for i in notes:
            idsi = i[0]
            note = i[1]
            date = i[2]
            text = f"ID Raqami: {idsi}\n\n<b>Eslatmangiz: {note}</b>.\n\nJoylangan Sana: {date}"
            await message.answer(text=text)
    else:
        await message.answer(text=f"Kechirasiz: {message.from_user.full_name} Sizda Eslatmalar Mavjud Emas!😕 ", reply_markup=my_notes)

@dp.message_handler(text="Eslatmalarni Ochirish")
async def delete_notes(message: types.Message):
    notes = cursor.execute(f"SELECT * FROM notes WHERE chat_id={message.chat.id}").fetchall()
    if notes:
        for i in notes:
            idsi = i[0]
            note = i[1]
            date = i[2]
            text = f"ID Raqami: {idsi}\n\n<b>Eslatmangiz: {note}</b>.\n\nJoylangan Sana: {date}"
            await message.answer(text=text)
            await message.answer(text=f"Iltimos: {message.from_user.full_name} Eslatmangiz ID Raqamini Kiriting!", reply_markup=ReplyKeyboardRemove())
            await Note.delete_note.set()
    else:
        await message.answer(text=f"Kechirasiz: {message.from_user.full_name} Sizda Eslatmalar Mavjud Emas!😕 ", reply_markup=my_notes)


@dp.message_handler(state=Note.delete_note)
async def delete_note_handler(message: types.Message, state: FSMContext):
    idsi = cursor.execute(f"SELECT * FROM notes WHERE id={message.text}").fetchone()
    if idsi:
        cursor.execute(f"DELETE FROM notes WHERE id={message.text} AND chat_id={message.chat.id}")
        conn.commit()
        textt = f"Eslatmangiz Mening Eslatmalarim Bolimidan Muvaffaqqiyatli Olib Tashlandi!"
        await message.answer(text=textt, reply_markup=my_notes)
    else:
        textr = f"Kechirasiz: {message.from_user.full_name} Sizda Bunday ID Raqamdagi Eslatma Mening Eslatmalarim Bolimidan Topilmadi!"
        await message.answer(text=textr, reply_markup=my_notes)
    await state.finish()

conn.commit()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
