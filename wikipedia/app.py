from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from default_keyboards import *

from inline_keyboards import *

from states import RegisterStates

api_token = "6470957998:AAE-UAuVWKb2MeEB9gE3WTkvEggoBc-CcNk"
bot = Bot(token=api_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "🇺🇿 Botga Xush Kelibsiz Botdan Foydalanish Uchun Tilni Tanlang: " \
           "🇷🇺 Добро пожаловать в бот. Выберите язык для использования бота: "
    await message.answer(text=text, reply_markup=select_lang)
    await RegisterStates.set_lang.set()

@dp.message_handler(state=RegisterStates.set_lang, text="🇺🇿 Uzbek Tili")
async def uzbek_tili(message: types.Message, state: FSMContext):
    await state.update_data({
        "til": "🇺🇿 Uzbek Tili"
    })
    text = "🇺🇿 Uzbek Tiliga O'tkazildi!" \
           "Tel Nomeriz!"
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()

@dp.message_handler(state=RegisterStates.set_lang, text="🇷🇺 Русский Язык")
async def rus_menu(message: types.Message):
    text = "Переведено на русский!" \
           "Выберите тип фаст-фуда:"
    await message.answer(text=text, reply_markup=send_phone_rus)

@dp.message_handler(text="⚙️ Tilni O'zgartirish / Изменить язык")
async def set_lang_handler(message: types.Message):
    text = "🇺🇿 Tilni Tanlang!" \
           "" \
           "" \
           "🇷🇺 Выберите язык"
    await message.answer(text=text, reply_markup=select_lang)

@dp.message_handler(text="⚙️ Изменить язык / Tilni O'zgartirish")
async def set_lang_handler(message: types.Message):
    text = "🇺🇿 Tilni Tanlang!" \
           "" \
           "" \
           "🇷🇺 Выберите язык"
    await message.answer(text=text, reply_markup=select_lang)

@dp.message_handler(text="🍕 Bellissimo")
async def bellissimo_handler(message: types.Message):
    text = "Bellissimo"
    await message.answer(text=text, reply_markup=bellissimo_pizza_menu)

@dp.message_handler(text="🍕 Беллиссимо")
async def bellissimo_handler(message: types.Message):
    text = "Беллиссимо"
    await message.answer(text=text, reply_markup=bellissimo_pizza_menu_rus)

@dp.message_handler(text="🥩 Go'shtlik Lavash")
async def goshtlik_lavash(message: types.Message):
    text = "Grilda pishirilgan mol go'shti va pishgan pomidorning suvli" \
           " bo'laklari,oltin kartoshka chiplari, eng yangi klassik lavashdagi yangi piyoz va o'tlar" \
           " bilan sharqona pomidor sousi."
    photo = InputFile("./../evos_bots/goshtlik_lavash.jpg")
    await message.answer_photo(photo=photo, reply_markup=mini_big)
    await message.answer(text=text)

@dp.message_handler(text="🍕 Tovuqli Donar (New)")
async def bellissimo_handler(message: types.Message):
    photo = InputFile(path_or_bytesio="./../photos/5fb58b09-5c77-44de-8de8-f1be55c2aef1.png")
    text = "Kurka filesi, motsarella pishlogʻi, qarsildoq bulgʻor qalampiri," \
           " qoʻziqorin, qora zaytun, pepperoni va piyoz tomat sousi bilan"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕 Куриный Донар (Новый)")
async def bellissimo_handler(message: types.Message):
    photo = InputFile(path_or_bytesio="./../photos/5fb58b09-5c77-44de-8de8-f1be55c2aef1.png")
    text = "Филе индейки, сыр моцарелла, хрустящий болгарский перец" \
            " с грибами, маслинами, пепперони и луково-томатным соусом"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕🧀 Pishloqli Pizza")
async def cheese_pizza_handler(message: types.Message):
    photo = InputFile(path_or_bytesio="./../photos/Pishloqlik_Pizza.png")
    text = "Haqiqiy motsarella firmenniy va alfredo sousi bilan uyg'unlikda"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕🧀 Пицца с сыром")
async def cheese_pizza_handler(message: types.Message):
    photo = InputFile(path_or_bytesio="./../photos/Pishloqlik_Pizza.png")
    text = "Настоящая моцарелла в сочетании с фирменни и соусом Альфредо"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕 Go'shtlik Miks")
async def goshtlik_pizza(message: types.Message):
    text = "Pitsa, barbekyu va burger souslari solingan, donar, kabob, mol go'shti va pepperoni kolbasasi bilan" \
           " haqiqiy motsarella pishlog'i va piyoz, kornishonlar, bulg'or qalampiri va pomidorlar uyg'unligi."
    photo = InputFile(path_or_bytesio="./../photos/Goshtlik_Pizza.png")
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕 Мясной микс")
async def goshtlik_pizza(message: types.Message):
    text = "Пицца, соусы для барбекю и бургеров, с крупами, шашлыками, говядиной и колбасой пепперони" \
            "Сочетание настоящего сыра моцарелла и лука, корнишонов, болгарского перца и помидоров."
    photo = InputFile(path_or_bytesio="./../photos/Goshtlik_Pizza.png")
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕 Donar Pizza")
async def donar_pizza_handler(message: types.Message):
    text = "Donar go‘shti va haqiqiy motsarella pishlog‘i solingan mazali va to‘yimli pitsa"
    photo = InputFile(path_or_bytesio="./../photos/Donar_Pizza.png")
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍕 Донер Пицца")
async def donar_pizza_handler(message: types.Message):
    text = "Вкусная и сытная пицца с мясом донара и настоящим сыром моцарелла."
    photo = InputFile(path_or_bytesio="./../photos/Donar_Pizza.png")
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🌯 Evos")
async def bellissimo_handler(message: types.Message):
    text = "Evos Menu"
    await message.answer(text=text, reply_markup=Evos_menu)

@dp.message_handler(text="🌯 Эвос")
async def bellissimo_handler(message: types.Message):
    text = "Evos Menu"
    await message.answer(text=text, reply_markup=Evos_menu_rus)

@dp.message_handler(text="🌯 Lavash")
async def lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/lavash_menu.jpg")
    text = "Lavaash Turini Tanlang: "
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_lavash)

