<template>
    <main id="cad-main">
        <section id="cad-section">
            <div id="cad-grid">
                <div id="logo">
                    <span class="material-symbols-outlined">
                        app_registration
                    </span>
                </div>
                <div id="cad-inputs">
                    <label for="cadNome" class="label">Nome</label>
                    <input type="text" id="cadNome" class="input" v-model="nome" required />

                    <label for="cadNickname" class="label">Nickname</label>
                    <input type="text" id="cadNickname" class="input" v-model="nickname" required />

                    <label for="cadSenha" class="label">Senha</label>
                    <input type="password" id="cadSenha" class="input" v-model="senha" required minlength="8" />

                    <label for="cadConfirmSenha" class="label">Confirme a senha</label>
                    <input type="password" id="cadConfirmSenha" class="input" v-model="confsenha" @input="validarSenha"
                        ref="confirmSenha" required />
                    <p ref="alertcad"></p>

                    <input type="submit" id="cadButton" value="Cadastrar" class="input" @click="cadastrar" />
                </div>
                <div id="cad-login">
                    <router-link to="/login" class="link">
                        Possuí uma conta?
                    </router-link>
                </div>
            </div>
        </section>
        <CompDireitosAutorais />
    </main>
</template>

<script>
import CompDireitosAutorais from './CompDireitosAutorais.vue';
import axios from 'axios'

export default {
    name: 'CompCadastro',
    components: {
        CompDireitosAutorais
    },
    data() {
        return {
            nome: '',
            nickname: '',
            senha: '',
            confsenha: ''
        }
    },
    methods: {
        async cadastrar() {
            if (this.senha !== this.confsenha) {
                alert('Senhas diferentes')
                return
            }
            const dados = {
                nome: this.nome,
                nickname: this.nickname,
                senha_front: this.senha
            }
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/user/register', dados)
                this.$refs.alertcad.innerText = response.data.message
                this.$refs.alertcad.style.color = 'green'
                this.$router.push('/login')
            } catch (error) {
                this.$refs.alertcad.innerText = error.response.data.detail
                this.$refs.alertcad.style.color = 'red'
            }
        },
        validarSenha() {
            if (this.senha !== this.confsenha) {
                this.$refs.confirmSenha.style.borderColor = 'red'
                this.$refs.alertcad.innerText = 'Senhas não coincidem'
                this.$refs.alertcad.style.color = 'red'
            } else {
                this.$refs.confirmSenha.style.borderColor = 'green'
                this.$refs.alertcad.innerText = 'Senhas iguais'
                this.$refs.alertcad.style.color = 'green'
            }
        }
    }
}
</script>

<style src="../style/CompCadastro.css"></style>
<style src="../assets/static.css"></style>
