<template>
    <header>
        <nav class="navbar">
            <button class="btn" data-bs-toggle="offcanvas" data-bs-target="#sidebar">
                <i class="bi bi-list span"></i>
            </button>

            <div class="offcanvas offcanvas-start" tabindex="-1" id="sidebar">
                <div class="offcanvas-header">
                    <h5 class="offcanvas-title">{{ nomeUser }}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
                </div>
                <div class="offcanvas-body">
                    <div class="menu-items mb-4" @click="redirect_user">
                        <i class="bi bi-person span"></i>
                        Perfil
                    </div>
                    <div class="menu-items mb-4" @click="redirect_tarefas">
                        <i class="bi bi-list-task span"></i>
                        Tarefas
                    </div>
                    <div class="menu-items" @click="logout">
                        <i class="bi bi-box-arrow-left span exit"></i>
                        Sair
                    </div>
                </div>
            </div>
        </nav>
    </header>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompHeader',
    data() {
        return {
            nomeUser: ''
        }
    },
    created() {
        this.buscar_nome()
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
    padding: 20px;
    box-shadow: 3px 3px 7px rgba(69, 69, 69, 0.211);
    position: sticky;
    top: 0;
}

.span {
    font-size: 3em !important;
    cursor: pointer;
    color: var(--branco-painel-texto);
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