@dp.message_handler(text="🌯 Лаваш")
async def lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/lavash_menu.jpg")
    text = "Выберите тип лаваша:"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_lavash_rus)

@dp.message_handler(text="🐔 Tovuqlik Lavash")
async def tovuqlik_lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    text = "Grilda pishirilgan tovuq go'shti, sharqona ziravorlar, yangi pishgan pomidor bo'laklari, tabiiy " \
           "kartoshka chiplari, eng yangi klassik lavashda yangi piyoz va o'tlar bilan sharqona pomidor sousi bilan" \
           "xususiy retsept bo'yicha marinadlangan."
    await message.answer_photo(photo=photo,caption=text, reply_markup=mini_big_tovuq)

@dp.callback_query_handler(text="big_tovuq")
async def big_tovuq(call: types.CallbackQuery):
    text = "Big Tovuqlik Lavash: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_tovuq")
async def big_tovuq(call: types.CallbackQuery):
    text = "Mini Tovuqlik Lavash: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🐔 Куриный лаваш")
async def tovuqlik_lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    text = "Курица гриль, восточные специи, кусочки свежих спелых помидоров, натуральные "\
            "картофельные чипсы, свежайший классический лаваш со свежим луком и зеленью в восточном томатном соусе"\
            "маринованное по особому рецепту."
    await message.answer_photo(photo=photo, caption=text, reply_markup=mini_big_tovuq_rus)


@dp.callback_query_handler(text="big_tovuq_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Биг куриный лаваш: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)


@dp.callback_query_handler(text="mini_tovuq_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Мини куриный лаваш: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🧀🥩 Sirlik Go'shtlik Lavash")
async def sirlik_lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/sirlik_goshtlik_lavash.jpg")
    text = "Grilda pishirilgan tovuq go'shti, sharqona ziravorlar, yangi pishgan pomidor bo'laklari, " \
           "tabiiy kartoshka chiplari, bir bo'lak Cheddar pishloqi, yangi piyoz va o'tlar bilan sharqona" \
           " pomidor sousi, eng yangi pishloqli pita nonida xususiy retsept bo'yicha marinadlangan."
    await message.answer_photo(photo=photo, caption=text, reply_markup=mini_big_sirlik_gosht)

@dp.callback_query_handler(text="big_gosht_sir")
async def big_tovuq(call: types.CallbackQuery):
    text = "Big Pishloqlik Go'shtlik: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/sirlik_goshtlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_gosht_sir")
async def big_tovuq(call: types.CallbackQuery):
    text = "Mini Pishloqlik Go'shtlik Lavash: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/sirlik_goshtlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🧀🥩 Сыр Мясной Лаваш")
