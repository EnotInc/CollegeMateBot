from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from backend_logic.ASCII_the_cat import cat
from keyboard_stuff.buttons import TODAY
from backend_logic.parser import get_today_schedule

import emoji

rout_daily = Router()


@rout_daily.message(F.text==TODAY)
async def send_courses(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        for i in range(4):
            builder.button(text=f'{i+1}-й', callback_data=f'course_{i}')
        builder.button(text=emoji.emojize('Омена :cross_mark:'), callback_data='c')
        builder.adjust(2)

        await message.answer('На каком курсе товя группа?'+cat.owo, reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await message.edit_text('Сорян, что-то пошло не так'+cat.shame)


@rout_daily.callback_query(F.data.in_(['course_0', 'course_1', 'course_2', 'course_3']))
async def send_groups(callback: CallbackQuery):
    try:
        course = int(callback.data[-1:])
        builder = InlineKeyboardBuilder()

        from backend_logic.schedule_constructor import get_groups
        groups=get_groups(course=course)

        for i in groups:
            builder.button(text=i, callback_data=f'c{course}g{i}')

        builder.button(text=emoji.emojize('Назад :left_arrow:'), callback_data='back')

        builder.adjust(2)
        await callback.message.edit_text('Расписане какой группы вам надо?'+cat.owo, reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так'+cat.shame)


@rout_daily.callback_query(F.data.regexp(r'c\d+g\d+'))
async def send_schedule(callback: CallbackQuery):
    try:
        await callback.message.edit_text('Ищу расписание'+cat.laptop) 
        course = callback.data[1]
        group = callback.data[3:]
        answer = get_today_schedule(course=course, group=group)
        
        await callback.message.edit_text(f'Вот расписание для группы "{group}"'+cat.schedule)

        for i in answer:
            await callback.message.answer(emoji.emojize(i))
    
    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так'+cat.shame) 


@rout_daily.callback_query(F.data=='back')
async def send_courses(callback: CallbackQuery):
    try:
        builder = InlineKeyboardBuilder()
        for i in range(4):
            builder.button(text=f'{i+1}-й', callback_data=f'course_{i}')
        builder.button(text='Омена', callback_data='c')
        builder.adjust(2)

        await callback.message.edit_text('На каком курсе товя группа?'+cat.owo, reply_markup=builder.as_markup())

    except Exception as ex:
        print(ex)
        await callback.message.edit_text('Сорян, что-то пошло не так'+cat.shame)