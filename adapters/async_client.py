from typing import List
import certifi
import ssl

import aiohttp
import asyncio


class AsyncReqResClient:
    def __init__(self):
        self.host = 'https://reqres.in/api'

    def get_requests(self, user_ids: List[int]):
        return asyncio.run(self._get_requests(user_ids=user_ids))

    @staticmethod
    async def fetch(session: aiohttp.ClientSession, url: str):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with session.get(url, ssl=ssl_context) as response:
            return await response.json()

    async def _get_requests(self, user_ids: List[int]):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, f'{self.host}/users/{user_id}') for user_id in user_ids]
            return await asyncio.gather(*tasks)
