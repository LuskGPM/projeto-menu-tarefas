# 📋 Menu de Tarefas

Sistema completo de gerenciamento de tarefas desenvolvido com Vue.js 3 e FastAPI, featuring autenticação segura, cache inteligente e design responsivo.

## 🚀 Tecnologias

**Frontend:**
- Vue.js 3 + Vue Router
- Bootstrap 5 + Bootstrap Icons
- Axios para integração com API
- Design responsivo mobile-first

**Backend:**
- FastAPI (Python async)
- SQLAlchemy async + MySQL
- Redis para cache e sessões
- bcrypt para hash de senhas

## ✨ Funcionalidades

### 🔐 Sistema de Usuários
- Cadastro e login seguro
- Autenticação com sessões Redis (30min)
- Alteração de dados pessoais
- Alteração de senha com validação
- Exclusão de conta
- Verificação de disponibilidade de nickname

### 📝 Gerenciamento de Tarefas
- CRUD completo de tarefas
- Categorização por prioridade (Alta, Média, Baixa)
- Status de tarefas (Pendente, Em Andamento, Concluída)
- Filtros por prioridade e status
- Busca por título
- Interface responsiva com cards coloridos

### 🎨 Interface Moderna
- Design mobile-first responsivo
- Menu hambúrguer com sidebar
- Loading states e spinners
- Feedback visual completo
- Modais para edição/exclusão
- Footer profissional

## 🏗️ Arquitetura

### Backend (FastAPI)
```
app/
├── backend/
│   ├── api/
│   │   ├── routes/          # Rotas da API
│   │   ├── schemas/         # Validações Pydantic
│   │   ├── dependencies/    # Middleware de auth
│   │   └── server/          # Configuração FastAPI
│   ├── controller/          # Lógica de negócio
│   │   └── configs/         # Cache e criptografia
│   └── model/
│       ├── mysql_db/        # Entidades e repositórios
│       └── redis_db/        # Cache Redis
└── app.py                   # Ponto de entrada
```

### Frontend (Vue.js)
```
view/
├── src/                     # Código fonte Vue.js
│   ├── components/          # Componentes Vue
│   ├── composables/         # Lógica reutilizável
│   ├── router/              # Configuração de rotas
│   ├── assets/              # CSS e imagens
│   └── style/               # Estilos específicos
├── dist/                    # Versão compilada (após build)
│   ├── index.html           # HTML otimizado
│   ├── css/                 # CSS minificado
│   └── js/                  # JavaScript compilado
└── public/                  # Arquivos estáticos
```

## 🔧 Instalação e Execução

### Pré-requisitos
- Python 3.8+
- Node.js 16+
- MySQL 8.0+
- **Redis próprio** (local ou nuvem)

### ⚠️ Importante - Configuração Redis
**Este sistema suporta apenas 1 usuário logado por vez.** Cada pessoa que usar o projeto deve configurar seu próprio Redis para evitar conflitos de sessão.

**Opções de Redis:**
- **Local**: Redis instalado na máquina
- **Nuvem**: Redis Cloud, Upstash, Railway, etc.

### Backend
```bash
# Clonar repositório
git clone <url-do-repositorio>
cd projeto-menu-tarefas

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar banco de dados
# 1. Copie os arquivos de exemplo:
cp app/backend/model/mysql_db/connection/connection_mysql.example.py connection_mysql.py
cp app/backend/model/redis_db/connection/connection_config.example.py connection_config.py

# 2. Configure suas credenciais nos arquivos copiados

# Executar servidor
python app/app.py
```

### Frontend
```bash
# Navegar para pasta do frontend
cd app/view

# Instalar dependências
npm install

# Executar em desenvolvimento
npm run serve

# Build para produção
npm run build

# Servir versão de produção
cd dist
npx serve .
# ou
python -m http.server 8080
```

## 📊 Banco de Dados

### Estrutura MySQL
```sql
-- Tabela de usuários
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    nickname VARCHAR(90) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL
);

-- Tabela de categorias
CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    cor VARCHAR(7) NOT NULL
);

-- Tabela de tarefas
CREATE TABLE tarefa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    descricao TEXT,
    status ENUM('pendente', 'em_andamento', 'concluida') NOT NULL,
    prioridade ENUM('baixa', 'media', 'alta') NOT NULL,
    categoria_id INT,
    usuario_id INT NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id) ON DELETE SET NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);
```

