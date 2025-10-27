from ....model import RepositoryRedis
from typing import Dict, Any

class RedisControl:
    def __init__(self, cache_key: str, cache_data: Dict | Any | None = None) -> None:
        self.__redis_repo = RepositoryRedis()
        self.__data: Dict | Any = cache_data or {}
        self.__cache_key = cache_key
        
    def set_hash_cache(self) -> None | TypeError:
        if not isinstance(self.__data, dict):
            raise TypeError('Objeto precisa ser um dicionário para ser inserido como hash')
        for key, value in self.__data.items():
            self.__redis_repo.insert(self.__cache_key, key_hash=key, value_hash=str(value))
            
    def get_hash_cache(self) -> Dict | None:
        return self.__redis_repo.get_hash_all(self.__cache_key)
    
    def set_cache(self) -> None | TypeError:
        if isinstance(self.__data, dict):
            raise TypeError('Para trabalhar com dicionários escolha o método set_hash_cache')
        self.__redis_repo.set_key(self.__cache_key, self.__data)

    def get_cache(self) -> Any | None:
        return self.__redis_repo.get_key(self.__cache_key)
    
    def delete_cache(self) -> bool:
        return self.__redis_repo.drop_cache(self.__cache_key)
    
    def renovar_cache(self) -> None:
        self.__redis_repo.expire(self.__cache_key)
