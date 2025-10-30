import bcrypt
    
class HashSenha:
    def __init__(self, senha_do_front: str | None = None, senha_do_banco: str | None = None) -> None:
        if senha_do_front:
            self.__senha_do_front: bytes = senha_do_front.encode('utf-8')
        if senha_do_banco:
            self.__senha_do_banco: bytes = senha_do_banco.encode('utf-8')
        self.__salt: bytes = bcrypt.gensalt(12)
        
    def hash(self) -> bytes | ValueError:
        if self.__senha_do_front:
            return bcrypt.hashpw(self.__senha_do_front, self.__salt)
        raise ValueError('<HashSenha>: Senha do front-end é obrigatória para gerar o hash')
        
    def is_equal(self) -> bool | ValueError:
        if self.__senha_do_banco and self.__senha_do_front:
            return bcrypt.checkpw(self.__senha_do_front, self.__senha_do_banco)
        raise ValueError('<HashSenha>: Senha do banco/front não fornecida para comparação')
