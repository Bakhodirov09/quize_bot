from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Test Qoshish"),
            KeyboardButton(text="🔍 Mening Testlarim")
        ],
        [
            KeyboardButton(text="👤 Profil"),
            KeyboardButton(text="📞 Aloqa")
        ]

    ], resize_keyboard=True
)

send_phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon Raqamni Yuborish", request_contact=True)
        ]
    ], resize_keyboard=True
)

back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Asosiy Menyuga Qaytish")
        ]
    ], resize_keyboard=True
)

test_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🆕 Yangi Variant"),
            KeyboardButton(text="➕ Yangi Savol")
        ],
        [
            KeyboardButton(text="🚫 Testni Tugatish")
        ]
    ], resize_keyboard=True
)