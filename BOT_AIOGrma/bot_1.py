import asyncio

from aiogram import Bot, Router, Dispatcher
from aiogram.types import Message

router = Router()
TOKEN = "5813663548:AAFc9jg8YYE7sZtV98bkura56hxztU4EMU0"


@router.message()
async def any_message(msg: Message):
    await msg.answer("Hello World!")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
