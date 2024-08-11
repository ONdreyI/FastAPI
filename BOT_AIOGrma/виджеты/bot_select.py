from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, Url, Column, Select
from aiogram_dialog.widgets.text import Const, Format
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()


class StartSG(StatesGroup):
    start = State()


# Это геттер
async def get_categories(**kwargs):
    categories = [
        ("Техника", 1),
        ("Одежда", 2),
        ("Обувь", 3),
    ]
    return {"categories": categories}


start_dialog = Dialog(
    Window(
        Const(text="Выберите категорию:"),
        Select(
            Format("{item[0]}"),
            id="categ",
            item_id_getter=lambda x: x[1],
            items="categories",
        ),
        state=StartSG.start,
        getter=get_categories,
    ),
)


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == "__main__":
    dp.include_routers(router, start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
