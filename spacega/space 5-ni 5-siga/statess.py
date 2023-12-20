from aiogram.dispatcher.filters.state import StatesGroup, State


class Note(StatesGroup):
    add_note = State()
    delete_note = State()