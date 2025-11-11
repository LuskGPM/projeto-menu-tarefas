<template>
    <button type="button" class="btn btn-outline-danger" data-bs-toggle="modal"
        :data-bs-target="`#confirmDelete${tarefaId}`">
        <i class="bi bi-trash3"></i>
        Delete
    </button>

    <div class="modal fade" :id="`confirmDelete${tarefaId}`" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Confirmar exclusão</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Tem certeza que quer excluir "{{ tarefaTitulo }}"?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="button" class="btn btn-danger" @click="deletarTarefa"
                        data-bs-dismiss="modal">Deletar</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompExcluirTarefas',
    emits: ['tarefa-excluida'],
    props: {
        tarefaId: {
            type: Number,
            required: true
        },
        tarefaTitulo: {
            type: String,
            required: true
        },
        tarefaPrioridade: {
            type: String,
            required: true
        }
    },

    methods: {
        async deletarTarefa() {
            try {
                const dados = {
                    tarefa_id: this.tarefaId,
                    prioridade: this.tarefaPrioridade
                }
                await axios.delete('http://127.0.0.1:8000/api/tarefa/delete', {
                    data: dados
                })
                alert('Tarefa excluída com sucesso')
                this.$emit('tarefa-excluida')
            } catch (error) {
                console.log('Erro ao deletar tarefa: ', error)
            }
        }

    }
}
</script>

<style src="../assets/static.css"></style>
