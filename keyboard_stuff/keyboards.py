import keyboard_stuff.buttons as b
import emoji

from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
    )


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=b.AUTO), KeyboardButton(text=b.TODAY)],
    [KeyboardButton(text=b.THIS), KeyboardButton(text=b.NEXT)],
    [KeyboardButton(text=b.TIME), KeyboardButton(text=b.CALL), KeyboardButton(text=b.CANTEEN)]
], resize_keyboard=True, input_field_placeholder='^ w ^', one_time_keyboard=False)


coures_this = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='00'), InlineKeyboardButton(text='2-й', callback_data='01')],
    [InlineKeyboardButton(text='3-й', callback_data='02'), InlineKeyboardButton(text='4/5', callback_data='03')]
])


coures_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='10'), InlineKeyboardButton(text='2-й', callback_data='11')],
    [InlineKeyboardButton(text='3-й', callback_data='12'), InlineKeyboardButton(text='4/5', callback_data='13')]
])


auto_courses = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='0'), InlineKeyboardButton(text='2-й', callback_data='1')],
    [InlineKeyboardButton(text='3-й', callback_data='2'), InlineKeyboardButton(text='4/5', callback_data='3')],
    [InlineKeyboardButton(text='Отмена', callback_data='c')]
])


edit_auto_courses = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='e0'), InlineKeyboardButton(text='2-й', callback_data='e1')],
    [InlineKeyboardButton(text='3-й', callback_data='e2'), InlineKeyboardButton(text='4/5', callback_data='e3')],
    [InlineKeyboardButton(text='Отмена', callback_data='c')]
])


cancel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
])


auto_settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=emoji.emojize('Подключить :check_mark_button:'), callback_data='add')],
    [InlineKeyboardButton(text=emoji.emojize('Изменить курс :counterclockwise_arrows_button:'), callback_data='edit')],
    [InlineKeyboardButton(text=emoji.emojize('Отключить :cross_mark:'), callback_data='delete')],
    [InlineKeyboardButton(text='Отмена', callback_data='c')]
])


are_you_shure = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=emoji.emojize('Да'), callback_data='yes'),  InlineKeyboardButton(text=emoji.emojize('Нет'), callback_data='no')]
])