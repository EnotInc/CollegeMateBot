from aiogram import F, Router
from aiogram.types import Message, InputFile, FSInputFile

from parser import date_diff

import buttons as b
import keyboards as kb

rout_messages = Router()

beginning_date = '29.01.2018'
 

@rout_messages.message(F.text == b.TIME)
async def get_time(message:Message):
    await message.answer('№ 1 Время: 9:00 - 10:30 \
                         \n\n№ 2 Время: 10:50 - 11:35 \n& 11:55 - 12:40\
                         \n\n№ 3 Время: 13:00 - 14:30\
                         \n\n№ 4 Время: 14:50 - 16:20\
                         \n\n№ 5 Время: 16:30 - 18:00\
                         \n\n|\\_ _ _/|\
                         \n| 0 W 0|')

@rout_messages.message(F.text == b.THIS)
async def get_this_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_this)


@rout_messages.message(F.text == b.NEXT)
async def get_next_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_next)

@rout_messages.message(F.text == b.AUTO)
async def set_auto_scheduler(message: Message):
    await message.answer('Что вы хотели бы настроить?', reply_markup=kb.auto_settings)


@rout_messages.message(F.text == b.CANTEEN)
async def canteen_schedule(message: Message):
    msg = await message.answer('Ищу меню на сегодня\
                         \n\n|\\_ _ _/|\
                         \n| ^ w ^ |')
    try:
        day_of_week = date_diff(beginning_date)%7
        weeks_past = date_diff(beginning_date)//7    
        day_of_menu = day_of_week + weeks_past%2*6

        photo_path = f'canteen_menu/page_{day_of_menu}.jpeg'
        menu_photo = FSInputFile(photo_path)

        await message.answer_photo(photo=menu_photo)
        await msg.edit_text('Вот что сегодня в столовой\
                                \n\n|\\_ _ _/|\
                                \n|   . w . |  .,,,')

    except Exception as ex:
        print(ex)