## 🔌 API Endpoints

### Usuários
- `POST /api/user/register` - Cadastro
- `POST /api/user/login` - Login
- `GET /api/user/logout` - Logout
- `GET /api/user/me` - Dados do usuário
- `PUT /api/user/update` - Atualizar dados
- `POST /api/user/validar-senha` - Validar senha
- `DELETE /api/user/delete` - Excluir conta

### Tarefas
- `POST /api/tarefa/register` - Criar tarefa
- `GET /api/tarefa/all` - Listar tarefas
- `PUT /api/tarefa/update` - Atualizar tarefa
- `DELETE /api/tarefa/delete` - Excluir tarefa

## 🎯 Características Técnicas

### Performance
- **Cache Redis** inteligente por usuário
- **Connection pooling** MySQL (pool_size=10)
- **Sliding sessions** com renovação automática (30min)
- **Build otimizado** com minificação e compressão

### Segurança
- **Hash bcrypt** para senhas (salt=12)
- **Sessões Redis** com expiração automática
- **Middleware de autenticação** FastAPI
- **Validações Pydantic** rigorosas
- **CORS** configurado adequadamente
- **Isolamento de sessões** (1 usuário por Redis)

### Arquitetura
- **MVC Pattern** bem definido
- **Repository Pattern** para acesso a dados
- **Dependency Injection** FastAPI
- **Clean Architecture** com SOLID principles
- **Type hints** completos
- **Frontend compilado** para HTML/CSS/JS puro

## 📱 Screenshots

### Tela de Login
![Tela de Login](screenshots/login.png)
*Interface limpa e responsiva com validação em tempo real*

### Tela de Cadastro
![Cadastro](screenshots/cadastro.png)
*Formulário de cadastro com validações em tempo real*

### Dashboard de Tarefas
![Dashboard](screenshots/dashboard.png)
*Cards coloridos por status, filtros inteligentes e busca por título*

### Perfil do Usuário
![Perfil](screenshots/perfil.png)
*Sistema completo de gerenciamento de conta com validações*

## 🚀 Deploy

### Desenvolvimento Local
```bash
# Backend (Terminal 1)
cd projeto-menu-tarefas
python app/app.py  # Roda na porta 8000

# Frontend (Terminal 2)
cd app/view
npm run serve      # Desenvolvimento na porta 8080
```

### Produção Local
```bash
# Backend (Terminal 1)
python app/app.py  # Roda na porta 8000

# Frontend (Terminal 2)
cd app/view
npm run build      # Gera pasta /dist
cd dist
npx serve .        # Serve arquivos estáticos
```

### Produção na Nuvem
```bash
# Frontend: GitHub Pages, Netlify, Vercel
# Backend: Heroku, Railway, Render
# MySQL: PlanetScale, AWS RDS
# Redis: Redis Cloud, Upstash
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Desenvolvedor

**LuskGPM**
- Sistema completo desenvolvido do zero
- Arquitetura full-stack moderna
- Foco em performance e segurança

---

## ⚙️ Configuração Necessária

### Arquivos de Configuração
Antes de executar, você deve criar e/ou configurar:

```bash
# MySQL
app/backend/model/mysql_db/connection/connection_mysql.py

# Redis (OBRIGATÓRIO - use seu próprio)
app/backend/model/redis_db/connection/connection_config.py

# Cors (localhost do servidor que roda o front)
app/backend/api/server/server.py
```

### Exemplo Redis Cloud (Gratuito)
```python
# connection_config.py
DATABASE_SETTINGS = {
    'URL': 'redis://default:sua-senha@seu-host.redis-cloud.com:12345'
}

TIMER_REDIS_EX = {
    'TIMER_30': 1800
}
```

---

## 🎉 Status do Projeto

✅ **PROJETO 100% CONCLUÍDO**

Sistema completo de gerenciamento de tarefas pronto para produção, com todas as funcionalidades implementadas e testadas.

**Stack**: Vue.js 3 + FastAPI + Redis + MySQL + Bootstrap 5

**Versão de Produção**: Arquivos compilados disponíveis em `/app/view/dist/`