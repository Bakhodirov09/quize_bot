from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import *
from utils.set_bot_commands import set_default_commands
from main.database_set import *

async def on_startup(dispatcher):
    await database.connect()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

async def on_shut_down(dispatcher):
    await database.disconnect()
    await on_shut_down_notify(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shut_down)