from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, Url, Column
from aiogram_dialog.widgets.text import Const, Format
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()


class StartSG(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()


async def go_back(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.back()


async def go_next(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.next()


async def username_getter(
    dialog_manager: DialogManager, event_from_user: User, **kwargs
):
    if dialog_manager.start_data:
        getter_data = {
            "username": event_from_user.first_name or "1dy_naxui",
            "first_show": True,
        }
        dialog_manager.start_data.clear()
    else:
        getter_data = {"first_show": False}
    return getter_data


start_dialog = Dialog(
    Window(
        Format("<b>Привет, {username}!</b>\n", when="first_show"),
        Const("Это <b>первое</b> окно диалога"),
        Button(Const("Вперед ▶️"), id="b_next", on_click=go_next),
        getter=username_getter,
        state=StartSG.window_1,
    ),
    Window(
        Const("Это <b>второе</b> окно диалога"),
        Row(
            Button(Const("◀️ Назад"), id="b_back", on_click=go_back),
            Button(Const("Вперед ▶️"), id="b_next", on_click=go_next),
        ),
        state=StartSG.window_2,
    ),
    Window(
        Const("Это <b>третье</b> окно диалога"),
        Row(
            Button(Const("◀️ Назад"), id="b_back", on_click=go_back),
            Button(Const("Вперед ▶️"), id="b_next", on_click=go_next),
        ),
        state=StartSG.window_3,
    ),
    Window(
        Const("Это <b>четвертое</b> окно диалога"),
        Button(Const("◀️ Назад"), id="b_back", on_click=go_back),
        state=StartSG.window_4,
    ),
)


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        state=StartSG.window_1,
        mode=StartMode.RESET_STACK,
        data={"first_show": True},
    )


if __name__ == "__main__":
    dp.include_routers(router, start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
