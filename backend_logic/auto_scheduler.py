import json

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from backend_logic.schedule_constructor import get_all_schedules
from backend_logic.parser import get_link
from app import bot


async def friday_schedule():
    try:
        users = []
        with open('users.json', 'r+') as file:
            users = json.load(file)
        
        for user in users:
            await bot.send_message(chat_id=user['user_chat_id'], message_thread_id=user['user_topic'], text='ВНИМАНИЕ!\nВ связи с переездом бот будет временно отключен для его доработки. Постараемся вернуться через неделю. \nСпасибо за понимание!\n\n|\\_ _ _/|\n|Q w Q|')
            #await bot.send_message(chat_id=user['user_chat_id'], message_thread_id=user['user_topic'], text='Ваше расписание:')
            #await bot.send_document(chat_id=user['user_chat_id'], message_thread_id=user['user_topic'], document=get_link(course=user['user_course'], week=1))
    except Exception as ex:
        print(f'error at sending message:\n{ex}')


async def scheduler():
    scheduler = AsyncIOScheduler()
    
    scheduler.add_job(
         friday_schedule, trigger=CronTrigger(
              day_of_week="*",
              hour="*",
              minute="*",
              timezone="Europe/Moscow"
         )
    )

    scheduler.add_job(
         get_all_schedules, trigger=CronTrigger(
            day_of_week='sun',
            hour='2',
            minute='15'
         ) 
    )

    scheduler.start()


def add_user(user_chat_id, course, topic=None) -> bool:
    try:
        new_user = []

        with open('users.json', 'r') as file:
            new_user = json.load(file)

            if any(user['user_chat_id'] == user_chat_id for user in new_user):
                return False

        new_user.append({
            'user_chat_id': user_chat_id,
            'user_course': course,
            'user_topic': topic
        })

        with open('users.json', 'r+') as file:
            json.dump(new_user, file, ensure_ascii=False, indent=4)
        return True

    except Exception as ex:
        print(f'Error at add_user:\n{ex}')
        return False


def delete_user(user_chat_id):
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
        
        new_users = [user for user in users if user['user_chat_id'] != user_chat_id]
        if len(new_users) == len(users):
            return None        

        with open('users.json', 'w') as file:
            json.dump(new_users, file,  ensure_ascii=False, indent=4)

    except Exception as ex:
        print(f'Error at delete_user:\n{ex}')
        return None


def edit_user(user_chat_id, new_course):
    with open('users.json', "r+", encoding="utf-8") as file:
        users = json.load(file)
        updated = False
        
        for user in users:
            if user["user_chat_id"] == user_chat_id:
                user["course"] = new_course
                updated = True
                break

        if not updated:
            return False

        file.seek(0)
        json.dump(users, file, ensure_ascii=False, indent=4)
        file.truncate()
        return True