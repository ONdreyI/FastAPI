from pprint import pprint

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import (
    Const,
    Format,
)  # Здесь будем импортировать нужные виджеты
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class StartSG(StatesGroup):
    start = State()


async def some_hendler(
    callback: CallbackQuery, dialog_manager: DialogManager
):  # Здесь будут хэндлеры
    pass


async def some_getter(**kwargs):  # Здесь дудем создавать нужные геттеры
    pass


async def username_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs,
):  # Здесь дудем создавать нужные геттеры
    pprint(kwargs)
    return {"username": event_from_user.first_name, "user_id": event_from_user.id}


# Это стартовый диалог
start_dialog = Dialog(
    Window(
        Format("Привет, {username}!"),
        getter=username_getter,
        state=StartSG.start,
    ),  # Здесь будем добавлять виджеты и геттеры
)


@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == "__main__":
    dp.include_router(start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
