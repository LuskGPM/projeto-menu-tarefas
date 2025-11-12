<template>
    <section id="CampoDadosUser">
        <div class="row">
            <div class="form-floating mb-3 col-md-6">
                <input type="text" class="form-control" id="floatingUsername" placeholder="name@example.com"
                    :disabled="disabledInputs" v-model="nomeUser">
                <label for="floatingUsername">Username</label>
            </div>
            <div class="form-floating mb-3 col-md-6">
                <input type="text" class="form-control" id="floatingNickname" placeholder="Nickname"
                    :disabled="disabledInputs" v-model="nicknameUser">
                <label for="floatingNickname">Nickname</label>
            </div>
            <div class="col-12 d-flex mb-3">
                <button type="button" class="btn btn-success" @click="editarCampos">
                    <i class="bi bi-pencil-square"></i>
                    Editar
                </button>
                <button type="button" class="btn btn-primary" @click="atualizar_dados" style="margin-left: 10px; position: static;"
                    :disabled="disabledSalvar">
                    Salvar
                </button>
            </div>
            <div class="col-12">
                <div class="alert alert-info" role="alert" v-if="alert">
                    {{ messageAlert }}
                </div>
                <div v-if="loading" class="spinner-border col-md-6" role="status"
                    style="align-self: start;">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ComDadosUser',
    data() {
        return {
            nomeUser: null,
            nicknameUser: null,
            disabledInputs: true,
            disabledSalvar: true,
            alert: false,
            messageAlert: '',
            nicknameInMemory: '',
            loading: false
        }
    },
    created() {
        this.dados()
    },
    methods: {
        editarCampos() {
            this.disabledInputs = !this.disabledInputs
            this.disabledSalvar = !this.disabledSalvar
        },
        async dados() {
            try {
                const response = await axios('http://127.0.0.1:8000/api/user/me')
                this.nomeUser = response.data.nome
                this.nicknameUser = response.data.nickname
                this.nicknameInMemory = response.data.nickname
            } catch (error) {
                console.log('erro: ', error)
            }
        },
        async atualizar_dados() {
            let dados = {}
            if (this.nicknameUser == this.nicknameInMemory) {
                dados = {
                    nome: this.nomeUser
                }
            } else {
                dados = {
                    nome: this.nomeUser,
                    nickname: this.nicknameUser
                }
            }
            try {
                this.alert = false
                this.loading = true
                const response = await axios.put('http://127.0.0.1:8000/api/user/update', dados)
                this.loading = false
                this.alert = true
                this.messageAlert = response.data.message
            } catch (error) {
                this.loading = false
                this.alert = true
                this.messageAlert = 'Erro ao atualizar dados'
            } finally {
                setTimeout(() => this.alert = '', 10000)
            }
        }
    }
}
</script>

<style src="../assets/static.css"></style>
<style>
label {
    margin-left: 10px !important;
}
</style>