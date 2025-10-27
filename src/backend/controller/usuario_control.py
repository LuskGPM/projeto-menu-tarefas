from ..model import Usuario, UsuarioRepository
from .configs import RedisControl as RedCache, HashSenha
from .configs import build_cache_key, COMMON_KEYS, ENTITIES, USUARIO_STATUS
from typing import Dict

class UsuarioControler:
    
    def __init__(self):
        self.__user_repo = UsuarioRepository()
    
    def processar_cadastro(self, dados: Dict) -> None | Exception:
        # Cadastra novo usuário
        ## Hash da senha
        senha_hash = HashSenha(senha_do_front=dados['senha']).hash()
        new_user = Usuario(
            nome = dados['nome'],
            nickname = dados['nickname'],
            senha_hash = senha_hash
        )
        ## Insere novo usuário
        self.__user_repo.insert(new_user)
    
    def verificar_disponibilidade_nickname(self, nickname: str) -> bool:
        # Verificar se o nickname já existe
        nickname_no_banco = self.__user_repo.select_by_nickname(nickname)
        if nickname_no_banco: # Se o nickname for encontrado, retorna False
            return False
        return True
    
    def autenticar_usuario(self, nickname: str, senha_do_front: str) -> None | ValueError:
        senha_do_banco = self.__user_repo.select_by_nickname(nickname).senha_hash
        if not HashSenha(senha_do_front, senha_do_banco).is_equal():
            raise ValueError('Senha fornecida pelo front não condiz com a senha do banco')
        
        RedCache(cache_key=COMMON_KEYS['USUARIO_LOGADO'], cache_data=nickname).processar_cache()
    
    def encerrar_sessao(self) -> str:
        delete_cache = RedCache(cache_key=COMMON_KEYS['USUARIO_LOGADO']).excluir_cache()
        if delete_cache:
            return 'Sessão encerrada com sucesso'
        return 'Sessão já estava encerrada'
    
    def esta_logado(self) -> bool:
        cache = RedCache(COMMON_KEYS['USUARIO_LOGADO'])
        if cache.receber_cache():
            cache.renovar_cache()
            return True
        return False
    
    def obter_nickname_sessao(self) -> str | None:
        cache_nickname = RedCache(COMMON_KEYS['USUARIO_LOGADO']).receber_cache()
        if cache_nickname:
            return cache_nickname
