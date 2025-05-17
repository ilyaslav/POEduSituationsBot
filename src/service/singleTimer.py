import asyncio

class SingleTimer:
    def __init__(self, callback, delay = None):
        self.delay = delay or 0
        self.callback = callback
        self.task = None

    async def _run(self):
        try:
            await asyncio.sleep(self.delay)
            await self.callback()
        except asyncio.CancelledError:
            print("[Timer] Задача отменена.")
        except Exception as e:
            print(f"[Timer error]: {e}")

    def start(self, delay=None):
        self.stop()  # отменяем предыдущую задачу, если есть
        self.delay = delay if delay is not None else self.delay
        self.task = asyncio.create_task(self._run())

    def stop(self):
        if self.task and not self.task.done():
            self.task.cancel()
        self.task = None

    def is_running(self):
        return self.task is not None and not self.task.done()