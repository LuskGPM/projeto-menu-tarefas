from ....model.redis_db import RepositoryRedis
from typing import Dict, Any

class RedisControl(RepositoryRedis):
    def __init__(self, cache_key: str, cache_data: Dict | None = None) -> None:
        super().__init__()
        self.__data: Dict = cache_data or {}
        self.__key = cache_key
        
    async def processar_cache(self) -> None:
        await self._set_json(self.__key, self.__data)
    
    async def receber_cache(self) -> dict | None:
        result = await self._get_json(self.__key)
        return result

    async def excluir_cache(self) -> bool:
        result = await self._drop_key(self.__key)
        return result
    
    async def renovar_cache(self) -> None:
        await self._expire_key(self.__key)
        
    def adicionar_dados(self, data: Dict) -> None:
        self.__data = data
    