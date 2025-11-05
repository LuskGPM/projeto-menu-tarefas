<template>
    <main id="login-main">
        <section id="login-section">
            <div id="login-grid">
                <div id="logo">
                   <span class="material-symbols-outlined">
                        login
                    </span> 
                </div>
                <div id="login-inputs">
                    <label for="loginNickname" class="label">Nickname</label>
                    <input type="text" class="input" id="loginNickname" v-model="nickname"/>
                    
                    <label for="loginSenha" class="label">Senha</label>
                    <input type="password" class="input" id="loginSenha" v-model="senha"/>
                    
                    <input type="submit" value="Login" class="input" id="submit" @click="login"/>
                </div>
                <div id="login-cadastrar">
                    <router-link to="/cadastro" class="link">
                        Não tem conta? Cadastre-se
                    </router-link>
                </div>
            </div>
        </section>
        <CompDireitosAutorais/>
    </main>
</template>

<script>
    import axios from 'axios';
    import CompDireitosAutorais from './CompDireitosAutorais.vue';

    export default {
        name: 'CompLogin',
        components: {
            CompDireitosAutorais
        },
        async created() {
            await this.verificarSessao()
        },
        data() {
            return {
                nickname: '',
                senha: ''
            }
        },
        methods: {
            async verificarSessao() {
                try {
                    const response = await axios('http://127.0.0.1:8000/api/user/me')
                    const userId = response.data.id
                    this.$router.push(`/tarefa/id=${userId}`)
                } catch (error) {
                    console.log('Nenhuma sessão ativa no redis')
                }
            },
            async login() {
                const dados = {
                    nickname: this.nickname,
                    senha_login: this.senha
                }
                try {
                    const response = await axios.post('http://127.0.0.1:8000/api/user/login', dados)
                    alert(response.data.message)
                    this.$router.push('/tarefa')
                } catch (error) {
                    alert(error.response.data.detail)
                }
            }
        }
    }
</script>

<style src="../style/CompLogin.css"></style>
