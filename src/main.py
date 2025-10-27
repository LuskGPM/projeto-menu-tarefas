from backend.controller import TarefaControler
from backend.view.schemas import TarefaCreate
"""
# amazonq-ignore-next-line
usuario = UsuarioCreate(nome = 'Lucas Melo', nickname = 'LuskGPM', senha_front = 'lgm256974')

uc = UsuarioControler()
# amazonq-ignore-next-line
uc.processar_cadastro(usuario)
"""

tarefa = TarefaCreate(
    titulo='Minha primeira tarefa',
    descricao='Teste de cadastro da primeira tarefa',
    status='pendente',
    prioridade='baixa',
    categoria_id=2
)

tc = TarefaControler()
tc.processar_tarefa(tarefa)
