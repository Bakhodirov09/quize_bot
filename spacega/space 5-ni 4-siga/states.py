from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterStates(StatesGroup):
    name = State()
    age = State()
    book = State()