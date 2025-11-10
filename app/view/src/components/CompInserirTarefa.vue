<template>
    <section id="inserirTarefa">
        <form class="formulario-insert">
            <div class="form-floating">
                <input type="text" id="tarefaTitulo" v-model="t_titulo" class="form-control" placeholder="Titulo">
                <label for="tarefaTitulo">Titulo</label>
            </div>

            <div class="form-floating">
                <textarea type="text" id="tarefaDesc" v-model="t_desc" class="form-control" placeholder="descricao"></textarea>
                <label for="tarefaDesc">Descrição</label>
            </div>

            <div class="form-floating">
                <select aria-label="Selecione o status" id="tarefaStatus" class="form-select" v-model="t_status">
                    <option value="pendente">Pendente</option>
                    <option value="em_andamento">Em andamento</option>
                    <option value="concluida">Concluído</option>
                </select>
                <label for="tarefaStatus">Status</label>
            </div>

            <div class="form-floating">
                <select aria-label="Selecione a prioridade" id="tarefaPrioriodade" class="form-select"
                    v-model="t_prioridade">
                    <option value="alta">Alta</option>
                    <option value="media">Media</option>
                    <option value="baixa">Baixa</option>
                </select>
                <label for="tarefaPrioridade">Prioridade</label>
            </div>

            <div class="form-floating">
                <select aria-label="Selecione a prioridade" id="tarefaCategoria" class="form-select"
                    v-model.number="t_categoria">
                    <option value="1">Trabalho</option>
                    <option value="2">Pessoal</option>
                    <option value="3">Estudos</option>
                    <option value="4">Urgente</option>
                    <option value="5">Casa</option>
                    <option value="6">Saúde</option>
                </select>
                <label for="tarefaCategoria">Categoria</label>
            </div>

            <p ref="inserirTarefaAlert" v-show="inserirAlert">{{ inserirAlert }}</p>

            <input type="submit" value="Inserir" class="btn btn-success" @click.prevent="inserir_tarefa"
                :disabled="processandoInsert">
        </form>
    </section>
    <section id="tarefas"> </section>
</template>

<script>
import axios from 'axios';

//import axios from 'axios';

export default {
    name: 'CompInserirTarefa',
    data() {
        return {
            t_titulo: '',
            t_desc: '',
            t_status: 'pendente',
            t_prioridade: 'media',
            t_categoria: 2,
            processandoInsert: false,
            inserirAlert: ''
        }
    },
    methods: {
        async inserir_tarefa() {
            this.processandoInsert = true
            const dados = {
                titulo: this.t_titulo,
                descricao: this.t_desc,
                status: this.t_status,
                prioridade: this.t_prioridade,
                categoria_id: this.t_categoria
            }

            try {
                const response = await axios.post('http://127.0.0.1:8000/api/tarefa/register', dados)
                this.$refs.inserirTarefaAlert.style.color = 'green'
                this.inserirAlert = response.data.message
                this.t_titulo = ''
                this.t_desc = ''
            } catch (error) {
                console.log(error)
                this.$refs.inserirTarefaAlert.style.color = 'red'
                this.inserirAlert = 'Preencha todos os campos corretamente'
            } finally {
                this.processandoInsert = false
                setTimeout(() => {
                    if (this.$refs.inserirTarefaAlert) {
                        this.inserirAlert = ''
                    }
                }, 5000)
            }
        }
    }
}
</script>

<style src="../assets/static.css"></style>
<style>
.formulario-insert {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    gap: 10px;

    input,
    textarea,
    select {
        border: 1px solid var(--verde-ciano);
    }
}
</style>