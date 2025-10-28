from ..view.schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate
from ..model.mysql_db import Usuario, UsuarioRepository
from .configs import RedisControl as RedCache, HashSenha, COMMON_KEYS

class UsuarioControler(UsuarioRepository):
    async def processar_update(self, user: UsuarioUpdate) -> None | ValueError:
        # Busca o nickname na sessão em cache
        sessao = RedCache(COMMON_KEYS['USUARIO_LOGADO'])
        nickname_sessao = await sessao.receber_cache()
        dados_usuario = await self.select_by_nickname(nickname_sessao)
        # Senha do banco para validar o update
        senha_do_banco = dados_usuario.senha_hash
        ## Validação da senha do banco com a senha fornecida
        if not HashSenha(user.senha_antiga, senha_do_banco).is_equal():
            raise ValueError('<ControlerUser>: Senha incorreta')
        
        new_dados_usuario = user.model_dump(exclude_unset=True) # Excluí dados não fornecidos
        # Verifica se existe uma nova senha e trata ela
        if 'senha_nova' in new_dados_usuario:
            new_dados_usuario['senha_hash'] = HashSenha(new_dados_usuario['senha_nova']).hash()
            del new_dados_usuario['senha_nova']
        new_dados_usuario.pop('senha_antiga', None)
        
        for key, value in new_dados_usuario.items():
            setattr(dados_usuario, key, value)
        await self.update(dados_usuario)
    
    async def processar_cadastro(self, user: UsuarioCreate) -> None:
        # Cadastra novo usuário
        ## Hash da senha
        senha_hash = HashSenha(user.senha_front).hash()
        new_user = Usuario(
            nome = user.nome,
            nickname = user.nickname,
            senha_hash = senha_hash
        )
        ## Insere novo usuário
        await self.insert(new_user)
    
    async def verificar_disponibilidade_nickname(self, nickname: str) -> bool:
        # Verificar se o nickname já existe
        nickname_no_banco = await self.select_by_nickname(nickname)
        if nickname_no_banco: # Se o nickname for encontrado, retorna False
            return False
        return True
    
    async def autenticar_usuario(self, user: UsuarioLogin) -> None | ValueError:
        # amazonq-ignore-next-line
        user_banco = await self.select_by_nickname(user.nickname)
        senha_user = user_banco.senha_hash
        if not HashSenha(user.senha_login, senha_user).is_equal():
            raise ValueError('<ControlerUser>: Senha fornecida pelo front não condiz com a senha do banco')
        cache = RedCache(cache_key=COMMON_KEYS['USUARIO_LOGADO'], cache_data=user.nickname)
        await cache.processar_cache()
    
    async def encerrar_sessao(self) -> str:
        cache = RedCache(cache_key=COMMON_KEYS['USUARIO_LOGADO'])
        delete_cache = await cache.excluir_cache()
        if delete_cache:
            return 'Sessão encerrada com sucesso'
        return 'Sessão já estava encerrada'
    
    async def esta_logado(self) -> bool:
        cache = RedCache(COMMON_KEYS['USUARIO_LOGADO'])
        sessao_ativa = await cache.receber_cache()
        if sessao_ativa:
            await cache.renovar_cache()
            return True
        return False
    
    async def obter_nickname_sessao(self) -> str | None:
        cache = RedCache(COMMON_KEYS['USUARIO_LOGADO'])
        cache_nickname = await cache.receber_cache()
        if cache_nickname:
            return cache_nickname
