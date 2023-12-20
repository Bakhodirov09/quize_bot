from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()
    language = State()

class TestCreateStates(StatesGroup):
    title = State()
    question = State()
    option = State()
    is_true = State()
    next_step = State()
