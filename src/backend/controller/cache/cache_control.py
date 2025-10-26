from ...model import RepositoryRedis
from typing import Dict

class RedisControl:
    def __init__(self, data: Dict | None = None, is_tarefa: bool = True, status: str | None = None) -> None:
        self.__redis_repo = RepositoryRedis()
        self.__data: Dict = data or {}
        self.__key_value = 'TAREFA' if is_tarefa else 'USUARIO'
        self.__cache_key = f'{self.__key_value}:status:{status}'
        
    def set_cache(self) -> None:
        for key, value in self.__data.items():
            self.__redis_repo.insert(self.__cache_key, key_hash=key, value_hash=str(value))
            
    def get_cache(self) -> Dict | None:
        return self.__redis_repo.get_hash_all(self.__cache_key)
