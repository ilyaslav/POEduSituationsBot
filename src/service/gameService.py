import config
from src.service.keyboardBuilder import get_start_keyboard
from src.service.singleTimer import SingleTimer
from src.database.repository import Repository
from src.service.pairingSystem import PairingSystem
from src.texts import time_message, calls, press_start
from asyncio import Lock

class GameService:
    def __init__(self):
        self.game_status = False
        self.pairingSystem = PairingSystem(Repository.check_call)
        self.lock = Lock()
        self.notifications = {
            1: SingleTimer(lambda: self.sendNotification(1), 300),
            2: SingleTimer(lambda: self.sendNotification(2), 300),
            3: SingleTimer(lambda: self.sendNotification(3), 300),
            4: SingleTimer(lambda: self.sendNotification(4), 300),
            5: SingleTimer(lambda: self.sendNotification(5), 300),
            6: SingleTimer(lambda: self.sendNotification(6), 300),
            7: SingleTimer(lambda: self.sendNotification(7), 300),
            8: SingleTimer(lambda: self.sendNotification(8), 300),
            9: SingleTimer(lambda: self.sendNotification(9), 300),
            10: SingleTimer(lambda: self.sendNotification(10), 300),
            11: SingleTimer(lambda: self.sendNotification(11), 300),
            12: SingleTimer(lambda: self.sendNotification(12), 300),
        }

    async def sendNotification(self, admin_id: int):
        admin = await Repository.get_admin(admin_id)
        await config.bot.send_message(admin.user_id, time_message)

    async def startGame(self):
        admins = await Repository.get_free_admins()
        teams = await Repository.get_free_teams()
        # admins = [1]
        # teams = [1]
        await self.pairingSystem.fill_operators(admins)
        for team_id in teams:
            await self.workCall(team_id)


    async def workCall(self, team_id: int):
        async with self.lock:
            admin_id = await self.pairingSystem.add_call(team_id)
            if admin_id != -1:
                try:
                    await self.call(admin_id, team_id)
                except:
                    await self.workCall(team_id)

    async def workOperator(self, admin_id: int):
        async with self.lock:
            team_id = await self.pairingSystem.add_operator(admin_id)
            if team_id != -1:
                try:
                    await self.call(admin_id, team_id)
                except:
                    await self.workOperator(admin_id)

    async def call(self, admin_id: int, team_id: int):
        if not self.game_status:
            return
        admin = await Repository.get_admin(admin_id)
        team = await Repository.get_team(team_id)
        print(1)
        await Repository.add_call(admin_id, team_id)
        await Repository.update_after_call(admin_id, team_id)
        print(11)
        await Repository.set_in_progress(admin.user_id, True)
        await Repository.set_in_progress(team.user_id, True)
        print(111)
        keyboard = get_start_keyboard()
        file_id = await Repository.get_img_by_name(f"img{admin_id}")
        print(1111)
        await config.bot.send_message(chat_id=admin.user_id, text="Кто-то идёт"+press_start, reply_markup=keyboard)
        await config.bot.send_photo(chat_id=team.user_id, caption=calls[admin_id], photo=file_id)
        print(2)

gameService = GameService()
