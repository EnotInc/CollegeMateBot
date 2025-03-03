from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from parser import get_link
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from buttons import CALL

import os
import emoji
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
        await callback.message.edit_text('Вот твое расписание\
                                         \n\n|\\_ _ _/|\
                                         \n| u w u|  .,,,')
        await callback.message.answer_document(link)
    except:
        await callback.message.edit_text('Сорян, я не нашел рассписание\nВозможно его еще не загрузили на сайт колледжа\
                                         \n\n|\\_ _ _/|\
                                         \n| T _ T |')


@rout_callbacks.callback_query(F.data.in_(['1', '2', '3', '0', 'c']))
async def get_this_week(callback: CallbackQuery):
    try:
        if callback.data != 'c':
            from auto_scheduler import add_user
            course = int(callback.data)
            try:
                topic = int(callback.message.message_thread_id)
            except:
                topic = None
            if add_user(user_chat_id=callback.message.chat.id, course=course, topic=topic):
                await callback.message.edit_text(f'Отлично, теперь по пятницам я смогу отправлять сюда расписане за {course + 1}-й курс\
                                                 \n\n|\\_ _ _/|\
                                                 \n| u w u|')
            else:
                await callback.message.edit_text('Вы уже подлючены к рассылке\
                                                 \n\n|\\_ _ _/|\
                                                 \n| o _ o |')
        else:
            await callback.message.edit_text('Запрос отменен')
    except Exception as ex:
        print(f'error at callback get_this_week:\n{ex}')
        await callback.message.edit_text('Сорян, что-то пошло не так\
                                         \n\n/|_ _ _|\\   <--- *стыдно*')


@rout_callbacks.callback_query(F.data.in_(['e1', 'e2', 'e3', 'e0', 'c']))
async def edit_this_week(callback: CallbackQuery):
    try:
        if callback.data != 'c':
            from auto_scheduler import edit_user
            course = int(callback.data[1])
            
            if edit_user(user_chat_id=callback.message.chat.id, new_course=course):
                await callback.message.edit_text(f'Отлично, курс обновлен на {course+1}-й\
                                                 \n\n|\\_ _ _/|\
                                                 \n| o w o|')
            else:
                await callback.message.edit_text('Вы не подключены к рассылке\
                                                 \n\n|\\_ _ _/|\
                                                 \n| o _ o |')
        else:
            await callback.message.edit_text('Запрос отменен', reply_markup=kb.menu)
    except Exception as ex:
        await callback.message.edit_text('Сорян, что-то пошло не так`\
                                         \n\n/|_ _ _|\\   <--- *стыдно*')
        print(ex)


@rout_callbacks.message(F.text == CALL)
async def bug_report(message: Message, state: FSMContext):
    await state.set_state(Report.bag)
    await message.answer('Опишите что у вас пошло не так, или напишите свое предложение о доработке бота\
                                       \n\n|\\_ _ _/|\
                                       \n| o w o|', reply_markup=kb.cancel)


@rout_callbacks.message(Report.bag)
async def send_repot(message: Message, state: FSMContext):
    try:
        await message.forward(os.getenv('DEVELOPER'))
        await message.reply(emoji.emojize("Я передал ваше сообщение разработчику. Спасибо за помощь в развитии пректа\
                                          \n\n|\\_ _ _/|\
                                          \n| o w o|:thumbs_up:"), reply_markup=kb.menu)
        await state.clear()
    except Exception as ex:
        await message.answer('Так, у меня что-то cломалось и отправить озыв не удалось\nПрошу прощения!\
                             \n\n/|_ _ _|\\   <--- *стыдно*', reply_markup=kb.menu)
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


@rout_callbacks.callback_query(F.data == 'edit')
async def edit_user_for_chesuler(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите новый курс', reply_markup=kb.edit_auto_courses)


@rout_callbacks.callback_query(F.data == 'yes')
async def delete_user_finally(callback: CallbackQuery):
    try:
        from auto_scheduler import delete_user
        delete_user(callback.message.chat.id)
        await callback.message.edit_text('Рассылка оменена\
                                         \n\n|\\_ _ _/|\
                                         \n| U _ U |')
    except Exception as ex:
        await callback.message.edit_text('Что-то пошло не так\
                                         \n\n./|_ _ _|\\   <--- *стыдно*')


@rout_callbacks.callback_query(F.data == 'no')
async def cancel_delete_user(callback: CallbackQuery):
    await callback.message.edit_text('Что бы вы хотели настроить?\
                                     \n\n|\\_ _ _/|\
                                     \n| o w o|', reply_markup=kb.auto_settings) 