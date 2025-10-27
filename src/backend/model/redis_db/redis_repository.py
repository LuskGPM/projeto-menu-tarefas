from .connection import ConnectionRedis, TIMER_REDIS_EX
from redis import Redis
from typing import Dict, Any

class RepositoryRedis(ConnectionRedis):
    def __init__(self) -> None:
        super().__init__()
        self.__conn_redis: Redis = self.getConn()
        self.__timer: int = TIMER_REDIS_EX['TIMER_30']
        
    def set_key(self, name_key: str, value_key: Any) -> None:
        self.__conn_redis.setex(name_key, self.__timer, value_key)
        
    def get_key(self, name_key: str) -> Any | None:
        return self.__conn_redis.get(name_key)
        
    def insert(self, name_hash: str, key_hash: str, value_hash: any) -> None:
        self.__conn_redis.hset(name_hash, key_hash, value_hash)
        self.__conn_redis.expire(name=name_hash, time=self.__timer)
        
    def get_hash_all(self, name_hash) -> Dict | None:
        return self.__conn_redis.hgetall(name_hash)
        
    def drop_cache(self, name_hash: str) -> bool:
        result = self.__conn_redis.delete(name_hash)
        return result > 0 # Se houve um ou mais deletes retorna True

    def expire(self, name_key) -> None:
        self.__conn_redis.expire(name_key, time=self.__timer)
        