from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def get_set_team_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Команда 1", callback_data="team_1")],
            [InlineKeyboardButton(text="Команда 2", callback_data="team_2")],
            [InlineKeyboardButton(text="Команда 3", callback_data="team_3")],
            [InlineKeyboardButton(text="Команда 4", callback_data="team_4")],
            [InlineKeyboardButton(text="Команда 5", callback_data="team_5")],
            [InlineKeyboardButton(text="Команда 6", callback_data="team_6")],
            [InlineKeyboardButton(text="Команда 7", callback_data="team_7")],
            [InlineKeyboardButton(text="Команда 8", callback_data="team_8")],
            [InlineKeyboardButton(text="Команда 9", callback_data="team_9")],
            [InlineKeyboardButton(text="Команда 10", callback_data="team_10")],
            [InlineKeyboardButton(text="Команда 11", callback_data="team_11")],
        ]
    )


def get_team_feedback_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data="feedback_1")],
            [InlineKeyboardButton(text="2", callback_data="feedback_2")],
            [InlineKeyboardButton(text="3", callback_data="feedback_3")],
            [InlineKeyboardButton(text="4", callback_data="feedback_4")],
            [InlineKeyboardButton(text="5", callback_data="feedback_5")],
        ]
    )


def get_admin_feedback_keyboard(persons: str) -> ReplyKeyboardMarkup:
    names = [name.strip() for name in persons.split(",") if name.strip()]
    keyboard = [[KeyboardButton(text=name)] for name in names]
    keyboard.append([KeyboardButton(text="никто")])
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_start_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Начать", callback_data="start")],
        ]
    )


def get_finish_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Завершить", callback_data="finish")],
        ]
    )

def get_admin_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Начать игру", callback_data="start_game")],
            [InlineKeyboardButton(text="Остановить игру", callback_data="stop_game")],
            [InlineKeyboardButton(text="Перезагрузить игру", callback_data="reset_game")],
            [InlineKeyboardButton(text="Поменять фото", callback_data="change_photo")],
            [InlineKeyboardButton(text="Админ 1", callback_data="admin1")],
            [InlineKeyboardButton(text="Админ 2", callback_data="admin2")],
            [InlineKeyboardButton(text="Админ 3", callback_data="admin3")],
            [InlineKeyboardButton(text="Админ 4", callback_data="admin4")],
            [InlineKeyboardButton(text="Админ 5", callback_data="admin5")],
            [InlineKeyboardButton(text="Админ 6", callback_data="admin6")],
            [InlineKeyboardButton(text="Админ 7", callback_data="admin7")],
            [InlineKeyboardButton(text="Админ 8", callback_data="admin8")],
            [InlineKeyboardButton(text="Админ 9", callback_data="admin9")],
            [InlineKeyboardButton(text="Админ 10", callback_data="admin10")],
            [InlineKeyboardButton(text="Админ 11", callback_data="admin11")],
            [InlineKeyboardButton(text="Админ 12", callback_data="admin11")],
        ]
    )

def get_photo_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Поменять приветствие", callback_data="img0"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check0")],
            [InlineKeyboardButton(text="Поменять педситуацию 1", callback_data="img1"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check1")],
            [InlineKeyboardButton(text="Поменять педситуацию 2", callback_data="img2"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check2")],
            [InlineKeyboardButton(text="Поменять педситуацию 3", callback_data="img3"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check3")],
            [InlineKeyboardButton(text="Поменять педситуацию 4", callback_data="img4"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check4")],
            [InlineKeyboardButton(text="Поменять педситуацию 5", callback_data="img5"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check5")],
            [InlineKeyboardButton(text="Поменять педситуацию 6", callback_data="img6"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check6")],
            [InlineKeyboardButton(text="Поменять педситуацию 7", callback_data="img7"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check7")],
            [InlineKeyboardButton(text="Поменять педситуацию 8", callback_data="img8"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check8")],
            [InlineKeyboardButton(text="Поменять педситуацию 9", callback_data="img9"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check9")],
            [InlineKeyboardButton(text="Поменять педситуацию 10", callback_data="img10"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check10")],
            [InlineKeyboardButton(text="Поменять педситуацию 11", callback_data="img11"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check11")],
            [InlineKeyboardButton(text="Поменять педситуацию 12", callback_data="img12"),
             InlineKeyboardButton(text="Посмотреть", callback_data="check12")],
        ]
    )
