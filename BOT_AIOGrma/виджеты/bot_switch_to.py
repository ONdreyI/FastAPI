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


start_dialog = Dialog(
    Window(
        Const("На кнопки из этого сообщения можно нажать!"),
        Column(
            Button(
                text=Const("Нажми!"),
                id="button_1",
            ),
            Button(
                text=Const("И меня!"),
                id="button_2",
            ),
            Button(
                text=Const("И меня тоже!"),
                id="button_3",
            ),
        ),
        state=StartSG.start,
    ),
)


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == "__main__":
    dp.include_routers(router, start_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
