# from aiogram.dispatcher.handler import CancelHandler
# from aiogram.dispatcher.middlewares import BaseMiddleware
# from aiogram import types, Bot
#
# async def check(user_id, channel_id):
#     bot = Bot.get_current()
#     member = await bot.get_chat_member(user_id=user_id, chat_id=channel_id)
#     return member.is_chat_member()
#
# class Check_Sub(BaseMiddleware):
#     async def on_subscribe(self, update: types.Update, data: dict):
#         user_id = 0
#         if update.message.text:
#             user_id = update.message.chat.id
#         elif update.callback_query:
#             if update.callback_query.data == "check_subscription":
#                 return
#             user_id = update.callback_query.message.chat.id
#
#         checker = await check(user_id=user_id, channel_id=-1001517005880)
#         if checker:
#             return
#         else:
#             text = f"Kechirasiz Kanalga Obuna Boling."
#             await update.message.answer(text=text)
#             await CancelHandler()
