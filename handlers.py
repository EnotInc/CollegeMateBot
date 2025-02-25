from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from parser import get_link, get_schedule_pdf
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import os
import emoji
import keyboards as kb

time_array = ['9:00 - 10:30', '10:50 - 11:35 & 11:55 - 12:40', '13:00 - 14:30', '14:50 - 16:20', '16:30 - 18:00']
router = Router()

class Report(StatesGroup):
    bag = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, это бот способный облегчить твое прибывание в колледже.\n\
                         Сдать БД я тебе, конечно, не помогу, но подкинуть рассписание или напомнить о начале пары - без проблем, просто выбери необходимый пункт в меню",
                            reply_markup=kb.menu)

@router.message(F.text == emoji.emojize(':e-mail: Связаться с разрабом'))
async def bug_report(message: Message, state: FSMContext):
    await state.set_state(Report.bag)
    await message.answer('Опишите что у вас пошло не так, или напишите свое предложение о доработке бота')

@router.message(Report.bag)
async def send_repot(message: Message, state: FSMContext):
    await message.forward(os.getenv('DEVELOPER'))
    await message.answer("Я передал ваше сообщение разработчику.\nСпасибо за помощь в развитии пректа!")
    await state.clear()

@router.message(F.text == emoji.emojize(':red_question_mark: информация о проекте'))
async def about(message:Message):
    await message.answer('Так, ну что я могу сказать о себе. Даже не знаю. Я тут просто для того что бы помочь тебе с расписанием в колледже. Подробнее можешь прочитать на странице гит хаба:\nhttps://github.com/EnotInc/CollegeMateBot')

@router.message(F.text == 'Расписание на сегодня')
async def get_today(message:Message):
    await message.answer("Ищу твое рассписсание")
    get_schedule_pdf()
    for i in range(0, 5):
        await message.answer('№ ' +str(i+1)+ ' - ' + ''
                                #'\nВ кабинете: ' + ''
                                #'\nПреподаватель: ' + ''
                                '\nВремя: ' + str(time_array[i]))
        
@router.message(F.text == emoji.emojize(':stopwatch: Время пар'))
async def get_today(message:Message):
    for i in range(0, 5):
        await message.answer('№ ' +str(i+1)+ ' Время: ' + str(time_array[i]))

@router.message(F.text == emoji.emojize(":clipboard: Расписание на эту неделю"))
async def get_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_this)

@router.message(F.text == emoji.emojize(":calendar: Расписание на след. неделю"))
async def get_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_next)


@router.message(F.text == 'Сообщить об ошибке')
async def send_bug_report(message: Message):
    await message.answer('Данная функция пока недоступна. Если у вас что-то полшо не так, ну, ебать, анлаки')

@router.callback_query(F.data.in_(['00', '01', '02', '03', '10', '11', '12', '13']))
async def get_this_week(callback: CallbackQuery):
    try:
        course = int(callback.data[1])
        week = int(callback.data[0])
        link = get_link(course=course, week=week)
        await callback.message.edit_text('Ваше Расписание:')
        await callback.message.answer_document(link)
    except:
        await callback.message.edit_text('Сорян, я не нашел рассписание :(\nЧто-то пошло не так')
