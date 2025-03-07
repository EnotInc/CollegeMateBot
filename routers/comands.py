from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import keyboards as kb

rout_commands = Router()


@rout_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Здарова, я Аскии, твой приятель из колледжа. Сдать бд я тебе, к сожаления, не помогу, но вот подкинуть расписание или напомнить о начале пар - без проблемм \
                         \n\n|\\_ _ _/|\
                         \n| ^ W ^|",
                            reply_markup=kb.menu)


@rout_commands.message(Command('about'))
async def about_cmd(message: Message):
    await message.answer('Еще раз привет, я кот Аскии. Нужен я для того что-бы помогать тебе с расписанием и некоторыми другими вещами по колледжу. Подробнее про то как я работаю можешь почитать тут:\nhttps://github.com/EnotInc/CollegeMateBot\
                         \n\n|\\_ _ _/|\
                         \n| o w o|',
                         reply_markup=kb.menu)


@rout_commands.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer('Вот список команд которые я могу выполнить:\
                         \n\n/help - выводит данный список \
                         \n/start - запуск/перезапуск бота\
                         \n/about - информация о боте\
                         \n\n|\\_ _ _/|\
                         \n| * w * |',
                         reply_markup=kb.menu)