async def sirlik_lavash(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/sirlik_goshtlik_lavash.jpg")
    text = "Курица гриль, восточные специи, кусочки свежих спелых помидоров" \
            "Восточный с натуральными картофельными чипсами, кусочком сыра Чеддер, свежим луком и зеленью" \
            "Томатный соус, маринованный по фирменному рецепту на свежайшем сырном лаваше"
    await message.answer_photo(photo=photo, reply_markup=mini_big_sirlik_gosht_rus)
    await message.answer(text=text)

@dp.callback_query_handler(text="big_gosht_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Биг куриный лаваш: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)


@dp.callback_query_handler(text="mini_gosht_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Мини сырно-мясной лаваш: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🧀🐔 Sirlik Tovuqlik Lavash")
async def sirlik_lavash_tovuq(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_sirlik_lavash.jpg")
    text = "Grilda pishirilgan tovuq go'shti, sharqona ziravorlar, yangi pishgan pomidor" \
           " bo'laklari, tabiiy kartoshka chiplari, bir bo'lak Cheddar pishloqi, yangi piyoz va" \
           " o'tlar bilan sharqona pomidor sousi, eng yangi pishloqli pita nonida xususiy retsept" \
           " bo'yicha marinadlangan."
    await message.answer_photo(photo=photo, caption=text, reply_markup=mini_big_tovuq_sirlik_tovuq)

@dp.callback_query_handler(text="big_tovuq_sir")
async def big_tovuq(call: types.CallbackQuery):
    text = "Big Pishloqlik Tovuqlik: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_sirlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_tovuq_sir")
async def big_tovuq(call: types.CallbackQuery):
    text = "Mini Pishloqlik Tovuqlik Lavash: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/sirlik_goshtlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🧀🐔 Сырный куриный лаваш")
async def sirlik_lavash_tovuq(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_sirlik_lavash.jpg")
    text = "Курица гриль, восточные специи, свежие помидоры" \
            "ломтики, натуральные картофельные чипсы, кусочек сыра Чеддер, свежий лук и" \
            "Восточный томатный соус с зеленью, особый рецепт свежего сырного лаваша" \
            "маринованный в"
    await message.answer_photo(photo=photo, caption=text, reply_markup=mini_big_tovuq_sirlik_rus)

@dp.callback_query_handler(text="big_tovuq_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Биг куриный лаваш: 17000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)


@dp.callback_query_handler(text="mini_tovuq_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Мини сырно-мясной лаваш: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🥩 Achchiq Go'shtlik Lavash")
async def achchiq_gosht(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_goshtlik_lavash.jpg")
    text = "Grilda pishirilgan mol go'shti va pishgan pomidorning suvli bo'laklari," \
           "oltin chiplar, yangi piyoz bilan pomidor achchiq Kalampir sousi oltin jigarrang pita nonida."
    await message.answer_photo(photo=photo, reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🥩 Острый мясной лаваш")
async def achchiq_gosht(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_goshtlik_lavash.jpg")
    text = "Сочные кусочки говядины на гриле и спелых помидоров" \
            "Золотые чипсы, соус из свежих помидоров и острого перца на золотисто-коричневом лаваше."
    await message.answer_photo(photo=photo, reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🐔 Achchiq Tovuqlik Lavash")
async def achchiq_gosht(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_tovuqlik_lavash.jpg")
    text = "Grilda pishirilgan mol go'shti va pishgan pomidorning suvli bo'laklari," \
           "oltin chiplar, yangi piyoz bilan pomidor achchiq Kalampir sousi oltin jigarrang pita nonida."
    await message.answer_photo(photo=photo, reply_markup=achhiq_tovuq_lavash)
    await message.answer(text=text)

@dp.callback_query_handler(text="big_achchiq_tovuq_sir")
async def big_tovuq(call: types.CallbackQuery):
    text = "Big Achchiq Tovuqlik Lavash Narxi: 28000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_achchiq_tovuq_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Mini Achchiq Tovuqlik Lavash Narxi: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🐔 Острый куриный лаваш")
async def achchiq_gosht(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_tovuqlik_lavash.jpg")
    text = "Сочные кусочки курицы-гриль и спелых помидоров" \
            "Золотые чипсы, соус из свежих помидоров и острого перца на золотисто-коричневом лаваше."
    await message.answer_photo(photo=photo, reply_markup=achhiq_tovuq_lavash_rus)
    await message.answer(text=text)

@dp.callback_query_handler(text="big_achchiq_tovuq_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Биг острый куриный лаваш Цена: 28000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_achchiq_tovuq_sir_rus")
async def big_tovuq(call: types.CallbackQuery):
    text = "Мини острый куриный лаваш Цена: 14000 So'm"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_lavash.jpg")
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🌯 Fitter")
async def fitter_lavash(message: types.Message):
    text = "Yumshoq panjara qilingan tovuq go'shti, Aysberg salatasi, pishgan pomidor va yangi bodring bo'laklari," \
           " yumshoq Fetaxa pishloq, och yashil rangdagi engil qaymoqli eko sous Fitter lavash"
    photo = InputFile(path_or_bytesio="./../evos_bots/fitter_lavash.jpg")
    await message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🌯 Фиттер")
async def fitter_lavash(message: types.Message):
    text = "Нежная курица-гриль, салат айсберг, спелые помидоры и ломтики свежего огурца" \
            "мягкий сыр Фета, светло-зеленый светло-сливочный эко-соус Фиттер-лаваш"
    photo = InputFile(path_or_bytesio="./../evos_bots/fitter_lavash.jpg")
    await message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🏠 Asosiy Menu")
async def back_main_menu(message: types.Message):
    text = "Asosiy Menyu"
    await message.answer(text=text, reply_markup=main_menu)

@dp.message_handler(text="🏠 Главное меню")
async def back_main_menu(message: types.Message):
    text = "Главное меню"
    await message.answer(text=text, reply_markup=main_menu_rus)

@dp.message_handler(text="🍔 Gamburger")
async def gamburger_menu(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/gamburger_menu.jpg")
    text = "Gamburger Tanlang:"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Gamburger)

@dp.message_handler(text="🍔 Гамбургер")
async def gamburger_menu(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/gamburger_menu.jpg")
    text = "Gamburger Tanlang:"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Gamburger_rus)

@dp.message_handler(text="🍔 Oddiy Gamburger")
async def oddiy_gamburger(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/oddiy_gamburger.jpg")
    text = "Suvli tabiiy mol go'shti kotleti, pishgan yangi pomidor va tuzlangan bodringning yumaloq bo'laklari," \
           " Aysberg salatasi, yumshoq dumaloq bulochkada qaymoqli pomidor sousi bilan qizil shirin piyoz halqalari"
    await message.answer_photo(photo=photo, caption="Oddiy Gamburger Narxi: 17000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🍔 Простой гамбургер")
async def oddiy_gamburger(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/oddiy_gamburger.jpg")
    text = "Сочная натуральная котлета из говядины, круглые ломтики спелых свежих помидоров и соленые огурцы" \
            "Салат Айсберг, кольца сладкого красного лука со сливочно-томатным соусом на мягкой круглой булочке."
    await message.answer_photo(photo=photo, caption="Oddiy Gamburger Narxi: 17000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🧀🍔Cheese Burger")
async def cheese_burger(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/cheese_burger.jpg")
    text = "Shirali tabiiy mol go'shti kotleti, pishgan yangi pomidor va tuzlangan bodringning yumaloq bo'laklari, " \
           "aysberg salatasi, yumshoq dumaloq bulochkada qaymoqli pomidor sousi bilan bir bo'lak cheddar pishloqi"
    await message.answer_photo(photo=photo, caption="Cheese Burger Narxi: 24000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🍔 Double Burger")
async def double_burger(message: types.Message):
    text = "Tabiiy mol go'shtidan tayyorlangan ikkita suvli kotlet, pishgan yangi pomidor va tuzlangan bodringning" \
           " yumaloq bo'laklari, Aysberg salatasi, yumshoq bulochkada qaymoqli pomidor sousi bilan qizil shirin piyoz" \
           " halqalari"
    photo = InputFile(path_or_bytesio="./../evos_bots/dablburger.jpg")
    await message.answer_photo(photo=photo, caption="Double Burger Narxi: 33000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🍔🧀 Double Cheese Burger")
async def double_cheese(message: types.Message):
    text = "Tabiiy mol go'shtidan tayyorlangan ikkita suvli kotlet, pishgan yangi pomidor va tuzlangan bodringning" \
           " yumaloq bo'laklari, Aysberg salatasi, yumshoq dumaloq bulochkada qaymoqli pomidor souli ikki bo'lak" \
           " cheddar pishloqi"
    photo = InputFile(path_or_bytesio="./../evos_bots/double_cheese_burger.jpg")
    await message.answer_photo(photo=photo, caption="🍔🧀 Double Cheese Burger Narxi: 37000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🥪 Trendwich")
async def trendwich_handler(message: types.Message):
    photo = "https://cp.ectn.uz/files//0622/trend_wich.png"
    text = "Trendwich Turini tanlang: "
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_trendwich)


@dp.message_handler(text="🐔 Tovuqlik Trendwich")
async def tovuq_trendwich(message: types.Message):
    text = "Yumshoq tortillada xushbo'y sousda pishloq va pomidor bilan pishirilgan tovuq go'shti!"
    photo = "https://cp.ectn.uz/files//0622/trend_wich.png"
    await message.answer_photo(photo=photo, caption="Tovuqlik Trendwich Narxi: 24000")
    await message.answer(text=text)

@dp.message_handler(text="🥩 Go'shtlik Trendwich")
async def tovuq_trendwich(message: types.Message):
    text = "Yumshoq tortillada xushbo'y sousda pishloq va pomidor bilan pishirilgan tovuq go'shti!"
    photo = "https://cp.ectn.uz/files//trindwich_29_05_wb.png"
    await message.answer_photo(photo=photo, caption="Goshtlik Trendwich Narxi: 26000")
    await message.answer(text=text)

@dp.message_handler(text="🌮 Shaurma")
async def shaurma_menu(message: types.Message):
    text = "Shourma Turini Tanlang: "
    photo = InputFile(path_or_bytesio="./../evos_bots/shaurma_menu.jpg")
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Shaurma)

@dp.message_handler(text="🐔 Tovuq Go'shtlik Shaurma")
async def tovuq_shaurma(message: types.Message):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_shourma.jpg")
    text = "Qizil panjara qilingan tovuq go'shti, yangi bodring va suvli pomidor bo'laklari, tiniq chiplar," \
           " kunjut urug'lari bilan xushbo'y yarim doira shaklida yangi piyoz va o'tlar bilan sharqona pomidor sousi."
    await message.answer_photo(photo=photo, caption="Tovuqlik Shaurma Narxi: 24000 So'm", reply_markup=shourma_menu_tovuq)
    await message.answer(text=text)

@dp.message_handler(text="🥩 Mol Goshtlik Shaurma")
async def mol_goshti(message: types.Message):
    text = "Grilda pishirilgan mol go'shti, yangi bodring va suvli pomidorning shirali bo'laklari, qizarib pishgan" \
           " kartoshka chiplari, kunjut urug'lari bilan xushbo'y yarim doira shaklidagi bulochkada yangi piyoz va o'tlar" \
           " bilan sharqona pomidor sousi. Mini versiya - engil geril uchun juda mos keladi"
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiqmas_goshtlik_shourma.jpg")
    await message.answer_photo(photo=photo, caption="🥩 Mol Goshtlik Shaurma Narxi: 26000 So'm", reply_markup=shourma_menu_gosht)
    await message.answer(text=text)

@dp.message_handler(text="🐔 Tovuq Goshtlik Achchiq Shaurma")
async def tovuq_goshtlik_mini(mesage: types.Message):
    text = "Qizil panjara qilingan tovuq go'shti, yangi bodring va suvli pomidor bo'laklari, çıtır chipslar, kunjut" \
           " urug'lari bilan xushbo'y bulochkada piyoz bo'laklari bilan achchiq pomidor sousi."
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_tovuq_shouqma.jpg")
    await mesage.answer_photo(photo=photo, caption="🐔 Tovuq Go'shtlik Shourma Narxi: 24000 So'm", reply_markup=shourma_menu_tovuq_achchiq)
    await mesage.answer(text=text)

@dp.message_handler(text="🥩 Mol Goshtlik Achchiq Shaurma")
async def tovuq_goshtlik_mini(mesage: types.Message):
    text = "Achchiq pishirilgan mol go'shti, yangi bodring va suvli pomidor bo'laklari, qizarib pishgan kartoshka" \
           " chiplari, kunjut urug'lari bilan xushbo'y yarim doira shaklidagi bulochkada yangi piyoz va o'tlar bilan" \
           " achchiq pomidor sousi."
    photo = InputFile(path_or_bytesio="./../evos_bots/goshtlik_shourqma.jpg")
    await mesage.answer_photo(photo=photo, caption="🥩 Mol Go'shtlik Mini Shourma Narxi: 26000 So'm", reply_markup=shourma_menu_gosht_achchiq)
    await mesage.answer(text=text)

@dp.callback_query_handler(text="big_shaurma_gosht")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiqmas_goshtlik_shourma.jpg")
    text = "Big Shaurma Go'shtlik 26000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_shaurma_gosht")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiqmas_goshtlik_shourma.jpg")
    text = "Big Shaurma Go'shtlik 24000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_shaurma_gosht_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/goshtlik_shourqma.jpg")
    text = "Big Shaurma Go'shtlik Achchiq 26000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_shaurma_gosht_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/goshtlik_shourqma.jpg")
    text = "Mini Shaurma Go'shtlik Achchiq 17000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_shaurma_tovu_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_shourma.jpg")
    text = "Big Shaurma Tovuqlik Achchiq 26000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_shaurma_tovu")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_shourma.jpg")
    text = "Big Shaurma Tovuqlik 26000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_shaurma_tovu")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_shourma.jpg")
    text = "Big Shaurma Tovuqlik 22000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_shaurma_tovu_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_shourma.jpg")
    text = "Mini Shaurma Tovuqlik 17000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="big_shaurma_tovu_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_tovuq_shouqma.jpg.jpg")
    text = "Big Shaurma Tovuqlik Achchiq 26000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.callback_query_handler(text="mini_shaurma_tovu_achchiq")
async def big_shaurma_gosht(call: types.CallbackQuery):
    photo = InputFile(path_or_bytesio="./../evos_bots/achchiq_tovuq_shouqma.jpg.jpg")
    text = "Big Shaurma Tovuqlik Achchiq 17000 So'm"
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=plus_minus)

@dp.message_handler(text="🍗 Tovuq Sneki")
async def tovuq_snek(message: types.Message):
    text = "Snek Turini Tanlang: "
    photo ="https://cp.ectn.uz/files//0622/strips_iz_kurochki_evos.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Snek)

@dp.message_handler(text="🍗 Tovuqlik Oddiy Strips")
async def oddiy_snek(message: types.Message):
    text = "Tovuq Go'shtidan Tayyorlangan Strips"
    photo = "https://cp.ectn.uz/files//0622/strips_iz_kurochki_evos.png"
    await message.answer_photo(photo=photo, caption="Tovuqlik Stripslar Narxi: 19000 So'm")
    await message.answer(text=text)

@dp.message_handler(text="🥯 Smayliklar")
async def smaylik_strips(message: types.Message):
    text = "Xamir Va Kartoshka Pyuresi Va Tovuqdan Tayyorlangan Kulgichlik Stripslar"
    photo = "https://cp.ectn.uz/files//smiles_web(1).png"
    await message.answer_photo(photo=photo, caption="Kulgichlk Stripslar Narxi: 14000 So'm")
    await message.answer(text=text)

@dp.message_handler(text="🫔 Sab")
async def sab_menu(message: types.Message):
    text = "Sab Turini Tanlang: "
    photo = InputFile(path_or_bytesio="./../evos_bots/sab_menu.jpg")
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Sab_menu)

