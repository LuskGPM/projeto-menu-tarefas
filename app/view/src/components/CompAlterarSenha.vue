<template>
    <section id="campoAlterarSenha" class="mb-3">
        <div class="accordion">
            <div class="accordion-item">
                <div class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseSenha" aria-expanded="false">
                        Alterar Senha
                    </button>
                </div>
                <div id="collapseSenha" class="accordion-collapse collapse">
                    <div class="accordion-body">
                        <div class="row g-3">
                            <div class="form-floating col-md-6">
                                <input type="password" class="form-control" id="inputSenha" placeholder="Senha"
                                    v-model="senha_front" :disabled="loading">
                                <label for="inputSenha">Verificar Senha</label>
                            </div>
                            <div v-if="mostrarButton" class="col-md-6 d-flex align-items-center">
                                <button class="btn btn-primary" @click="verificar_senha">Verificar</button>
                            </div>
                            <div v-else-if="loading" class="spinner-border col-md-6" role="status"
                                style="align-self: center;">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                            <div class="col-12 d-flex align-items-center">
                                <p ref="alertSenhaRef">{{ alertSenha }}</p>
                            </div>
                        </div>
                        <div class="row g-3">
                            <div class="form-floating col-md-6">
                                <input type="password" class="form-control" id="inputNovaSenha" placeholder="Senha"
                                    :disabled="bloquearAlterarSenha" v-model="senha_nova">
                                <label for="inputNovaSenha">Nova senha</label>
                            </div>
                            <div class="form-floating col-md-6">
                                <input type="password" class="form-control" id="inputConfirmSenha" placeholder="Senha"
                                    :disabled="bloquearAlterarSenha" @input="verificar_senhas_iguais"
                                    v-model="senha_confirm">
                                <label for="inputConfirmSenha">Confirme a senha</label>
                            </div>
                            <div class="col-md-6" style="color: red;" v-show="alertUpSenhaExists">
                                <p>{{ alertNovaSenha }}</p>
                            </div>
                            <div class="col-md-6" v-show="alertUpSenhaExists">
                                <p ref="alertConfirmSenhaRef">{{ alertConfirmSenha }}</p>
                            </div>
                            <div class="col-12 d-flex">
                                <button type="button" class="btn btn-success" :disabled="bloquearAlterarSenha"
                                    @click="alterar_senha">Salvar</button>
                                <div v-if="loadingUpSenha" class="spinner-border col-md-6" role="status"
                                    style="align-self: center; margin-left: 10px;">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompAlterarSenha',
    data() {
        return {
            senha_front: '',
            senha_nova: '',
            senha_confirm: '',
            alertSenha: '',
            alertNovaSenha: '',
            alertConfirmSenha: '',
            mostrarButton: true,
            bloquearAlterarSenha: true,
            loading: false,
            loadingUpSenha: false,
            alertUpSenhaExists: false
        }
    },
    methods: {
        async verificar_senha() {
            if (this.senha_front.length < 8) {
                this.alertSenha = 'Senha deve ter pelo menos 8 dígitos'
                this.$refs.alertSenhaRef.style.color = 'red'
                return
            }
            try {
                this.mostrarButton = false
                this.loading = true
                const dados = {
                    senha_do_front: this.senha_front
                }
                const response = await axios.post('http://127.0.0.1:8000/api/user/validar-senha', dados)
                this.loading = false
                this.mostrarButton = true
                if (response.data.message == 'true') {
                    this.bloquearAlterarSenha = false
                    this.alertSenha = 'Autorizado'
                    this.$refs.alertSenhaRef.style.color = 'green'
                    this.senha_front = ''
                } else {
                    this.mostrarButton = true
                    this.alertSenha = 'Senha incorreta - Não autorizado'
                    this.$refs.alertSenhaRef.style.color = 'red'
                }
            } catch (error) {
                this.loading = false
                console.log('Erro ao validar senha: ', error)
                this.bloquearAlterarSenha = true
                this.alertSenha = 'Erro ao validar senha'
                this.$refs.alertSenhaRef.style.color = 'red'
            }
        },
        async alterar_senha() {
            this.alertConfirmSenha = ''
            if (this.senha_nova.length < 8) {
                this.alertUpSenhaExists = true
                this.alertNovaSenha = 'A senha deve ter no mínimo 8 dígitos'
                this.senha_nova = ''
                this.senha_confirm = ''
                return
            } else if (this.senha_nova != this.senha_confirm) {
                this.alertNovaSenha = 'As senhas não conferem!'
                return
            }
            this.loadingUpSenha = true
            try {
                const dados = {
                    senha_nova: this.senha_nova
                }
                await axios.put('http://127.0.0.1:8000/api/user/update', dados)
                this.loadingUpSenha = false
                this.senha_nova = ''
                this.senha_confirm = ''
                this.alertConfirmSenha = 'Senha alterada com sucesso!'
                this.bloquearAlterarSenha = true
                // Limpar após 3 segundos
                setTimeout(() => this.alertNovaSenha = '', 5000)
            } catch (error) {
                this.loadingUpSenha = false
                console.log('erro: ', error)
                this.alertNovaSenha = 'Erro ao alterar senhas'
            }
        },
        verificar_senhas_iguais() {
            this.alertNovaSenha = ''
            this.alertUpSenhaExists = true
            if (this.senha_confirm != this.senha_nova) {
                this.alertConfirmSenha = 'Senhas não conferem'
                this.$refs.alertConfirmSenhaRef.style.color = 'red'
            } else {
                this.alertConfirmSenha = 'Tudo ok!'
                this.$refs.alertConfirmSenhaRef.style.color = 'green'
            }
        }
    }
}
</script>

<style>
label {
    margin-left: 5px !important;
}
</style>