COMMON_KEYS = {
    'TASK': 'tarefas',
    'USER': 'usuario'
}

STATUS_KEYS = {
    'EM_ANDAMENTO': 'em_andamento',
    'CONCLUIDA': 'concluida',
    'PENDENTE': 'pendente'
}

def criar_key(common, status):
    return f'{common}:{status}'
