from aiogram import F, Router
from aiogram.types import Message

import buttons as b
import keyboards as kb


rout_messages = Router()


time_array = ['9:00 - 10:30', '10:50 - 11:35 & 11:55 - 12:40', '13:00 - 14:30', '14:50 - 16:20', '16:30 - 18:00']


@rout_messages.message(F.text == b.ABOUT)
async def about(message:Message):
    await message.answer('Еще раз привет, я кот Аскии. Нужен я для того что-бы помогать тебе с расписанием и некоторыми другими вещами по колледжу. Подробнее про то как я работаю можешь почитать тут:\nhttps://github.com/EnotInc/CollegeMateBot\
                         \n\n|\\_ _ _/|\
                         \n| o u o |')
 

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