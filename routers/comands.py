from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import keyboards as kb

rout_commands = Router()

@rout_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, это бот способный облегчить твое пребывание в колледже.\n\
                         Сдать БД я тебе, конечно, не помогу, но подкинуть рассписание или напомнить о начале пары - без проблем, просто выбери необходимый пункт в меню",
                            reply_markup=kb.menu)