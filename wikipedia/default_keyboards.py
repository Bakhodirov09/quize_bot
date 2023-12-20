from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

select_lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek Tili"),
            KeyboardButton(text="🇷🇺 Русский Язык")
        ],
    ], resize_keyboard=True
)



send_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon Raqamingizni Jo'natish", request_contact=True)
        ]
    ],resize_keyboard=True
)

send_phone_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Отправьте свой номер телефона", request_contact=True)
        ]
    ],resize_keyboard=True
)

send_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Telefon Joylashuvingizni Jo'natish", request_location=True)
        ]
    ],resize_keyboard=True
)

send_location_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Отправьте свой Локатсия", request_location=True)
        ]
    ],resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Bellissimo"),
            KeyboardButton(text="🌯 Evos"),
        ],
        [
            KeyboardButton(text="🌯 Oqtepa Lavash"),
            KeyboardButton(text="🍔 Feed Up")
        ],
        [
            KeyboardButton(text="⚙️ Tilni O'zgartirish / Изменить язык")
        ],
    ], resize_keyboard=True
)

main_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Беллиссимо"),
            KeyboardButton(text="🌯 Эвос"),
        ],
        [
            KeyboardButton(text="🌯 Октепа Лаваш"),
            KeyboardButton(text="🍔 Фид Ап")
        ],
        [
            KeyboardButton(text="⚙️ Изменить язык / Tilni O'zgartirish")
        ],
    ], resize_keyboard=True
)

bellissimo_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Pitsa"),
            KeyboardButton(text="🍹 Ichimlik"),
        ],
        [
            KeyboardButton(text="Dust"),
            KeyboardButton(text="Inferno"),
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ]
    ], resize_keyboard=True
)

bellissimo_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕Пицца"),
            KeyboardButton(text="🍹 Напиток"),
        ],
        [
            KeyboardButton(text="Dust"),
            KeyboardButton(text="Inferno"),
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ]
    ], resize_keyboard=True
)

bellissimo_pizza_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Tovuqli Donar (New)"),
            KeyboardButton(text="🍕🧀 Pishloqli Pizza")
        ],
        [
            KeyboardButton(text="🍕 Go'shtlik Miks"),
            KeyboardButton(text="🍕 Donar Pizza")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True

)

bellissimo_pizza_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍕 Куриный Донар (Новый)"),
            KeyboardButton(text="🍕 Пицца с сыром")
        ],
        [
            KeyboardButton(text="🍕 Мясной микс"),
            KeyboardButton(text="🍕 Донер Пицца")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True

)

Evos_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌯 Lavash"),
            KeyboardButton(text="🍔 Gamburger"),
        ],
        [
            KeyboardButton(text="🥪 Trendwich"),
            KeyboardButton(text="🍗 Tovuq Sneki"),
        ],
        [
            KeyboardButton(text="🌮 Shaurma"),
            KeyboardButton(text="🫔 Sab")
        ],
        [
            KeyboardButton(text="🍟 Kartoshka Fri"),
            KeyboardButton(text="🌭 Xot Dog")
        ],
        [
            KeyboardButton(text="🥗 Salat,Non..."),
            KeyboardButton(text="🍛 Souslar")
        ],
        [
            KeyboardButton(text="🍱 Tayyor Nabor Setlar"),
            KeyboardButton(text="🍩 Shirinliklar")
        ],
        [
            KeyboardButton(text="☕ Issiq Ichimliklar"),
            KeyboardButton(text="🍸 Muzdek Ichimliklar")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ]
    ], resize_keyboard=True
)

