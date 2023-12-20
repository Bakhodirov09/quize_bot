from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

my_notes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mening Eslatmalarim")
        ],
        [
            KeyboardButton(text="Eslatmalarni Ochirish")
        ]
    ], resize_keyboard=True
)
