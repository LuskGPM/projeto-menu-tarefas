from ..view.schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate
from ..model.mysql_db import Usuario, UsuarioRepository
from .configs import RedisControl as RedCache, HashSenha, COMMON_KEYS

class UsuarioControler:
    
    def __init__(self) -> None:
        self.__user_repo = UsuarioRepository()
        
    def processar_update(self, user: UsuarioUpdate) -> None | ValueError:
        # Busca o nickname na sessão em cache
        nickname_sessao = RedCache(COMMON_KEYS['USUARIO_LOGADO']).receber_cache()
        dados_usuario = self.__user_repo.select_by_nickname(nickname_sessao)
        # Senha do banco para validar o update
        senha_do_banco = dados_usuario.senha_hash
        ## Validação da senha do banco com a senha fornecida
        if not HashSenha(user.senha_antiga, senha_do_banco).is_equal():
            raise ValueError('Senha incorreta')
        
        new_dados_usuario = user.model_dump(exclude_unset=True) # Excluí dados não fornecidos
        # Verifica se existe uma nova senha e trata ela
        if 'senha_nova' in new_dados_usuario:
            new_dados_usuario['senha_hash'] = HashSenha(new_dados_usuario['senha_nova']).hash()
            del new_dados_usuario['senha_nova']
        new_dados_usuario.pop('senha_antiga', None)
        
        for key, value in new_dados_usuario.items():
            setattr(dados_usuario, key, value)
        self.__user_repo.update(dados_usuario)
    
    def processar_cadastro(self, user: UsuarioCreate) -> None:
        # Cadastra novo usuário
        ## Hash da senha
        senha_hash = HashSenha(user.senha_front).hash()
        new_user = Usuario(
            nome = user.nome,
            nickname = user.nickname,
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
    
    def autenticar_usuario(self, user: UsuarioLogin) -> None | ValueError:
        # amazonq-ignore-next-line
        senha_do_banco = self.__user_repo.select_by_nickname(user.nickname).senha_hash
        if not HashSenha(user.senha_login, senha_do_banco).is_equal():
            raise ValueError('Senha fornecida pelo front não condiz com a senha do banco')
        
        RedCache(cache_key=COMMON_KEYS['USUARIO_LOGADO'], cache_data=user.nickname).processar_cache()
    
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
