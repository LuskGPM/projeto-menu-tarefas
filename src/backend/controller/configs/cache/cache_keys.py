# Padronização das chaves de cache Redis

# Entidades
ENTITIES = {
    'TAREFA': 'TAREFA',
    'USUARIO': 'USUARIO'
}

# Status das tarefas
TAREFA_STATUS = {
    'PENDENTE': 'pendente',
    'EM_ANDAMENTO': 'em_andamento', 
    'CONCLUIDA': 'concluida'
}

# Status do usuário
USUARIO_STATUS = {
    'LOGADO': 'logado',
    'OFFLINE': 'offline'
}

# Função helper para gerar chaves
def build_cache_key(entity: str, status: str) -> str:
    return f"{entity}:{status}"

# Chaves pré-definidas mais usadas
COMMON_KEYS = {
    'TAREFAS_PENDENTES': build_cache_key(ENTITIES['TAREFA'], TAREFA_STATUS['PENDENTE']),
    'TAREFAS_CONCLUIDAS': build_cache_key(ENTITIES['TAREFA'], TAREFA_STATUS['CONCLUIDA']),
    'TAREFAS_EM_ANDAMENTO': build_cache_key(ENTITIES['TAREFA'], TAREFA_STATUS['EM_ANDAMENTO']),
    'USUARIO_LOGADO': build_cache_key(ENTITIES['USUARIO'], USUARIO_STATUS['LOGADO'])
}