<template>
    <button type="button" class="btn btn-outline-success" data-bs-toggle="modal"
        :data-bs-target="`#modalEdit${tarefaId}`">
        <i class="bi bi-pencil-square"></i>
        Editar
    </button>

    <div class="modal fade" :id="`modalEdit${tarefaId}`" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" :id="`modalEditLabel${tarefaId}`">Editar Tarefa</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="formEdit">
                        <div class="form-floating titulo">
                            <input type="text" class="form-control" placeholder="Leave a comment here"
                                id="floatingInput" v-model="tarefa_titulo_edit">
                            <label for="floatingInput">Titulo</label>
                        </div>
                        <div class="form-floating desc">
                            <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea"
                                v-model="tarefa_desc_edit"></textarea>
                            <label for="floatingTextarea">Descrição</label>
                        </div>
                        <div class="form-floating status">
                            <select class="form-select" id="floatingSelect" aria-label="Floating label select example"
                                v-model="tarefa_status_edit">
                                <option value="pendente">Pendente</option>
                                <option value="em_andamento">Em andamento</option>
                                <option value="concluida">Concluído</option>
                            </select>
                            <label for="floatingSelect">Status</label>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-success" data-bs-dismiss="modal" @click="editarTarefa">Salvar
                        alterações</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CompEditarTarefas',
    emits: ['tarefa-editada'],
    data() {
        return {
            tarefa_titulo_edit: this.tarefaTitulo,
            tarefa_desc_edit: this.tarefaDesc,
            tarefa_status_edit: this.tarefaStatus
        }
    },
    props: {
        tarefaId: {
            type: Number,
            required: true
        },
        tarefaDesc: {
            type: String,
            required: true
        },
        tarefaStatus: {
            type: String,
            required: true
        },
        tarefaTitulo: {
            type: String,
            required: true
        }
    },
    methods: {
        async editarTarefa() {
            try {
                const dados = {
                    id: this.tarefaId,
                    titulo: this.tarefa_titulo_edit,
                    descricao: this.tarefa_desc_edit,
                    status: this.tarefa_status_edit
                }
                await axios.put('http://127.0.0.1:8000/api/tarefa/update', dados)
                this.$emit('tarefa-editada')
            } catch (error) {
                console.log('Erro ao editar tarefa: ', error)
            }
        }
    }
}
</script>

<style src="../assets/static.css"></style>
<style>
#formEdit {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 5px;

    .titulo {
        grid-column: 1/3;
        grid-row: 1/2;
    }

    .desc {
        grid-column: 3/-1;
        grid-row: 1/-1;
        display: flex;
        flex-direction: column;

        textarea {
            flex: 1;
            min-height: 100px;
        }
    }
    
    .status {
        grid-column: 1/3;
        grid-row: 2/-1;
    }
}
</style>