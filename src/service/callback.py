from aiogram import F

import config
from src.database.repository import Repository
from src.service.gameService import gameService
from src.service.keyboardBuilder import *
from src.texts import *


@config.dp.callback_query(F.data == "start_game")
async def callback_button(callback_query):
    gameService.game_status = True
    await gameService.startGame()


@config.dp.callback_query(F.data == "stop_game")
async def callback_button(callback_query):
    gameService.game_status = False
    users = await Repository.get_all_users()
    for user_id in users:
        await config.bot.send_message(chat_id=user_id, text=finish_game)

@config.dp.callback_query(F.data == "reset_game")
async def callback_button(callback_query):
    gameService.game_status = False
    await Repository.reset_game()
    await callback_query.message.answer(text="Игра перезагружена")


@config.dp.callback_query(F.data == "change_photo")
async def callback_button(callback_query):
    keyboard = get_photo_keyboard()
    await callback_query.message.answer(text=change_photo, reply_markup=keyboard)


@config.dp.callback_query(F.data == "start")
async def callback_button(callback_query):
    user_id = str(callback_query.from_user.id)
    admin = await Repository.get_user(user_id)

    gameService.notifications.get(admin.admin_id).start()

    keyboard = get_finish_keyboard()
    await callback_query.message.answer(text=press_finish, reply_markup=keyboard)
    await callback_query.message.delete()


@config.dp.callback_query(F.data == "finish")
async def callback_button(callback_query):
    user_id = str(callback_query.from_user.id)
    admin = await Repository.get_user(user_id)
    team = await Repository.get_team(admin.team_id)
    gameService.notifications.get(admin.admin_id).stop()

    await Repository.set_in_progress(admin.user_id, False)
    await Repository.set_in_progress(team.user_id, False)
    await gameService.workCall(team.team_id)
    await gameService.workOperator(admin.admin_id)

    await Repository.set_feedback_id(admin.admin_id, team.team_id)
    admin_keyboard = get_admin_feedback_keyboard(team.persons)
    team_keyboard = get_team_feedback_keyboard()
    await config.bot.send_message(admin.user_id, text=admin_feedback_message ,reply_markup=admin_keyboard)
    await config.bot.send_message(team.user_id, text=team_feedback_message ,reply_markup=team_keyboard)
    await callback_query.message.delete()


@config.dp.callback_query(F.data.contains("team"))
async def callback_button(callback_query):
    if gameService.game_status:
        await callback_query.message.delete()
        return
    team_id = int(callback_query.data[5:])
    text = teams[team_id]
    await Repository.set_team(str(callback_query.from_user.id), team_id)
    await callback_query.message.answer(text=text)
    await callback_query.message.delete()


@config.dp.callback_query(F.data.contains("feedback"))
async def callback_button(callback_query):
    user_id = str(callback_query.from_user.id)
    user = await Repository.get_user(user_id)
    if await Repository.check_call(user.feedback_id, user.team_id):
        await Repository.add_team_feedback(user.admin_id, user.feedback_id, int(callback_query.data[-1]))
    await callback_query.message.delete()


@config.dp.callback_query(F.data.contains("admin"))
async def callback_button(callback_query):
    if gameService.game_status:
        return
    user_id = str(callback_query.from_user.id)
    await Repository.set_admin(user_id, int(callback_query.data[5:]))
    keyboard = get_admin_keyboard()
    await callback_query.message.answer(f"Вы стали админом {callback_query.data[5:]}\n{admin_menu_text}", reply_markup=keyboard)


@config.dp.callback_query(F.data.contains("img"))
async def callback_button(callback_query):
    user_id = str(callback_query.from_user.id)
    await Repository.set_img_user_id(callback_query.data, user_id)
    await callback_query.message.answer(text=send_photo)


@config.dp.callback_query(F.data.contains("check"))
async def callback_button(callback_query):
    file_id = await Repository.get_img_by_name(f"img{callback_query.data[5:]}")
    if file_id:
        await callback_query.message.answer_photo(photo=file_id)
    else:
        await callback_query.message.answer(text="Изображение не загружено")
