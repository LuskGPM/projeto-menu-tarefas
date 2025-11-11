<template>
    <header>
        <nav class="navbar">
            <div id="header-sanduiche">
                <span class="material-symbols-outlined span" 
               style="padding-left: 10px;" @click="toggle_menu">
                    menu
                </span>
            </div>

            <aside v-if="mostrarSideBar" class="overlay" @click="fechar_menu"></aside>

            <aside class="sidebar" :class="{ 'sidebar-aberto': mostrarSideBar }">
                <div id="header-close" @click="fechar_menu" class="menu-items">
                    <p>Atalhos de usuário</p>
                    <span class="material-symbols-outlined span">
                        close
                    </span>
                </div>
                <div id="header-perfil" class="menu-items">
                    <span class="material-symbols-outlined span">
                        account_circle
                    </span>
                    Perfil
                </div>
                <div id="header-logout" class="menu-items" @click="logout">
                    <span class="material-symbols-outlined span">
                        logout
                    </span>
                    Sair
                </div>
            </aside>
        </nav>
    </header>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompHeader',
    data() {
        return {
            mostrarSideBar: false
        }
    },
    methods: {
        toggle_menu() {
            this.mostrarSideBar = !this.mostrarSideBar
        },
        fechar_menu() {
            this.mostrarSideBar = false
        },
        async logout() {
            try {
                await axios('http://127.0.0.1:8000/api/user/logout')
                console.log('Sessão encerrada')
                this.$router.push('/login')
            } catch (error) {
                console.log('erro:', error)
            }
        }
    }
}
</script>

<style>
@import url('../assets/static.css');

.navbar {
    background-color: var(--azul-claro);
    padding: 20px;
    box-shadow: 3px 3px 7px rgba(69, 69, 69, 0.211);
    position: sticky;
    top: 0;
}

.span {
    font-size: 3em !important;
    cursor: pointer;
    color: var(--azul-escuro);
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    z-index: 998;
}

.sidebar {
    position: fixed;
    top: 0;
    left: -300px;
    /* escondido inicialmente */
    width: 300px;
    height: 100vh;
    background: white;
    z-index: 999;
    transition: left 0.3s ease-out;
    box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);

    .menu-items {
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .menu-items:first-child {
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;
        font-size: .7em;

        .span {
            box-sizing: border-box;
            font-size: 2.5em !important;
            border: 2px solid transparent;

            &:hover {
                border-radius: 10px;
                border: 2px solid var(--azul-escuro);
            }
        }
    }

    #header-logout .span {
        color: var(--vermelho-claro);
    }
}

.sidebar-aberto {
    left: 0;
    /* aparece quando ativo */
}
</style>