@dp.message_handler(text="🐔 Tovuq Go'shtlik Sab")
async def chicken_sab(message: types.Message):
    text = "Qizil Panjara Qilingan Tovuq Go'shti, Svejiy Pomidor va Bodring"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_sab.jpg")
    await message.answer_photo(photo=photo, caption="🐔 Tovuq Go'shtlik Sab Narxi: 17000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🥩 Mol Go'shtilik Sab")
async def mol_gushtli_sab(message:types.Message):
    text = "Shirali qovurilgan mol go'shti, yangi qizil piyoz halqalari, uzun mayin bulochkada tutunli barbekyu sousi"
    photo = InputFile(path_or_bytesio="./../evos_bots/goshtlik_sab.jpg")
    await message.answer_photo(photo=photo, caption="🥩 Mol Go'shtilik Sab Narxi: 19000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🧀 Tovuq Goshtlik Sirlik Sab")
async def sirlik_tovuq_sab(message: types.Message):
    text = "Tovuq Go'shtidan Tayyorlangan Sab Ichida Pishloq Ham Mavjud bo'ladi!"
    photo = InputFile(path_or_bytesio="./../evos_bots/tovuqlik_oishloqlik_sab.jpg")
    await message.answer_photo(photo=photo, caption="🧀 Tovuq Goshtlik Sirlik Sab Narxi: 22000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🥩 Mol Goshtlik Sirlik Sab")
