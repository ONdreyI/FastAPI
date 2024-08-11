import operator

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import (
    Button,
    Row,
    Url,
    Column,
    ManagedCheckbox,
    Checkbox,
    Multiselect,
)
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


# Хэндлер, обрабатывающий нажатие кнопки в виджете `Checkbox`
async def checkbox_clicked(
    callback: CallbackQuery, checkbox: ManagedCheckbox, dialog_manager: DialogManager
):
    dialog_manager.dialog_data.update(is_checked=checkbox.is_checked())


# Геттер
async def get_topics(dialog_manager: DialogManager, **kwargs):
    topics = [
        ("IT", "1"),
        ("Дизайн", "2"),
        ("Наука", "3"),
        ("Общество", "4"),
        ("Культура", "5"),
        ("Искусство", "6"),
    ]
    return {"topics": topics}


start_dialog = Dialog(
    Window(
        Const(text="Отметьте темы новостей 👇"),
        Column(
            Multiselect(
                checked_text=Format("[✔️] {item[0]}"),
                unchecked_text=Format("[  ] {item[0]}"),
                id="multi_topics",
                item_id_getter=operator.itemgetter(1),
                items="topics",
                # min_selected=2,
                # max_selected=6,
                on_select=checkbox_clicked,
                when="multi_topics",
                is_multi=True,
            ),
        ),
        state=StartSG.start,
        getter=get_topics,
    ),
)


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == "__main__":
    dp.include_routers(router, start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
