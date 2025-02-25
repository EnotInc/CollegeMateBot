import emoji

from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
    )


menu = ReplyKeyboardMarkup(keyboard=[
    #[KeyboardButton(text='Расписание на сегодня')],
    [KeyboardButton(text=emoji.emojize(':stopwatch: Время пар'))],
    [KeyboardButton(text= emoji.emojize(':clipboard: Расписание на эту неделю')), KeyboardButton(text=emoji.emojize(':calendar: Расписание на след. неделю'))],
    [KeyboardButton(text=emoji.emojize(':e-mail: Связаться с разрабом')), KeyboardButton(text=	emoji.emojize(':red_question_mark: информация о проекте'))],
    #[KeyboardButton(text='Поддерэать проект'), KeyboardButton(text='Сообщить об ошибке')]
], resize_keyboard=True, input_field_placeholder="Выбери что нужно", is_persistent=True)

coures_this = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='00'), InlineKeyboardButton(text='2-й', callback_data='01')],
    [InlineKeyboardButton(text='3-й', callback_data='02'), InlineKeyboardButton(text='4/5', callback_data='03')]
])

coures_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='10'), InlineKeyboardButton(text='2-й', callback_data='11')],
    [InlineKeyboardButton(text='3-й', callback_data='12'), InlineKeyboardButton(text='4/5', callback_data='13')]
])


back_to_courses = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_to_courses0')]
    ])