async def sirlik_tovuq_sab(message: types.Message):
    text = "Mol Go'shtidan Tayyorlangan Sab Ichida Pishloq Ham Mavjud bo'ladi!"
    photo = InputFile(path_or_bytesio="./../evos_bots/goshtlik_pishloqlik_sab.jpg")
    await message.answer_photo(photo=photo, caption="🥩 Mol Goshtlik Sirlik Sab Narxi: 25000", reply_markup=plus_minus)
    await message.answer(text=text)

@dp.message_handler(text="🍟 Kartoshka Fri")
async def kartoshka_fri(message: types.Message):
    text = "Kartoshka Frini Turini Tanlang: "
    photo = "https://cp.ectn.uz/files//kartofel_derevenskiy_evos.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Fri)

@dp.message_handler(text="🍟 Mamlakat Uslubidagi Fri")
async def mamlakat_fri(message: types.Message):
    text = "Mamlakat Uslubidagi Shirin Kartoshka Fri!"
    photo = "https://cp.ectn.uz/files//kartofel_derevenskiy_evos.png"
    await message.answer_photo(photo=photo, caption="Mamlakat Uslubidagi Frilar 15000 So'm")
    await message.answer(text=text)

@dp.message_handler(text="🍟 Kartoshhka Fri")
async def kartofel(message: types.Message):
    text = "Kartoshkadan Tayyorlangan Kartoshka Fri!"
    photo = "https://cp.ectn.uz/files//kartofel_fri_evos.png"
    await message.answer_photo(photo=photo, caption="artoshka Frilar Narxi: 14000 So'm")
    await message.answer(text=text)

