from ....model.redis_db import RepositoryRedis
from typing import Dict, Any

class RedisControl(RepositoryRedis):
    def __init__(self, cache_key: str, cache_data: Dict | Any | None = None) -> None:
        super().__init__()
        self.__data: Dict | Any = cache_data or {}
        self.__cache_key = cache_key
        
    async def processar_hash_cache(self) -> None | TypeError:
        if not isinstance(self.__data, dict):
            raise TypeError('<RedisControl>: Objeto precisa ser um dicionário para ser inserido como hash')
        for key, value in self.__data.items():
            await self.set_hash_cache(self.__cache_key, key, value)
            
    async def processar_cache(self) -> None | TypeError:
        if isinstance(self.__data, dict):
            raise TypeError('<RedisControl>: Para trabalhar com dicionários escolha o método set_hash_cache')
        await self.set_key(self.__cache_key, self.__data)
    
    async def renovar_cache(self) -> None:
        await self.expire(self.__cache_key)

    async def receber_hash_cache(self) -> Dict | None:
        result = await self.get_hash_all(self.__cache_key)
        return result
    
    async def receber_cache(self) -> Any | None:
        result = await self.get_key(self.__cache_key)
        return result
    
    async def excluir_cache(self) -> bool:
        result = await self.delete_cache(self.__cache_key)
        return result
    