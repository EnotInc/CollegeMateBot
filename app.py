import asyncio
import os

from handlers import router
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    try:
        dp.include_router(router)
        await dp.start_polling(bot)
    except:
         print("Exit")

if __name__ == "__main__":
        load_dotenv()
        asyncio.run(main())
