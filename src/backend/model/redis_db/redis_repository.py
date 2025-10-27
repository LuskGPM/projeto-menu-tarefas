from .connection import ConnectionRedis, TIMER_REDIS_EX
from typing import Dict, Any

class RepositoryRedis(ConnectionRedis):
    def __init__(self) -> None:
        super().__init__()
        self.__timer: int = TIMER_REDIS_EX['TIMER_30']
        
    async def set_key(self, name_key: str, value_key: Any) -> None:
        async with self as redis:
            await redis.session.set(name_key, value_key)
        
    async def get_key(self, name_key: str) -> Any | None:
        async with self as redis:
            return await redis.session.get(name_key)
        
    async def set_hash_cache(self, name_hash: str, key_hash: str, value_hash: any) -> None:
        async with self as redis:
            await redis.session.hset(name_hash, key_hash, value_hash)
            await redis.session.expire(name_hash, time=self.__timer)
        
    async def get_hash_all(self, name_hash) -> Dict | None:
        async with self as redis:
            return await redis.session.hgetall(name_hash)
        
    async def delete_cache(self, name_hash: str) -> bool:
        async with self as redis:
            result = await redis.session.delete(name_hash)
            return result > 0 # Se houver um ou mais deletes, retorna True

    async def expire(self, name_key) -> None:
        async with self as redis:
            await redis.session.expire(name_key, time=self.__timer)
        