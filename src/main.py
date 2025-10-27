from backend.controller import UsuarioControler
from backend.view.schemas import UsuarioCreate

# amazonq-ignore-next-line
usuario = UsuarioCreate(nome = 'Lucas Melo', nickname = 'LuskGPM', senha_front = 'lgm256974')

uc = UsuarioControler()
# amazonq-ignore-next-line
uc.processar_cadastro(usuario)