@dp.message_handler(text="🌭 Xot Dog")
async def hot_dog_menu(message: types.Message):
    text = "Xot-Dog Turini Tanlang: "
    photo = "https://cp.ectn.uz/files//web/hot_dog_kids.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_HotDog)

@dp.message_handler(text="🌭 Oddiy Xot-Dog")
async def oddiy_hot_dog(message: types.Message):
    photo = "https://cp.ectn.uz/files//0622/hot_dog_Baguette_evos.png"
    text = "Sosika, Bulochka, Ketchup, Mayonez va Hamda Eng Kerakli Suyuq Pishloq Mavjud!"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🌭🌭 Double Xot-Dog")
async def double_xot_dog(message: types.Message):
    text = "2 ta Sosika, Kattaroq Bulochka, Ketchup, Mayonez va Hamda Eng Kerakli Suyuq Pishloq Mavjud!"
    photo = "https://cp.ectn.uz/files//0622/dabl_hot_dog_Baguette_evos.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="👶🌭Bolalar Uchun Xot Dog")
async def bollaga_hot_dog_handler(message: types.Message):
    text = "Kanadalik kurka kolbasa, maydalangan piyoz kartoshkasi, yumshoq bulochkada pishloq sousi"
    photo = "https://cp.ectn.uz/files//web/hot_dog_kids.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🌭 Mini Xot Dog")
async def mini_hot_dog_handler(message: types.Message):
    text = "Kanadalik kurka kolbasa, maydalangan piyoz kartoshkasi, yumshoq bulochkada pishloq sousi"
    photo = "https://cp.ectn.uz/files//web/hot_dog_kids.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🥗 Salat,Non...")
async def salat_non_handler(message: types.Message):
    text = "Qo'shimcha Biron Narsa Tanlang: "
    photo = "https://cp.ectn.uz/files//salat_grecheskiy_web.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Salat_Menu)

@dp.message_handler(text="🍚 Guruch")
async def guruch_handler(message: types.Message):
    text = "Oq guruch va arpadan tayyorlangan mazali va foydali guruch"
    photo = "https://cp.ectn.uz/files//ris_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🥐 Non")
async def non_handler(message: types.Message):
    text = "YapYangi Shirin Yopgan Non"
    photo = "https://cp.ectn.uz/files//non_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🥗 Sezar Salat")
async def sezar_salat_hander(message: types.Message):
    text = "Xamirda qovurilgan tovuq bo'laklari, yangi pomidor, pishloq, sarimsoqli sarimsoqli krutonlar," \
           " Sezar qo'shimchasi bilan aysberg salatasi"
    photo = "https://cp.ectn.uz/files//salat_grecheskiy_web.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🥗 Oddiy Salat")
async def oddiy_salat(message: types.Message):
    text = "Limon sharbati va sharqona ziravorlar bilan yangi bodring va qizil karam"
    photo = "https://cp.ectn.uz/files//salat_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🥗 Yunon Salati")
async def yunon_salat_handler(message: types.Message):
    text = "Yangi pomidor va bodring, tort zaytun, achchiq yog'li sousli nozik Fetaxa pishloq. Sevimli" \
           " klassikalar yangi versiyada!"
    photo = "https://cp.ectn.uz/files//salat_grecheskiy_web.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍛 Souslar")
async def souslar_handler(message: types.Message):
    text = "Souslar Turini Tanlang"
    photo = "https://cp.ectn.uz/files//sladkiy_kisliy_08_wb.png"
    await message.answer_photo(photo=photo, caption=text, reply_markup=Evos_Sous_Menu)

@dp.message_handler(text="🍛 Shirin Nordon Sous 25 ml")
async def shirin_nordon_sous_handler(message: types.Message):
    text = "Kislo Sladkiy Holdagi 25 ml Lik Sous"
    photo = "https://cp.ectn.uz/files//barbekyu_08_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍛 Ketchup 25 ml")
