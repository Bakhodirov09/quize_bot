from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterStates(StatesGroup):
    set_lang = State()
    send_location = State()
    send_phone = State()
    set_lang_rus = State()
    send_location_rus = State()
    send_phone_rus = State()