<template>
    <header>

        <nav class="navbar navbar-expand-xxl">
            <div class="container-fluid">
                <a class="navbar-brand" href="#" style="opacity: .7;">{{ nomeUser }}</a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <button @click="redirect_tarefas" class="nav-link"
                                :class="{ 'nav-link-active': telaAtual == 'principal' }">Tarefas</button>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Usuario
                            </a>
                            <ul class="dropdown-menu">
                                <li>
                                    <button class="dropdown-item perfil" @click="redirect_user">
                                        <i class="bi bi-person"></i>
                                        Perfil
                                    </button>
                                </li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li>
                                    <button class="dropdown-item" @click="logout" style="color: red;">
                                        <i class="bi bi-box-arrow-left"></i>
                                        Sair
                                    </button>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!--
        <nav class="navbar">
            <div class="navbar-brand">
                <span>{{ nomeUser }}</span>
            </div>
            <div class="navbar-menu">
                <button class="nav-btn" @click="redirect_tarefas">
                    <i class="bi bi-list-task"></i>
                    Tarefas
                </button>
                <button class="nav-btn" @click="redirect_user">
                    <i class="bi bi-person"></i>
                    Perfil
                </button>
                <button class="nav-btn logout-btn" @click="logout">
                    <i class="bi bi-box-arrow-left"></i>
                    Sair
                </button>
            </div>
        </nav> -->
    </header>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompHeader',
    data() {
        return {
            nomeUser: 'Usuario',
            telaAtual: ''
        }
    },
    created() {
        this.buscar_nome()
        if (this.$route.path == '/tela-principal') {
            this.telaAtual == 'principal'
        } else {
            this.telaAtual == 'perfil'
        }
    },

    methods: {
        async logout() {
            try {
                await axios('http://127.0.0.1:8000/api/user/logout')
                console.log('Sessão encerrada')
                this.$router.push('/login')
            } catch (error) {
                console.log('erro:', error)
            }
        },
        async buscar_nome() {
            try {
                const response = await axios('http://127.0.0.1:8000/api/user/me')
                const dados = response.data
                this.nomeUser = dados['nome']

            } catch (error) {
                console.log(error)
                this.nomeUser = 'Chefia'
            }
        },
        redirect_user() {
            this.$router.push('/tela-user')
        },
        redirect_tarefas() {
            this.$router.push('/tela-principal')
        }
    }
}
</script>

<style>
@import url('../assets/static.css');

.navbar {
    background-color: var(--azul-escuro);
    box-shadow: 3px 3px 7px rgba(69, 69, 69, 0.211);
    height: 80px;

    .perfil {
        color: var(--azul-escuro);
    }

    a,
    button,
    li {
        color: var(--branco-painel-texto);

        &:hover,
        &:focus {
            color: var(--azul-claro);
        }
    }

    li {
        font-size: 1em;
    }

}

.menu-items {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1em;
}

.menu-items .span {
    color: var(--azul-escuro);
}

.menu-items .span.exit {
    color: var(--vermelho-claro);
}
</style>
