from aiogram import F, Router
from aiogram.types import Message

import emoji
import keyboards as kb

rout_messages = Router()

time_array = ['9:00 - 10:30', '10:50 - 11:35 \n& 11:55 - 12:40', '13:00 - 14:30', '14:50 - 16:20', '16:30 - 18:00']

@rout_messages.message(F.text == emoji.emojize(':red_question_mark: информация о проекте'))
async def about(message:Message):
    await message.answer('Так, ну что я могу сказать о себе. Даже не знаю. Я тут просто для того что бы помочь тебе с расписанием в колледже. Подробнее можешь прочитать на странице гит хаба:\nhttps://github.com/EnotInc/CollegeMateBot')
 
@rout_messages.message(F.text == emoji.emojize(':stopwatch: Время пар'))
async def get_time(message:Message):
    for i in range(0, 5):
        await message.answer('№ ' +str(i+1)+ ' Время: ' + str(time_array[i]))

@rout_messages.message(F.text == emoji.emojize(":clipboard: Расписание на эту неделю"))
async def get_this_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_this)

@rout_messages.message(F.text == emoji.emojize(":calendar: Расписание на след. неделю"))
async def get_next_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_next)

@rout_messages.message(F.text == 'Сообщить об ошибке')
async def send_bug_report(message: Message):
    await message.answer('Данная функция пока недоступна. Если у вас что-то полшо не так, ну, ебать, анлаки')
