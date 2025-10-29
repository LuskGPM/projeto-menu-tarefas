from .connection import ConnectionRedis, TIMER_REDIS_EX
from typing import Any
import json

class RepositoryRedis(ConnectionRedis):
    def __init__(self) -> None:
        super().__init__()
        self.__timer: int = TIMER_REDIS_EX['TIMER_30']
        
    async def _set_json(self, chanel: str, data: dict) -> None:
        async with self as redis:
            await redis.session.set(chanel, json.dumps(data))
            await redis.session.expire(chanel, self.__timer)
        
    async def _get_json(self, key) -> Any | None:
        async with self as redis:
            result = await redis.session.get(key)
            if result:
                return json.loads(result)

    async def _drop_key(self, key) -> bool:
        async with self as redis:
            result = await redis.session.delete(key)
            return result > 0
        
    async def _expire_key(self, key) -> None:
        async with self as redis:
            await redis.session.expire(key, self.__timer)
