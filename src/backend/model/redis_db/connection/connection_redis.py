from redis import Redis
from redis.exceptions import AuthenticationError
from .connection_config import DATABASE_SETTINGS

class ConnectionRedis:
    def __init__(self) -> None:
        self.__host: str = DATABASE_SETTINGS['HOST']
        self.__port: int = DATABASE_SETTINGS['PORT']
        self.__decode_responses: bool = DATABASE_SETTINGS['DECODE_RESPONSES']
        self.__username: str = DATABASE_SETTINGS['USERNAME']
        self.__password: str = DATABASE_SETTINGS['PASSWORD']
        
    def __conn(self) -> Redis | AuthenticationError:
        try:
            r = Redis(
                host=self.__host,
                port=self.__port,
                decode_responses=self.__decode_responses,
                username=self.__username,
                password=self.__password
            )
            return r
        except AuthenticationError as e:
            raise AuthenticationError('Erro ao conectar ao banco: ',{e})
            
    def getConn(self) -> Redis | AuthenticationError:
        return self.__conn()
