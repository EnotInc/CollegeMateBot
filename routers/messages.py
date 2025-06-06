from aiogram import F, Router
from aiogram.types import Message, FSInputFile

from canteen_menu.waiter import get_menu_page, menu_chedule_reactions
from backend_logic.ASCII_the_cat import cat

import keyboard_stuff.buttons as b
import keyboard_stuff.keyboards as kb

rout_messages = Router()

beginning_date = '03.04.2025'
 

@rout_messages.message(F.text == b.TIME)
async def get_time(message:Message):
    await message.answer('''№ 1 Время: 9:00 - 10:30
                         \n\n№ 2 Время: 10:50 - 11:35 & 11:55 - 12:40
                         \n\n№ 3 Время: 13:00 - 14:30
                         \n\n№ 4 Время: 14:50 - 16:20
                         \n\n№ 5 Время: 16:30 - 18:00''' + cat.OwO)


@rout_messages.message(F.text == b.THIS)
async def get_this_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_this)


@rout_messages.message(F.text == b.NEXT)
async def get_next_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_next)

@rout_messages.message(F.text == b.AUTO)
async def set_auto_scheduler(message: Message):
    await message.answer('Что вы хотели бы настроить?', reply_markup=kb.auto_settings)


@rout_messages.message(F.text == b.CANTEEN)
async def canteen_schedule(message: Message):
    msg = await message.answer('Ищу меню на сегодня' + cat.laptop)
    try:
        menu_page = get_menu_page()

        if menu_page == 5 or menu_page == 11:
            await msg.edit_text('Сегодня столовка закрыта'+cat.QwQ)
        else:
            photo_path = f'canteen_menu/page_{menu_page}.jpeg'
            menu_photo = FSInputFile(photo_path)

            await message.answer_photo(photo=menu_photo)
            await msg.edit_text(f'Вот что сегодня в столовой'+cat[menu_chedule_reactions[menu_page]])

    except Exception as ex:
        print(ex)
        await msg.edit_text('Сорян, что-то пошло не так'+cat.shame)