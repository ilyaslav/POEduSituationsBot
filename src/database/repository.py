from sqlalchemy import select, delete

from src.database.database import session_factory
from src.database.models import UserBase, CallBase, ImgBase
from sqlalchemy.sql.expression import update


class Repository:

    @staticmethod
    async def get_all_users() -> list[str]:
        async with session_factory() as session:
            result = await session.execute(
                select(UserBase.user_id)
            )
            return [row[0] for row in result.all()]

    @staticmethod
    async def set_team(user_id: str, team_id: int):
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(user_id=None)
                .filter(UserBase.role_admin == False)
                .filter(UserBase.user_id == user_id)
            )
            await sf.execute(
                update(UserBase)
                .values(user_id=user_id)
                .filter(UserBase.team_id == team_id)
            )
            await sf.commit()

    @staticmethod
    async def set_admin(user_id: str, admin_id: int):
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(user_id=None)
                .filter(UserBase.role_admin == True)
                .filter(UserBase.user_id == user_id)
            )
            await sf.execute(
                update(UserBase)
                .values(user_id=user_id)
                .filter(UserBase.admin_id == admin_id)
            )
            await sf.commit()

    @staticmethod
    async def set_in_progress(user_id: str, in_progress_id: bool):
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(in_progress=in_progress_id)
                .filter(UserBase.user_id == user_id)
            )
            await sf.commit()

    @staticmethod
    async def get_user(user_id: str) -> UserBase:
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase)
                .filter(UserBase.user_id == user_id)
            )
            return res.scalar_one_or_none()

    @staticmethod
    async def get_admin(admin_id: int) -> UserBase:
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase)
                .filter(UserBase.admin_id == admin_id)
                .filter(UserBase.role_admin == True)
            )
            return res.scalar_one_or_none()

    @staticmethod
    async def get_team(team_id: int) -> UserBase:
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase)
                .filter(UserBase.team_id == team_id)
                .filter(UserBase.role_admin == False)
            )
            return res.scalar_one_or_none()

    @staticmethod
    async def check_admin(user_id: str):
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase)
                .filter(UserBase.user_id == user_id)
            )
            user = res.scalar_one_or_none()
            return user.role_admin if user else False

    @staticmethod
    async def reset_game():
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(user_id=None)
                .values(admin_id=None)
                .filter(UserBase.role_admin == False)
            )
            await sf.execute(
                update(UserBase)
                .values(team_id=None)
                .filter(UserBase.role_admin == True)
            )
            await sf.execute(
                update(UserBase)
                .values(in_progress=False)
                .values(feedback_id=None)
            )
            await sf.execute(delete(CallBase))
            await sf.commit()

    @staticmethod
    async def add_call(admin_id: int, team_id: int):
        async with session_factory() as sf:
            new_call = CallBase(
                admin_id=admin_id,
                team_id=team_id
            )
            sf.add(new_call)
            await sf.commit()

    @staticmethod
    async def update_after_call(admin_id: int, team_id: int):
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(admin_id=admin_id)
                .filter(UserBase.team_id == team_id)
                .filter(UserBase.role_admin == False)
            )
            await sf.execute(
                update(UserBase)
                .values(team_id=team_id)
                .filter(UserBase.admin_id == admin_id)
                .filter(UserBase.role_admin == True)
            )
            await sf.commit()

    @staticmethod
    async def get_call(admin_id: int, team_id: int):
        async with session_factory() as sf:
            res = await sf.execute(
                select(CallBase)
                .filter(CallBase.admin_id == admin_id)
                .filter(CallBase.team_id == team_id)
            )
            return res.scalar_one_or_none()

    @staticmethod
    async def check_call(admin_id: int, team_id: int):
        async with session_factory() as sf:
            res = await sf.execute(
                select(CallBase)
                .filter(CallBase.admin_id == admin_id)
                .filter(CallBase.team_id == team_id)
            )
            return res.scalar_one_or_none() is None

    @staticmethod
    async def add_admin_feedback(admin_id: int, team_id: int, feedback: str):
        async with session_factory() as sf:
            await sf.execute(
                update(CallBase)
                .values(admin_feedback=CallBase.admin_feedback + f" {feedback}")
                .filter(CallBase.admin_id == admin_id)
                .filter(CallBase.team_id == team_id)
            )
            await sf.commit()

    @staticmethod
    async def add_team_feedback(admin_id: int, team_id: int, feedback: int):
        async with session_factory() as sf:
            await sf.execute(
                update(CallBase)
                .values(team_feedback=feedback)
                .filter(CallBase.admin_id == admin_id)
                .filter(CallBase.team_id == team_id)
            )
            await sf.commit()

    @staticmethod
    async def get_free_teams() -> list[int]:
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase.team_id)
                .filter(UserBase.role_admin == False)
                .filter(UserBase.in_progress == False)
                .filter(UserBase.team_id != None)
            )
            return [team_id for (team_id,) in res.all()]

    @staticmethod
    async def get_free_admins() -> list[int]:
        async with session_factory() as sf:
            res = await sf.execute(
                select(UserBase.admin_id)
                .filter(UserBase.role_admin == True)
                .filter(UserBase.in_progress == False)
                .filter(UserBase.user_id != None)
            )
            return [admin_id for (admin_id,) in res.all()]

    @staticmethod
    async def set_feedback_id(admin_id: int, team_id: int):
        async with session_factory() as sf:
            await sf.execute(
                update(UserBase)
                .values(feedback_id=admin_id)
                .filter(UserBase.team_id == team_id)
                .filter(UserBase.role_admin == False)
            )
            await sf.execute(
                update(UserBase)
                .values(feedback_id=team_id)
                .filter(UserBase.admin_id == admin_id)
                .filter(UserBase.role_admin == True)
            )
            await sf.commit()

    @staticmethod
    async def set_img_user_id(img_name: str, user_id: str):
        async with session_factory() as sf:
            await sf.execute(
                update(ImgBase)
                .values(user_id=user_id)
                .filter(ImgBase.name==img_name)
            )
            await sf.commit()

    @staticmethod
    async def set_img_id(user_id: str, img_id: str):
        async with session_factory() as sf:
            await sf.execute(
                update(ImgBase)
                .values(id=img_id)
                .values(user_id=None)
                .filter(ImgBase.user_id==user_id)
            )
            await sf.commit()

    @staticmethod
    async def get_img_by_name(img_name: str) -> str:
        async with session_factory() as sf:
            res = await sf.execute(
                select(ImgBase)
                .filter(ImgBase.name==img_name)
            )
            return res.scalar_one_or_none().id
