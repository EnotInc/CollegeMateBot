import buttons as b

from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
    )


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=b.TIME)],
    [KeyboardButton(text=b.THIS), KeyboardButton(text=b.NEXT)],
    [KeyboardButton(text=b.CALL), KeyboardButton(text=b.ABOUT)],
    [KeyboardButton(text=b.HELP)],
], resize_keyboard=True, input_field_placeholder="Выбери что нужно", is_persistent=True, one_time_keyboard=False)


coures_this = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='00'), InlineKeyboardButton(text='2-й', callback_data='01')],
    [InlineKeyboardButton(text='3-й', callback_data='02'), InlineKeyboardButton(text='4/5', callback_data='03')]
])


coures_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й', callback_data='10'), InlineKeyboardButton(text='2-й', callback_data='11')],
    [InlineKeyboardButton(text='3-й', callback_data='12'), InlineKeyboardButton(text='4/5', callback_data='13')]
])


cancel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel')]
])
