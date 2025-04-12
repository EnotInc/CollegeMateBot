from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from ASCII_the_cat import cat

import keyboards as kb

rout_commands = Router()


@rout_commands.message(CommandStart())
async def cmd_start(message: Message):
    #await message.answer(text=f"Здарова, я Аскии, твой приятель из колледжа. Сдать бд я тебе, к сожаления, не помогу, но вот подкинуть расписание или напомнить о начале пар - без проблемм{ascii_cat['owo']}",reply_markup=kb.menu)
    await message.answer(text="Здарова, я Аскии, твой приятель из колледжа. Сдать бд я тебе, к сожаления, не помогу, но вот подкинуть расписание или напомнить о начале пар - без проблемм"+cat.hello, reply_markup=kb.menu)


async def help_cmd(message: Message):
    await message.answer('''Вот список команд которые я могу выполнить:
                         \n\n/help - выводит данный список 
                         \n/start - запуск/перезапуск бота
                         \n/about - информация о боте'''+cat.AwA, 
                         reply_markup=kb.menu)


@rout_commands.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer('''*1\. Как начать?*
Нажмите кнопку _«Старт»_ если вы запускаете бота в первые или введите /start если уже пользовались ботом и/или хотите перезапустить его

*2\. Основные команды*
\- /help — руководство пользователя
\- /start — запуск/перезапуск бота
                        
*3\. Как работает рассылка*
После нажатия кнопку настроить рассылку в меню и выбора курса бот начинает присылать расписание:
    \- _В личных сообщениях_ — сразу в ваш чат с ботом
    \- _В групповом чате_ — если у бота есть права отправлять сообщения
    \- _В конкретном треде_ — рассылка работает конкретно в том треде, в котором была включена данная функция

Расписание на следующую неделю отправляется ботом в пятницу в 12:40 по Московскому времени

Чтобы остановить рассылку используете кнопку _настроить рассылку_ и выберите пункт оказаться

*4\. Частые проблемы*
\- _«Бот не отвечает»_ — проверьте, не заблокировали ли вы его \(напишите /start для перезапуска бота\)
\- Сообщение _«Что\-то пошло не так»_ — произошла ошибка в работе бота\. Можете оставить Отзыв разработчику с описанием условий, при которых произошла ошибка 
\- _«Рассылка приходит не туда»_ — отпишитесь и подпишитесь снова в нужном чате
\- _«Отзыв не был отправлен»_ — функция _Отзыв_ работает только в личном чате с ботом\. Проверьте что вы не пытаетесь отправить отзыв из группового чата

*5\. Контакты поддержки*
По вопросам и ошибкам можете воспользоваться функцией _Отзыв_, либо лично связаться с [разработчиком](https://t.me/BotEnot66)
''', reply_markup=kb.menu, parse_mode='MarkdownV2') 