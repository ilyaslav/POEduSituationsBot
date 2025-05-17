import asyncio
import logging
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from aiogram.filters import CommandStart
from aiogram.types import Message

from service.callback import *

@config.dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = get_set_team_keyboard()
    file_id = await Repository.get_img_by_name("img0")
    await message.answer_photo(photo=file_id, caption=hellow_message, reply_markup=keyboard)

@config.dp.message(lambda message: message.photo)
async def set_photo(message: Message):
    user_id = str(message.from_user.id)
    if not await Repository.check_admin(user_id):
        return
    file_id = message.photo[-1].file_id
    await Repository.set_img_id(user_id, file_id)
    await message.answer(text="Изображение загружено")

@config.dp.message()
async def echo_handler(message: Message) -> None:
    user_id = str(message.from_user.id)
    user = await Repository.get_user(user_id)
    if message.text.lower() == "секретный пароль":
        keyword = get_admin_keyboard()
        await message.answer(text = admin_menu_text, reply_markup=keyword)
    elif user is None:
        await message.answer(not_exist)
        return
    elif message.text == "Номер команды":
        await message.answer(teams.get(user.team_id, not_exist))
    elif user.role_admin:
        if not await Repository.check_call(user.admin_id, user.feedback_id):
            return
        await Repository.add_admin_feedback(user.admin_id, user.feedback_id, message.text)


async def main() -> None:
    # And the run events dispatching
    await config.dp.start_polling(config.bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())