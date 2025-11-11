from ..api.schemas import UsuarioCreate, UsuarioLogin, UsuarioUpdate, UsuarioValidarSenha
from ..model.mysql_db import Usuario, UsuarioRepository
from .configs import RedisControl as RedCache, HashSenha, COMMON_KEYS

class UsuarioControler(UsuarioRepository):
    
    async def verificar_igualdade_nas_senhas(self, user: UsuarioValidarSenha) -> bool:
        sessao = RedCache(cache_key = COMMON_KEYS['USER'])
        dados_sessao = await sessao.receber_cache()
        
        dados_usuario = await self._select_by_id(Usuario, dados_sessao['id'])
        senha_do_banco = dados_usuario.senha_hash
        
        if HashSenha(user.senha_do_front, senha_do_banco).is_equal():
            return True
        return False
    
    async def processar_update(self, user: UsuarioUpdate) -> None:
        # Busca dados da sessão
        sessao = RedCache(cache_key = COMMON_KEYS['USER'])
        dados_sessao = await sessao.receber_cache()
        # Busca usuário pelo ID
        dados_usuario = await self._select_by_id(Usuario, dados_sessao['id'])
        if not dados_usuario:
            raise ValueError('Usuário não encontrado')
        
        update_data = user.model_dump(exclude_unset=True, exclude={'senha_nova'})

        if user.senha_nova:
            update_data['senha_hash'] = HashSenha(user.senha_nova).hash()
            
        
        # Atualiza campos no objeto
        for key, value in update_data.items():
            setattr(dados_usuario, key, value)
    
        await self._update(dados_usuario)
        
        # Atualiza cache da sessão com dados mais recentes
        if 'nickname' in update_data or 'nome' in update_data:
            if 'nickname' in update_data:
                dados_sessao['nickname'] = update_data['nickname']
            if 'nome' in update_data:
                dados_sessao['nome'] = update_data['nome']
    
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
        
        # Busca do banco !importante para pegar o ID
        user_banco = await self._select_by_nickname(user.nickname)
        user_session = {
            'id': user_banco.id,
            'nome': user_banco.nome,
            'nickname': user_banco.nickname
        }
        cache = RedCache(cache_key = COMMON_KEYS['USER'], cache_data = user_session)
        await cache.processar_cache()
        
    async def processar_login(self, user: UsuarioLogin) -> None | ValueError:
        user_banco = await self._select_by_nickname(user.nickname)
        
        if not user_banco:
            raise ValueError('Senha ou Usuário incorretos')
        if not HashSenha(user.senha_login, user_banco.senha_hash).is_equal():
            raise ValueError('Senha ou Usuario incorretos')
        
        user_session = {
            'id': user_banco.id,
            'nome': user_banco.nome,
            'nickname': user_banco.nickname
        }
        cache = RedCache(cache_key = COMMON_KEYS['USER'], cache_data = user_session)
        await cache.processar_cache()
        
    async def processar_delete(self, user_id: int) -> None:
        await self._delete(Usuario, user_id)
        await self.encerrar_sessao()
    
    async def verificar_disponibilidade_nickname(self, nickname: str) -> bool:
        # Verificar se o nickname já existe
        return await self._nickname_exists(nickname)
    
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
            await cache.renovar_cache()  # Renova quando usado em rotas ativas
            return True
        return False

    async def obter_dados_sessao(self) -> dict | None:
        cache = RedCache(COMMON_KEYS['USER'])
        return await cache.receber_cache()
        