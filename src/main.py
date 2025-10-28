import asyncio
from backend.controller import UsuarioControler, TarefaControler
from backend.view.schemas import UsuarioCreate, TarefaCreate

async def cadastroUser():
    # Segundo usuário - Amazon Q testando!
    usuario = UsuarioCreate(
        nome='Amazon Q Assistant',
        nickname='AmazonQ_Dev',
        senha_front='async_is_beautiful_2024'
    )
    controler = UsuarioControler()
    await controler.processar_cadastro(usuario)
    print(f"Usuário {usuario.nome} cadastrado com sucesso! 🚀")

async def cadastroTarefa():
    # Tarefa do Amazon Q - Sistema Async funcionando!
    tarefa = TarefaCreate(
        titulo='Implementar sistema async completo',
        descricao='Refatorar todo o backend para async/await com MySQL e Redis',
        status='concluida',
        prioridade='alta',
        categoria_id=3
    )
    controler = TarefaControler()
    await controler.processar_tarefa(tarefa)
    print(f'🚀 Tarefa: {tarefa.titulo} cadastrada com sucesso!')
    print('💪 Sistema async funcionando perfeitamente!')
    
async def dados_cache():
    tarefa_controler = TarefaControler()
    tarefa = await tarefa_controler.receber_tarefa_por_status('CONCLUIDA')
    print(tarefa)
    
if __name__ == '__main__':
    asyncio.run(dados_cache())