Evos_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌯 Лаваш"),
            KeyboardButton(text="🍔 Гамбургер"),
        ],
        [
            KeyboardButton(text="🥪 Трендвич"),
            KeyboardButton(text="🍗 Снэки"),
        ],
        [
            KeyboardButton(text="🌮 Шаурма"),
            KeyboardButton(text="🫔 Саб")
        ],
        [
            KeyboardButton(text="🍟 Картофель фри"),
            KeyboardButton(text="🌭 Хот-дог")
        ],
        [
            KeyboardButton(text="🥗 Салат, хлеб..."),
            KeyboardButton(text="🍛 Соусы")
        ],
        [
            KeyboardButton(text="🍱 Готовые наборы наборов"),
            KeyboardButton(text="🍩 Сладости")
        ],
        [
            KeyboardButton(text="☕ Горячие напитки"),
            KeyboardButton(text="🍸 Ледяные напитки")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ]
    ], resize_keyboard=True
)

Evos_lavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Tovuqlik Lavash"),
            KeyboardButton(text="🧀🐔 Sirlik Tovuqlik Lavash"),
        ],
        [
            KeyboardButton(text="🧀🥩 Sirlik Go'shtlik Lavash"),
            KeyboardButton(text="🐔 Achchiq Tovuqlik Lavash"),
        ],
        [
            KeyboardButton(text="🥩 Achchiq Go'shtlik Lavash"),
            KeyboardButton(text="🌯 Fitter")
        ],
        [
            KeyboardButton(text="🥩 Go'shtlik Lavash")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ]
    ], resize_keyboard=True
)

Evos_lavash_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Куриный лаваш"),
            KeyboardButton(text="🧀🐔 Сырный куриный лаваш"),
        ],
        [
            KeyboardButton(text="🧀🥩 Сыр Мясной Лаваш"),
            KeyboardButton(text="🐔 Острый куриный лаваш"),
        ],
        [
            KeyboardButton(text="🥩 Острый мясной лаваш"),
            KeyboardButton(text="🌯 Фиттер")
        ],
        [
            KeyboardButton(text="🥩 Мясной лаваш")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ]
    ], resize_keyboard=True
)

