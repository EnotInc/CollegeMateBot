import asyncio
import os

from routers.callbacks import rout_callbacks
from routers.comands import rout_commands
from routers.messages import rout_messages
from routers.daily_schedule import rout_daily

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    try:
        from backend_logic.auto_scheduler import scheduler
        dp.include_router(rout_callbacks)
        dp.include_router(rout_commands)
        dp.include_router(rout_messages)
        dp.include_router(rout_daily)
        await asyncio.gather(dp.start_polling(bot), scheduler())
    except:
         print("Bot Got Stopped")

if __name__ == "__main__":
        asyncio.run(main())
