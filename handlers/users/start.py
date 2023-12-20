from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.inline_keyboards import *
from keyboards.default.default_keyboards import *
from aiogram.dispatcher.filters.builtin import CommandStart

from states.states import *
from utils.db_api.user_commands import *
from loader import dp

@dp.message_handler(state=TestCreateStates.title, text="⬅️ Asosiy Menyuga Qaytish")
async def back_main_menu_handler(message: types.Message, state: FSMContext):
    text = f"🏘 Asosiy Menyu"
    await state.finish()
    await message.answer(text=text, reply_markup=user_main_menu)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if await get_user(chat_id=message.chat.id):
        text = f"Xush Kelibsiz!"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = f"Iltimos Ozingizga Mos Tilni Tanlang!\nPlease Choose Your Language\nПожалуйста, выберите свой язык!"
        await message.answer(text=text, reply_markup=select_lang)
        await RegisterState.language.set()

@dp.callback_query_handler(state=RegisterState.language)
async def select_lang_handler(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({
        "lang": call.data
    })
    text = f"Iltimos: {call.message.from_user.full_name} Toliq Ismingizni Kirtig!"
    await call.message.answer(text=text)
    await RegisterState.full_name.set()

@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    text = f"Iltimos: {message.from_user.full_name} Telefon Raqamingizni Jo'nating!"
    await message.answer(text=text, reply_markup=send_phone_number)
    await state.update_data({
        "full_name": message.text,
        "created": message.date,
    })
    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number,
        "chat_id": message.chat.id
    })
    data = await state.get_data()
    if await add_user(data=data):
        text = f"Botga Xush Kelibsiz: {message.from_user.full_name}"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = f"Kechirasiz: {message.from_user.full_name} Botda Xatolik Yuz Berdi"
        await message.answer(text=text)
    await state.finish()

@dp.message_handler(text="➕ Test Qoshish")
async def add_test_handler(message: types.Message, state: FSMContext):
    text = f"✍️ Testingizni Nomini Kiriting!"
    await TestCreateStates.title.set()
    await message.answer(text=text, reply_markup=back_main_menu)

@dp.message_handler(state=TestCreateStates.title, content_types=types.ContentType.TEXT)
async def add_question_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "test_nomi": message.text,
        "chat_id": message.chat.id,
        "sana": message.date
    })
    data = await state.get_data()
    test_id = await add_test(data=data)
    if test_id:
        text = f"Testingiz Uchun Savol Kiriting!"
        await state.update_data({
            "test_id": test_id
        })
        await message.answer(text=text, reply_markup=back_main_menu)
        await TestCreateStates.question.set()
    else:
        text = f"Botda Xatolik Mavjud Adminga Murojaat Qiling Iltimos!"
        await message.answer(text=text, reply_markup=user_main_menu)

@dp.message_handler(state=TestCreateStates.question, content_types=types.ContentType.TEXT)
async def add_question_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    question_id = await add_question(data=data, message=message)
    if question_id:
        text = f"Savol Uchun Variant Kiriting!"
        await state.update_data({
            "question_id": question_id
        })
        await message.answer(text=text, reply_markup=back_main_menu)
        await TestCreateStates.option.set()
    else:
        text = f"Botda Xatolik Mavjud Adminga Murojaat Qiling Iltimos!"
        await message.answer(text=text, reply_markup=user_main_menu)

@dp.message_handler(state=TestCreateStates.option, content_types=types.ContentType.TEXT)
async def add_option_handler(message: types.Message, state: FSMContext):
    await state.update_data({
        "title": message.text
    })
    text = f'Bu Variantingiz Togrimi Yoki Yoq?'
    await message.answer(text=text)
    await TestCreateStates.is_true.set()

@dp.message_handler(state=TestCreateStates.is_true, content_types=types.ContentType.TEXT)
async def add_question_handler(message: types.Message, state: FSMContext):
    is_true = "None"
    if message.text == "✅ Xa":
        is_true = True
        await state.update_data({
            "is_true": True,
            "created_at": message.date
        })
    elif message.text == "❌ Yo'q":
        is_true = False
        await state.update_data({
            "is_true": False,
            "created_at": message.date
        })
    else:
        text = f"Xa Yoki Yoqmi Tanlang!"
        await message.answer(text=text)
        await TestCreateStates.is_true.set()
    if is_true == True or is_true == False:
        data = await state.get_data()
        option_id = await add_question_option(data=data)
        if option_id:
            text = f"Variant Qoshildi Yangi Savol Yoki Testni Tugatish Uchun Tanlang."
            await state.update_data({
                "option_id": option_id
            })
            await message.answer(text=text, reply_markup=test_menu)
            await TestCreateStates.next_step.set()
        else:
            text = f"Botda Xatolik Mavjud Adminga Murojaat Qiling Iltimos!"
            await message.answer(text=text, reply_markup=user_main_menu)

@dp.message_handler(state=TestCreateStates.next_step, text="🆕 Yangi Variant")
async def add_option_handler(message: types.Message, state: FSMContext):
    text = f'Yangi Variant Kiriting.'
    await message.answer(text=text)
    await TestCreateStates.option.set()

@dp.message_handler(state=TestCreateStates.next_step, text="➕ Yangi Savol")
async def add_option_handler(message: types.Message, state: FSMContext):
    text = f'Yangi Savol Kiriting.'
    await message.answer(text=text)
    await TestCreateStates.question.set()

@dp.message_handler(state=TestCreateStates.next_step, text="🚫 Testni Tugatish")
async def add_option_handler(message: types.Message, state: FSMContext):
    text = f'Test Qoshildi.'
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()