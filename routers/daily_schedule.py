from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from buttons import TODAY
from parser import get_today_schedule

import emoji


rout_daily = Router()

all_groups = [
    {
        0 : '24ИНФ1-1',
        1 : '24ИНФ1-2',
        2 : '24ИНФ1-3',
        3 : '24ИНФ1-4',
        4 : '24ИС1-1веб',
        5 : '24ИС1-2веб',
        6 : '24ИС1-3веб',
        7 : '24ИС-11-\n1прогр',
        8 : '24ИС-11-\n2прогр',
        9 : '24СА1-1',
        10: '24СА1-2',
        11: '24СА1-3',
        12: '24СА-11'
    },

    {
        0 : '23ЗЕУ2-1Д',
        1 : '23ИНФ2-1',
        2 : '23ИНФ2-2',
        3 : '23ИНФ-21',
        4 : '23ИС2-1',
        5 : '23ИС2-2',
        6 : '23ИС-21',
        7 : '23ИС-21-1',
        8 : '23СА2-1',
        9 : '23СА2-2',
    },

    {
        0 : '22АП3-1',
        1 : '223ИО3-1Д',
        2 : '22ИНФ3-1',
        3 : '22ИНФ3-2',
        4 : '22ИС3-1',
        5 : '22ИС3-2',
        6 : '22ИС3-3Д',
        7 : '22ИС3-4Д',
        8 : '22ИС3-5Д',
        9 : '22ИС-31',
        10 : '22ИС-31Д',
        11 : '22СА3-1',
        12 : '22СА3-2Д',
    },

    {
        0 : '21АП4-1',
        1 : '21ИНФ4-1',
        2 : '21ИНФ-41 +\n20ИНФ5-1',
        3 : '21ИС4-1 +\n21ИС4-4Д',
        4 : '21ИС4-2 +\n21ИС4-5Д',
        5 : '21ИС4-3Д',
        6 : '21СА4-1 +\n21СА4-1Д',
    }
]

@rout_daily.message(F.text==TODAY)
async def send_courses(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        for i in range(4):
            builder.button(text=f'{i+1}-й', callback_data=f'course_{i}')
        builder.button(text=emoji.emojize('Омена :cross_mark:'), callback_data='c')
        builder.adjust(2)

        await message.answer('На каком курсе товя группа? \
                         \n\n|\\_ _ _/|\
                         \n| o w o|'
                         , reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await message.edit_text('Сорян, что-то пошло не так\
                             \n\n/|_ _ _|\\   <--- *стыдно*')


@rout_daily.callback_query(F.data.in_(['course_0', 'course_1', 'course_2', 'course_3']))
async def send_groups(callback: CallbackQuery):
    try:
        course = int(callback.data[-1:])
        builder = InlineKeyboardBuilder()
    
        for i in all_groups[course]:
            builder.button(text=all_groups[course][i], callback_data=f'c{course}g{i}')
        builder.button(text=emoji.emojize('Назад :left_arrow:'), callback_data='back')

        builder.adjust(2)
        await callback.message.edit_text('Расписане какой группы вам надо?\
                                     \n\n|\\_ _ _/|\
                                     \n| o w o|', 
                                     reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так\
                             \n\n/|_ _ _|\\   <--- *стыдно*')
    

@rout_daily.callback_query(F.data.regexp(r'c\d+g\d+'))
async def send_schedule(callback: CallbackQuery):
    try:
        await callback.message.edit_text('Ищу расписание\
                                     \n\n|\\_ _ _/|\
                                     \n|   - w - |  _/7')
    
        course = int(callback.data[1])
        groud_id = int(callback.data[3:])
        group = all_groups[course][groud_id]
        answer = get_today_schedule(course=course, group=group)
    
        await callback.message.edit_text(f'Вот расписание для группы "{group}"\
                                     \n\n|\\_ _ _/|\
                                     \n| o W o|')
        for i in answer:
            await callback.message.answer(emoji.emojize(i))
    
    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так\
                             \n\n/|_ _ _|\\   <--- *стыдно*')
        

@rout_daily.callback_query(F.data=='back')
async def send_courses(callback: CallbackQuery):
    try:
        builder = InlineKeyboardBuilder()
        for i in range(4):
            builder.button(text=f'{i+1}-й', callback_data=f'course_{i}')
        builder.button(text='Омена', callback_data='c')
        builder.adjust(2)

        await callback.message.edit_text('На каком курсе товя группа? \
                         \n\n|\\_ _ _/|\
                         \n| o w o|'
                         , reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так\
                             \n\n/|_ _ _|\\   <--- *стыдно*')
