<template>
    <section id="campoAlterarDados">
        <div class="row">
            <div class="col-12">
                <button type="button" class="btn btn-danger" data-bs-target="#confirmDeleteUser"
                    data-bs-toggle="modal">Deletar conta</button>
            </div>
        </div>
    </section>
    <div class="modal fade" id="confirmDeleteUser" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="alert alert-danger" role="alert">
                        ESTA AÇÃO NÃO TEM VOLTA
                    </div>
                    <div class="alert alert-light" role="alert">
                        Escreva no campo abaixo a seguinte frase sem aspas<br /> "Eu quero deletar permanentemente a
                        minha conta"
                    </div>
                    <div class="mb-3">
                        <input type="text" class="form-control" :class="{'is-invalid': inputInvalid, 'is-valid': !inputInvalid}" v-model="confirmDeleteInput" @input="confirm_delete_escrito" ref="inputConfirmDeleteRef">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal" :disabled="disableDelete" @click="deletar_conta">Deletar</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompDeletarUser',
    data() {
        return {
            confirmDeleteInput: '',
            disableDelete: true,
            inputInvalid: true
        }
    },
    methods: {
        confirm_delete_escrito() {
            if (this.confirmDeleteInput === 'Eu quero deletar permanentemente a minha conta') {
                this.inputInvalid = false
                this.disableDelete = false
            } else {
                this.inputInvalid = true
                this.disableDelete = true
            }
        },
        async deletar_conta() {
            try {
                await axios.delete('http://127.0.0.1:8000/api/user/delete')
                this.$router.push('/login')
            } catch (error) {
                console.log('Erro', error)
            }
        }
    }
}
</script>

<style src="../assets/static.css"></style>