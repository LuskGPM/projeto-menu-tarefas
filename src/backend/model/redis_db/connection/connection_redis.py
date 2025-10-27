import aioredis
from aioredis import Redis
from aioredis.exceptions import AuthenticationError
from .connection_config import DATABASE_SETTINGS

class ConnectionRedis:
    def __init__(self) -> None:
        self.__redis_url: str = DATABASE_SETTINGS['URL']
        self.session: Redis = None
        
    async def __conn(self) -> Redis | AuthenticationError:
        try:
            r = await aioredis.from_url(self.__redis_url)
            return r
        except AuthenticationError as e:
            raise AuthenticationError('Erro ao conectar ao banco: ',{e})
            
    async def __getConn(self) -> Redis | AuthenticationError:
        return await self.__conn()

    async def __aenter__(self):
        self.session = await self.__getConn()
        return self
    
    async def __aexit__(self, *args):
        await self.session.close()
