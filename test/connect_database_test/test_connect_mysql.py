from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

class ConnectionMySQL:
    def __init__(self):
        self.__conn_str: str = 'mysql+pymysql://luskgpm:lgm256974@localhost:3306/teste_menu_tarefas'
        self.__engine: Engine = self.__create_engine()
        self.session = None
        
    def __create_engine(self) -> Engine:
        return create_engine(self.__conn_str)
    
    def get_engine(self) -> Engine:
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
        
    def __exit__(self, *args):
        self.session.close()
