from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from parser import get_link 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from buttons import CALL

import os
import keyboards as kb


rout_callbacks = Router()

class Report(StatesGroup):
    bag = State()

class cheduleInit(StatesGroup):
    init = State()

@rout_callbacks.callback_query(F.data.in_(['00', '01', '02', '03', '10', '11', '12', '13']))
async def get_this_week(callback: CallbackQuery):
    try:
        course = int(callback.data[1])
        week = int(callback.data[0])
        link = get_link(course=course, week=week)
        await callback.message.edit_text('Ваше Расписание:')
        await callback.message.answer_document(link)
    except:
        await callback.message.edit_text('Сорян, я не нашел рассписание :(\nВозможно его еще не загрузили на сайт колледжа')


@rout_callbacks.callback_query(F.data.in_(['1', '2', '3', '0', 'c']))
async def get_this_week(callback: CallbackQuery):
    try:
        if callback.data != 'c':
            from auto_scheduler import add_user
            course = int(callback.data)
            
            if add_user(user_chat_id=callback.message.chat.id, course=course):
                await callback.message.edit_text(f'Отлично, теперь по пятницам я смогу отправлять сюда расписане за {course + 1}-й курс')
            else:
                await callback.message.edit_text('Вы уже подлючены к рассылке')
        else:
            await callback.message.edit_text('Запрос отменен', reply_markup=None)
    except Exception as ex:
        await callback.message.edit_text('Сорян, что-то пошло не так :|')
        print(ex)


@rout_callbacks.message(F.text == CALL)
async def bug_report(message: Message, state: FSMContext):
    await state.set_state(Report.bag)
    await message.answer('Опишите что у вас пошло не так, или напишите свое предложение о доработке бота', reply_markup=kb.cancel)


@rout_callbacks.message(Report.bag)
async def send_repot(message: Message, state: FSMContext):
    try:
        await message.forward(os.getenv('DEVELOPER'))
        await message.reply("Я передал ваше сообщение разработчику.\nСпасибо за помощь в развитии пректа!", reply_markup=kb.menu)
        await state.clear()
    except Exception as ex:
        await message.answer('Так, у меня что-то cломалось и отправить озыв не удалось\nПрошу прощения!', reply_markup=None)
        print(ex)


@rout_callbacks.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text('Запрос отменен', reply_markup=None)
    

@rout_callbacks.callback_query(F.data == 'add')
async def add_user_for_scheduler(callback: CallbackQuery):
    await callback.message.edit_text('Ты на каком курсе сейчас?', reply_markup=kb.auto_courses) 


@rout_callbacks.callback_query(F.data == 'delete')
async def delete_user_for_scheduler(callback: CallbackQuery):
    await callback.message.edit_text(text='Вы уверены что хотите отказаться от рассылки?', reply_markup=kb.are_you_shure)


@rout_callbacks.callback_query(F.data == 'yes')
async def delete_user_finally(callback: CallbackQuery):
    try:
        from auto_scheduler import delete_user
        delete_user(callback.message.chat.id)
        await callback.message.edit_text('Рассылка оменена')
    except Exception as ex:
        await callback.message.edit_text('Что-то пошло не так')


@rout_callbacks.callback_query(F.data == 'no')
async def cancel_delete_user(callback: CallbackQuery):
    await callback.message.edit_text('Что бы вы хотели настроить?', reply_markup=kb.auto_settings) 