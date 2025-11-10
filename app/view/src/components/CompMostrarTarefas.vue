<template>
    <section id="mostrarTarefa">

        <div v-if="loading" class="container-tasks">
            <div class="card" style="border-left: 3px solid green;">
                <div class="card-header header-flex-card placeholder-glow">
                    <span class="placeholder col-1 paragrafo"></span>
                    <span class="placeholder col-1 paragrafo"></span>
                    <span class="placeholder col-1 paragrafo"></span>
                </div>
                <div class="card-body placeholder-glow" style="display: flex; flex-direction: column;">
                    <span class="card-title placeholder col-4"></span>
                    <span class="card-text placeholder col-8"></span>
                </div>
                <div class="card-footer placeholder-glow" style="display: flex; justify-content: center;">
                    <span class="placeholder col-2"></span>
                </div>
            </div>
        </div>

        <p v-else-if="tarefas.length == 0" class="no-tasks">
            Nenhuma tarefa encontrada
        </p>
        <div v-else class="container-tasks">
            <div v-for="tarefa in tarefasOrdenadas()" :key="tarefa.id" class="card" :style="{
                borderLeft: tarefa.status === 'pendente' ? '3px solid red' : tarefa.status === 'em_andamento' ? '3px solid orange' : '3px solid green'
            }">
                <div class="card-header header-flex-card">
                    <p :class="{
                        'alert-p-orange': tarefa.status === 'em_andamento',
                        'alert-p-red': tarefa.status === 'pendente',
                        'alert-p-green': tarefa.status === 'concluida'
                    }" class="paragrafo">{{ tarefa.status }}</p>
                    <p class="paragrafo">{{ tarefa.categoria_nome }}</p>
                    <p class="paragrafo">Prioridade: {{ tarefa.prioridade }}</p>
                </div>
                <div class="card-body" style="background-color: white;" :style="{color: tarefa.categoria_cor}">
                    <h4 class="card-title">{{ tarefa.titulo }}</h4>
                    <p class="card-text">{{ tarefa.descricao }}</p>
                </div>
                <div class="card-footer text-body-secondary" style="text-align: center;">
                    {{ calcularData(tarefa.data_atualizacao) }} dias atrás
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CompMostrarTarefas',
    data() {
        return {
            tarefas: [],
            loading: true,
            intervalId: null,
            ordenar: 'prioridade',
            filtroTitulo: ''
        }
    },
    async created() {
        await this.buscarTarefas()
        this.intervalId = setInterval(async () => {
            await this.buscarTarefas()
        }, 300000) //5 minutos
    },
    beforeUnmount() {
        if (this.intervalId) {
            clearInterval(this.intervalId)
        }
    },
    methods: {
        async buscarTarefas() {
            try {
                this.loading = true
                const response = await axios('http://127.0.0.1:8000/api/tarefa/all')
                this.tarefas = response.data
            } catch (error) {
                console.log('erro ao encontrar tarefas: ', error)
            } finally {
                this.loading = false
            }
        },
        async atualizarTarefas() {
            await this.buscarTarefas()
        },
        calcularData(data) {
            const agora = new Date()
            const dataAlteracao = new Date(data)
            const diferenca = agora - dataAlteracao
            return Math.floor(diferenca / (1000 * 60 * 60 * 24))
        },
        tarefasOrdenadas() {
            let tarefasFiltradas = this.tarefas
            if (this.filtroTitulo) {
                tarefasFiltradas = this.tarefas.filter(tarefa =>
                    tarefa.titulo.toLowerCase().includes(this.filtroTitulo.toLowerCase())
                )
            }

            if (this.ordenar === 'prioridade') {
                const ordemPrioridade = {'alta': 1, 'media': 2, 'baixa': 3}
                return [...tarefasFiltradas].sort((a,b) => {
                    return ordemPrioridade[a.prioridade] - ordemPrioridade[b.prioridade]
                })
            } else if (this.ordenar === 'status'){
                const ordemStatus = {'pendente': 1, 'em_andamento': 2, 'concluida': 3}
                return [...tarefasFiltradas].sort((a,b) => {
                    return ordemStatus[a.status] - ordemStatus[b.status]
                })
            } else if (this.ordenar === 'data') {
                return [...tarefasFiltradas].sort((a,b) => {
                    return new Date(b.data_atualizacao) - new Date(a.data_atualizacao)
                })
            }
            return tarefasFiltradas
        }
    }
}
</script>

<style src="../assets/static.css"></style>
<style>
.container-tasks {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.header-flex-card {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    justify-content: center;
    align-items: center;

    .paragrafo {
        justify-self: center;
    }

    .paragrafo:first-child{
        grid-column: 1/2;
    }
    .paragrafo:last-child{
        grid-column: 3/4;
    }
}

.alert-p-orange {color: rgb(255, 170, 0);}
.alert-p-red {color: rgb(255, 144, 144);}
.alert-p-green {color: #00ba6d;}
</style>