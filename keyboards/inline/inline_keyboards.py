from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek Tili", callback_data="uz")
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Русский Язык", callback_data="ru")
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en")
        ]
    ]
)