Evos_Gamburger = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍔 Oddiy Gamburger"),
            KeyboardButton(text="🧀🍔Cheese Burger")
        ],
        [
            KeyboardButton(text="🍔 Double Burger"),
            KeyboardButton(text="🍔🧀 Double Cheese Burger")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Gamburger_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍔 Простой гамбургер"),
            KeyboardButton(text="🧀🍔 Чизбургер")
        ],
        [
            KeyboardButton(text="🍔 Двойной бургер"),
            KeyboardButton(text="🍔🧀 Двойной чизбургер")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_trendwich = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Tovuqlik Trendwich"),
            KeyboardButton(text="🥩 Go'shtlik Trendwich")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Shaurma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Tovuq Go'shtlik Shaurma"),
            KeyboardButton(text="🥩 Mol Goshtlik Shaurma")
        ],
        [
            KeyboardButton(text="🐔 Tovuq Goshtlik Achchiq Shaurma"),
            KeyboardButton(text="🥩 Mol Goshtlik Achchiq Shaurma")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Snek = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍗 Tovuqlik Oddiy Strips"),
            KeyboardButton(text="🥯 Smayliklar")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Sab_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Tovuq Go'shtlik Sab"),
            KeyboardButton(text="🥩 Mol Go'shtilik Sab")
        ],
        [
            KeyboardButton(text="🧀 Tovuq Goshtlik Sirlik Sab"),
            KeyboardButton(text="🥩 Mol Goshtlik Sirlik Sab")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Sab_menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🐔 Куриное мясо Саб"),
            KeyboardButton(text="🥩 Говяжий Саб")
        ],
        [
            KeyboardButton(text="🧀 Курица Мясо Сыр Сб"),
            KeyboardButton(text="🥩 Говядина Мясо Сыр Саб")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Fri = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍟 Mamlakat Uslubidagi Fri"),
            KeyboardButton(text="🍟 Kartoshhka Fri")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Fri_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍟 Картофель по-деревенски"),
            KeyboardButton(text="🍟 Картофель фри")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_HotDog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌭 Oddiy Xot-Dog"),
            KeyboardButton(text="🌭🌭 Double Xot-Dog")
        ],
        [
            KeyboardButton(text="👶🌭 Bolalar Uchun Xot Dog"),
            KeyboardButton(text="🌭 Mini Xot Dog")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_HotDog_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌭 Хот-дог"),
            KeyboardButton(text="🌭🌭 Double Хот-дог")
        ],
        [
            KeyboardButton(text="👶🌭 Хот-дог для детей"),
            KeyboardButton(text="🌭 Мини-хот-дог")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Salat_Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍚 Guruch"),
            KeyboardButton(text="🥐 Non")
        ],
        [
            KeyboardButton(text="🥗 Sezar Salat"),
            KeyboardButton(text="🥗 Oddiy Salat")
        ],
        [
            KeyboardButton(text="🥗 Yunon Salati")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Salat_Menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍚 Рис"),
            KeyboardButton(text="🥐 Хлеб")
        ],
        [
            KeyboardButton(text="🥗 Салат Цезарь"),
            KeyboardButton(text="🥗 Салат")
        ],
        [
            KeyboardButton(text="🥗 Греческий салат")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Sous_Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛 Shirin Nordon Sous 25 ml"),
            KeyboardButton(text="🍛 Ketchup 25 ml")
        ],
        [
            KeyboardButton(text="🍛 Mayonez Pishloqlik 25 ml"),
            KeyboardButton(text="🍛 Barbekyu 25 ml")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Sous_Menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛 Кисло-сладкий соус 25 мл"),
            KeyboardButton(text="🍛 Томатный кетчуп 25 мл")
        ],
        [
            KeyboardButton(text="🍛 Майонезно-сырный соус 25 мл"),
            KeyboardButton(text="🍛 Барбекю 25 мл")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Set_Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍱🥩 Mol Go'shtilik Donar Seti"),
            KeyboardButton(text="🍱🐔 Tovuq Go'shtilik Donar Seti")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Set_Menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍱🥩 Донар из говядины сет"),
            KeyboardButton(text="🍱🐔 Куриный донар сет")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Shirinliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍨 Medovik"),
            KeyboardButton(text="🍨 Chizkeyk")
        ],
        [
            KeyboardButton(text="🍩 Teshik Kulcha Shirinlik"),
            KeyboardButton(text="🍩 Teshik Kulcha Shirinlik Karamel")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Shirinliklar_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍨 Медовик"),
            KeyboardButton(text="🍨 Чизкейк")
        ],
        [
            KeyboardButton(text="🍩 Донат ягодный"),
            KeyboardButton(text="🍩 Донат карамельный")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Issiq_Ichimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍵 Ko'k Choy"),
            KeyboardButton(text="🍵 Qora Choy")
        ],
        [
            KeyboardButton(text="☕ Kofee"),
            KeyboardButton(text="☕ Latte Kofee")
        ],
        [
            KeyboardButton(text="🍵 Limon Choy Ko'k"),
            KeyboardButton(text="🍵 Limon Choy Qora")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Issiq_Ichimliklar_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍵 Чай зеленый"),
            KeyboardButton(text="🍵 Чай черный")
        ],
        [
            KeyboardButton(text="☕ Коффе"),
            KeyboardButton(text="☕ Латте Коффе")
        ],
        [
            KeyboardButton(text="🍵 Чай зеленый с лимоном"),
            KeyboardButton(text="🍵 Чай черный с лимоном")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)

Evos_Cold_Drinks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍷 Cola 1.5l"),
            KeyboardButton(text="🍷 Pepsi 1.5l")
        ],
        [
            KeyboardButton(text="🍷 Fanta 1.5l"),
            KeyboardButton(text="🍷 Bliss")
        ],
        [
            KeyboardButton(text="🏠 Asosiy Menu")
        ],
    ], resize_keyboard=True
)

Evos_Cold_Drinks_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍷 Кола 1.5l"),
            KeyboardButton(text="🍷 Пепси 1.5l")
        ],
        [
            KeyboardButton(text="🍷 Фанта 1.5l"),
            KeyboardButton(text="🍷 Блисс")
        ],
        [
            KeyboardButton(text="🏠 Главное меню")
        ],
    ], resize_keyboard=True
)