async def shirin_nordon_sous_handler(message: types.Message):
    text = "Pomidordan Tayyorlangan 25 ml Lik Ketchup Sousi"
    photo = "https://cp.ectn.uz/files//Sauce_tomato_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍛 Mayonez Pishloqlik 25 ml")
async def shirin_nordon_sous_handler(message: types.Message):
    text = "Pishloqlik Mayonez 25 ml"
    photo = "https://cp.ectn.uz/files//sirniy_08_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍛 Barbekyu 25 ml")
async def shirin_nordon_sous_handler(message: types.Message):
    text = "Barbekyu Sousi 25 ml"
    photo = "https://cp.ectn.uz/files//barbekyu_08_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍱 Tayyor Nabor Setlar")
async def nabor_setlar_handler(message: types.Message):
    text = "Setlar Turini Tanlang: "
    photo = "https://cp.ectn.uz/files//donar_s_govyadinoy_evos.png"
    await message.answer_photo(photo=photo, caption=text, reply_markup=Evos_Set_Menu)

@dp.message_handler(text="🍱 Готовые наборы наборов")
async def nabor_setlar_handler(message: types.Message):
    text = "Setlar Turini Tanlang: "
    photo = "https://cp.ectn.uz/files//donar_s_govyadinoy_evos.png"
    await message.answer_photo(photo=photo, caption=text, reply_markup=Evos_Set_Menu_rus)

@dp.message_handler(text="🍱🥩 Mol Go'shtilik Donar Seti")
async def mol_gosht_se_handler(message: types.Message):
    text = "Mol Go'shtidan Tayyorlangan Set.Setda Kartoshka Fri, Salat, Gurusch va Ketchup Mavjud!"
    photo = "https://cp.ectn.uz/files//donar_s_govyadinoy_evos.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍱🥩 Донар из говядины сет")
async def mol_gosht_se_handler(message: types.Message):
    text = "Набор из говядины. В комплект входит картофель фри, салат, гурш и кетчуп!"
    photo = "https://cp.ectn.uz/files//donar_s_govyadinoy_evos.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍱🐔 Tovuq Go'shtilik Donar Seti")
async def tovuq_gosht_set(message: types.Message):
    text = "Tovuq Go'shtidan Tayyorlangan Set.Setda Kartoshka Fri, Salat, Gurusch va Ketchup Mavjud!"
    photo = "https://cp.ectn.uz/files//donar_s_kuricey_evos.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍱🐔 Куриный донар сет")
async def tovuq_gosht_set(message: types.Message):
    text = "Куриный сет: в набор входят картофель фри, салат, гурш и кетчуп!"
    photo = "https://cp.ectn.uz/files//donar_s_kuricey_evos.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍩 Shirinliklar")
async def shirinliklar_handler(message: types.Message):
    text = "Olmoqchi Bo'lgan Shirinligingizni Tanlang: "
    photo = "https://cp.ectn.uz/files//donat_klubnika_19_06_wb(1).png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Shirinliklar)

@dp.message_handler(text="🍩 Сладости")
async def shirinliklar_handler(message: types.Message):
    text = "Выберите сладость, которую хотите получить: "
    photo = "https://cp.ectn.uz/files//donat_klubnika_19_06_wb(1).png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Shirinliklar_rus)

@dp.message_handler(text="🍨 Medovik")
async def shirinliklar_handler(message: types.Message):
    text = "Smetana bilan asal tender shimgichni keki"
    photo = "https://cp.ectn.uz/files//medovik_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍨 Chizkeyk")
async def shirinliklar_handler(message: types.Message):
    text = "Krem pishloq kremi bilan vanil shimgichli kek"
    photo = "https://cp.ectn.uz/files//chizkeyk_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍩 Teshik Kulcha Shirinlik")
async def shirinliklar_handler(message: types.Message):
    text = "Qulupnay-qatiqli sirlangan yumshoq yumshoq donut"
    photo = "https://cp.ectn.uz/files//donat_klubnika_19_06_wb(1).png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)
    
@dp.message_handler(text="🍩 Teshik Kulcha Shirinlik Karamel")
async def shirinliklar_handler(message: types.Message):
    text = "Karamel sirida yumshoq nozik donut"
    photo = "https://cp.ectn.uz/files//donat_caramel_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍩 Донат ягодный")
async def shirinliklar_handler(message: types.Message):
    text = "Мягкий нежный донат в клубнично-йогуртовой глазури"
    photo = "https://cp.ectn.uz/files//donat_klubnika_19_06_wb(1).png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍩 Донат карамельный")
async def shirinliklar_handler(message: types.Message):
    text = "Мягкий нежный донат в карамельной глазури"
    photo = "https://cp.ectn.uz/files//donat_caramel_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍨 Чизкейк")
async def shirinliklar_handler(message: types.Message):
    text = "Ванильный бисквит с сырно-сливочным кремом"
    photo = "https://cp.ectn.uz/files//chizkeyk_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="🍨 Медовик")
async def shirinliklar_handler(message: types.Message):
    text = "Медовый мягкий бисквит со сметанным кремом"
    photo = "https://cp.ectn.uz/files//medovik_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text)

@dp.message_handler(text="☕ Issiq Ichimliklar")
async def issiq_ichimlik(message: types.Message):
    text = "Issiq Ichimlik Turini Tanlang: "
    photo = "https://cp.ectn.uz/files//tea_green_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Issiq_Ichimliklar)

