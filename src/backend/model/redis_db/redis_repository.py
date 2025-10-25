from .connection import ConnectionRedis
from redis import Redis
from typing import Dict

class RepositoryRedis(ConnectionRedis):
    def __init__(self):
        super().__init__()
        self.__conn_redis = self.getConn()
        
    def insert(self, name_hash: str, key_hash: str, value_hash: any, timer: int = 1800) -> bool:
        self.__conn_redis.hset(name_hash, key_hash, value_hash)
        self.__conn_redis.expire(name=name_hash, time=timer)
        return True
        
    def get_hash_all(self, name_hash) -> Dict | None:
        return self.__conn_redis.hgetall(name_hash)
        