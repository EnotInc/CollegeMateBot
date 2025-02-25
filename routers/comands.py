from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from routers.messages import get_this_week, get_next_week, get_time, about
from routers.callbacks import bug_report
from aiogram.fsm.context import FSMContext

import keyboards as kb

rout_commands = Router()


@rout_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, это бот способный облегчить твое пребывание в колледже.\
                         \nСдать БД я тебе, конечно, не помогу, но подкинуть рассписание или напомнить о начале пары - без проблем, просто выбери необходимый пункт в меню",
                            reply_markup=kb.menu)


@rout_commands.message(Command('get_this_week'))
async def get_this_week_cmd(message: Message):
    await get_this_week(message)


@rout_commands.message(Command('get_next_week'))
async def get_next_week_cmd(message: Message):
    await get_next_week(message)


@rout_commands.message(Command('get_time'))
async def get_time_cmd(message: Message):
    await get_time(message)


@rout_commands.message(Command('report'))
async def bug_report_cdm(message: Message, state: FSMContext):
    await bug_report(message, state)

@rout_commands.message(Command('about'))
async def about_cmd(message: Message):
    await about(message)

@rout_commands.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer('Вот список команд которые я могу выполнить:\
                         \n\n/help - выводит данный список \
                         \n/get_this_week - расписание на наделю\
                         \n/get_next_week - расписание на следю неделю\
                         \n/get_time - время начала и конца пар\
                         \n/report - оправить отчет о баге или предложние о доработке\
                         \n\nТак же каждая из этих команд может быть выполнена при помощи кнопок в меню')