from asyncio import Lock
from collections import deque


class PairingSystem:
    def __init__(self, is_compatible_func):
        self.free_calls = deque()
        self.free_operators = deque()
        self.lock = Lock()
        self.is_compatible = is_compatible_func

    async def add_call(self, call_id: int) -> int:
        async with self.lock:
            for operator_id in list(self.free_operators):
                if await self.is_compatible(call_id, operator_id):
                    self.free_operators.remove(operator_id)
                    return operator_id
            self.free_calls.append(call_id)
            return -1

    async def  add_operator(self, operator_id: int) -> int:
        async with self.lock:
            for call_id in list(self.free_calls):
                if await self.is_compatible(call_id, operator_id):
                    self.free_calls.remove(call_id)
                    return call_id
            self.free_operators.append(operator_id)
            return -1

    async def fill_calls(self, call_list: list[int]):
        async with self.lock:
            for call in call_list:
                self.free_calls.append(call)

    async def fill_operators(self, operator_list: list[int]):
        async with self.lock:
            for operator in operator_list:
                self.free_operators.append(operator)