@dp.message_handler(text="☕ Горячие напитки")
async def issiq_ichimlik(message: types.Message):
    text = "Выберите тип горячего напитка:"
    photo = "https://cp.ectn.uz/files//tea_green_19_06_wb.png"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Issiq_Ichimliklar_rus)

@dp.message_handler(text="🍵 Ko'k Choy")
async def kok_choy(message: types.Message):
    text = "Ko'k Choy"
    photo = "https://cp.ectn.uz/files//tea_qora_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍵 Чай зеленый")
async def kok_choy(message: types.Message):
    text = "Чай зеленый"
    photo = "https://cp.ectn.uz/files//tea_qora_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍵 Qora Choy")
async def qora_choy(message: types.Message):
    text = "Qora Choy Issiq"
    photo = "https://cp.ectn.uz/files//tea_qora_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍵 Чай черный")
async def qora_choy(message: types.Message):
    text = "Черный чай Горячий"
    photo = "https://cp.ectn.uz/files//tea_qora_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="☕ Kofee")
async def kofee_handler(message: types.Message):
    text = "Americano Kofee"
    photo = "https://cp.ectn.uz/files//web/amerikano.webp"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="☕ Коффе")
async def kofee_handler(message: types.Message):
    text = "Американо Кофе"
    photo = "https://cp.ectn.uz/files//web/amerikano.webp"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="☕ Latte Kofee")
async def latte_cofee(message: types.Message):
    text = "Latte Koffe"
    photo = "https://cp.ectn.uz/files//web/latte.webp"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="☕ Латте Коффе")
async def latte_cofee(message: types.Message):
    text = "Латте Кофе"
    photo = "https://cp.ectn.uz/files//web/latte.webp"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍵 Limon Choy Ko'k")
async def limon_choy(message: types.Message):
    text = "Limon Choy (Ko'k)"
    photo = "https://cp.ectn.uz/files//tea_lemon_green_19_06_wb.png"
    await message.answer_photo(photo=photo,caption=text)

@dp.message_handler(text="🍵 Чай зеленый с лимоном")
async def limon_choy(message: types.Message):
    text = "Чай зеленый с лимоном"
    photo = "https://cp.ectn.uz/files//tea_lemon_green_19_06_wb.png"
    await message.answer_photo(photo=photo,caption=text)

@dp.message_handler(text="🍵 Чай черный с лимоном")
async def qora_choy_handler(message: types.Message):
    text = "🍵 Чай черный с лимоном"
    photo = "https://cp.ectn.uz/files//tea_lemon_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍵 Limon Choy Qora")
async def limon_choy_qora_handler(message: types.Message):
    text = "Limon Choy(Qora)"
    photo = "https://cp.ectn.uz/files//tea_lemon_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍸 Muzdek Ichimliklar")
async def muzdek_ichimlik(message: types.Message):
    text = "Muzdek Ichimlik Turini Tanlang: "
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKP96iBzCPCjUAFCggqIF1T8a2VGkmJ_0foieuYvgZig&s"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Cold_Drinks)

@dp.message_handler(text="🍸 Ледяные напитки")
async def muzdek_ichimlik(message: types.Message):
    text = "Выберите тип ледяного напитка: "
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKP96iBzCPCjUAFCggqIF1T8a2VGkmJ_0foieuYvgZig&s"
    await message.answer_photo(photo=photo)
    await message.answer(text=text, reply_markup=Evos_Cold_Drinks_rus)

@dp.message_handler(text="🍷 Cola 1.5l")
async def cola_handler(message: types.Message):
    text = "Cola 1.5l"
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJc72Dl-mBhX8036lL2kAgRMEk97nS2VoJxw&usqp=CAU"
    await message.answer_photo(photo=photo, caption=text)
    
@dp.message_handler(text="🍷 Кола 1.5l")
async def cola_handler(message: types.Message):
    text = "Кола 1.5l"
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJc72Dl-mBhX8036lL2kAgRMEk97nS2VoJxw&usqp=CAU"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Пепси 1.5l")
async def pepsi_haandler(message: types.Message):
    text = "Пепси 1.5 l"
    photo = "https://cp.ectn.uz/files//0622/Pepsi_1.5.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Pepsi 1.5l")
async def pepsi_haandler(message: types.Message):
    text = "Pepsi 1.5 l"
    photo = "https://cp.ectn.uz/files//0622/Pepsi_1.5.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Fanta 1.5l")
async def fanta_handler(message: types.Message):
    text = "Fanta 1.5l"
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzwZojdsL9Y8QvPy3M5e9EcF-JSSHMi5V1tA&usqp=CAU"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Фанта 1.5l")
async def fanta_handler(message: types.Message):
    text = "Фанта 1.5l"
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzwZojdsL9Y8QvPy3M5e9EcF-JSSHMi5V1tA&usqp=CAU"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Bliss")
async def bliss_handler(message: types.Message):
    text = "Bliss"
    photo = "https://cp.ectn.uz/files//bliss_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

@dp.message_handler(text="🍷 Блисс")
async def bliss_handler(message: types.Message):
    text = "Блисс"
    photo = "https://cp.ectn.uz/files//bliss_19_06_wb.png"
    await message.answer_photo(photo=photo, caption=text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

