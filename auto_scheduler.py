import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app import bot
from parser import get_link

async def friday_schedule():
    try:
        await bot.send_message(chat_id=os.getenv('DEVELOPER'), text='Ваше расписание:')
        await bot.send_document(chat_id=os.getenv('DEVELOPER'), document=get_link())
    except Exception as ex:
        print(ex)


async def scheduler():
    scheduler = AsyncIOScheduler()
    
    scheduler.add_job(
         friday_schedule, trigger=CronTrigger(
              day_of_week="fri",
              hour="12",
              minute="40",
              timezone="Europe/Moscow"
         )
    )

    scheduler.start()