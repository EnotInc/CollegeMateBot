from aiogram import F, Router
from aiogram.types import Message, FSInputFile

from canteen_menu.waiter import get_menu_page, ascii_cat, menu_chedule_emotions

import buttons as b
import keyboards as kb

rout_messages = Router()

beginning_date = '03.04.2025'
 

@rout_messages.message(F.text == b.TIME)
async def get_time(message:Message):
    await message.answer('№ 1 Время: 9:00 - 10:30 \
                         \n\n№ 2 Время: 10:50 - 11:35 \n& 11:55 - 12:40\
                         \n\n№ 3 Время: 13:00 - 14:30\
                         \n\n№ 4 Время: 14:50 - 16:20\
                         \n\n№ 5 Время: 16:30 - 18:00\
                         \n\n|\\_ _ _/|\
                         \n| 0 W 0|')

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
    msg = await message.answer('Ищу меню на сегодня\
                         \n\n|\\_ _ _/|\
                         \n| ^ w ^ |')
    try:
        menu_page = get_menu_page()
        photo_path = f'canteen_menu/page_{menu_page}.jpeg'
        menu_photo = FSInputFile(photo_path)

        await message.answer_photo(photo=menu_photo)
        await msg.edit_text(f'Вот что сегодня в столовой\n\n{ascii_cat[menu_chedule_emotions[menu_page]]}')

    except Exception as ex:
        print(ex)
        await msg.edit_text('Сорян, что-то пошло не так\
                             \n\n/|_ _ _|\\   <--- *стыдно*')