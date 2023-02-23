from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp



@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer('hello!')