<template>
    <main id="login-main">
        <section id="login-section">
            <form id="login-grid">
                <div id="logo">
                    <span class="material-symbols-outlined">
                        login
                    </span>
                </div>
                <div id="login-inputs">
                    <p ref="alertLogin"></p>

                    <label for="loginNickname" class="label">Nickname</label>
                    <input type="text" class="input" id="loginNickname" v-model="nickname" />

                    <label for="loginSenha" class="label">Senha</label>
                    <input type="password" class="input" id="loginSenha" v-model="senha" />

                    <input type="submit" value="Login" class="input" id="submit" @click.prevent="login"/>
                </div>
                <div id="login-cadastrar">
                    <router-link to="/cadastro" class="link">
                        Não tem conta? Cadastre-se
                    </router-link>
                </div>
            </form>
        </section>
        <CompDireitosAutorais />
    </main>
</template>

<script>
import axios from 'axios';
import { useAuth } from '../composables/useAuth';
import CompDireitosAutorais from './CompDireitosAutorais.vue';

export default {
    name: 'CompLogin',
    components: {
        CompDireitosAutorais
    },
    async created() {
        const { verificarSessao } = useAuth()
        if (await verificarSessao()) {
            this.$router.push('/tela-principal')
        }
    },
    data() {
        return {
            nickname: '',
            senha: ''
        }
    },
    methods: {
        async login() {
            const dados = {
                nickname: this.nickname,
                senha_login: this.senha
            }
            try {
                await axios.post('http://127.0.0.1:8000/api/user/login', dados)
                this.$router.push('/tela-principal')
            } catch {
                this.$refs.alertLogin.innerText = 'Usuário ou senha incorretos'
                this.$refs.alertLogin.style.color = 'red'
            }
        }
    }
}
</script>

<style src="../style/CompLogin.css"></style>
