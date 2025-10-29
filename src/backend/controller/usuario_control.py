from ..view.schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate
from ..model.mysql_db import Usuario, UsuarioRepository
from .configs import RedisControl as RedCache, HashSenha, COMMON_KEYS

class UsuarioControler(UsuarioRepository):
    async def processar_update(self, user: UsuarioUpdate) -> None:
        # Busca dados da sessão
        sessao = RedCache(cache_key = COMMON_KEYS['USER'])
        dados_sessao = await sessao.receber_cache()
        if not dados_sessao:
            raise ValueError('Usuário não está logado')
        
        # Busca usuário pelo ID
        dados_usuario = await self._select_by_id(Usuario, dados_sessao['id'])
        if not dados_usuario:
            raise ValueError('Usuário não encontrado')
        
        # Valida senha atual
        if not HashSenha(user.senha_antiga, dados_usuario.senha_hash).is_equal():
            raise ValueError('Senha atual incorreta')
        
        # Prepara dados para atualização
        update_data = user.model_dump(exclude_unset=True, exclude={'senha_antiga', 'senha_nova'})
        
        # Processa nova senha se fornecida
        if user.senha_nova:
            update_data['senha_hash'] = HashSenha(user.senha_nova).hash()
        
        # Atualiza campos no objeto
        for key, value in update_data.items():
            setattr(dados_usuario, key, value)
        
        # Salva no banco
        await self._update(dados_usuario)
        
        # Atualiza cache da sessão se nickname mudou
        if 'nickname' in update_data:
            dados_sessao['nickname'] = update_data['nickname']
            cache_atualizado = RedCache(cache_key = COMMON_KEYS['USER'], cache_data = dados_sessao)
            await cache_atualizado.processar_cache()
    
    async def processar_cadastro(self, user: UsuarioCreate) -> None:
        # Hash da senha
        senha_hash = HashSenha(user.senha_front).hash()
        
        new_user = Usuario(
            nome = user.nome,
            nickname = user.nickname,
            senha_hash = senha_hash
        )
        
        # Insere novo usuário
        await self._insert(new_user)
    
    async def verificar_disponibilidade_nickname(self, nickname: str) -> bool:
        # Verificar se o nickname já existe
        nickname_no_banco = await self._select_by_nickname(nickname)
        if nickname_no_banco: # Se o nickname for encontrado, retorna True
            return True
        return False
    
    async def processar_login(self, user: UsuarioLogin) -> None | ValueError:
        user_banco = await self._select_by_nickname(user.nickname)
        senha_user = user_banco.senha_hash
        if not HashSenha(user.senha_login, senha_user).is_equal():
            raise ValueError('<ControlerUser>: Senha fornecida pelo front não condiz com a senha do banco')
        user_session = {
            'id': user_banco.id,
            'nome': user_banco.nome,
            'nickname': user_banco.nickname
        }
        cache = RedCache(cache_key = COMMON_KEYS['USER'], cache_data = user_session)
        await cache.processar_cache()
        
    async def encerrar_sessao(self) -> str:
        cache = RedCache(cache_key=COMMON_KEYS['USER'])
        delete_cache = await cache.excluir_cache()
        if delete_cache:
            return 'Sessão encerrada com sucesso'
        return 'Sessão já estava encerrada'
    
    async def esta_logado(self) -> bool:
        cache = RedCache(COMMON_KEYS['USER'])
        sessao_ativa = await cache.receber_cache()
        if sessao_ativa:
            await cache.renovar_cache()
            return True
        return False
    
    async def obter_nickname_sessao(self) -> str | None:
        cache = RedCache(COMMON_KEYS['USER'])
        dados_sessao = await cache.receber_cache()
        if dados_sessao:
            return dados_sessao['nickname']

    async def obter_dados_sessao(self) -> dict | None:
        cache = RedCache(COMMON_KEYS['USER'])
        return await cache.receber_cache()
    
    async def obter_nome_sessao(self) -> str | None:
        cache = RedCache(COMMON_KEYS['USER'])
        dados_sessao = await cache.receber_cache()
        if dados_sessao:
            return dados_sessao['nome']
