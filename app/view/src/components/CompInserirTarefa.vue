<template>
    <main>
        <section id="inserirTarefa">
            <form>
                <label for="tarefaTitulo">Titulo</label>
                <input type="text" id="tarefaTitulo" v-model="t_titulo">

                <label for="tarefaDesc">Descrição</label>
                <textarea type="text" id="tarefaDesc" v-model="t_desc"></textarea>

                <label for="tarefaStatus">Status</label>
                <select aria-label="Selecione o status" id="tarefaStatus" class="form-select" v-model="t_status">
                    <option value="pendente">Pendente</option>
                    <option value="em_andamento">Em andamento</option>
                    <option value="concluida">Concluído</option>
                </select>

                <label for="tarefaPrioridade">Prioridade</label>
                <select aria-label="Selecione a prioridade" id="tarefaPrioriodade" class="form-select" v-model="t_prioridade">
                    <option value="alta">Alta</option>
                    <option value="media">Media</option>
                    <option value="baixa">Baixa</option>
                </select>

                <label for="tarefaCategoria">Categoria</label>
                <select aria-label="Selecione a prioridade" id="tarefaCategoria" class="form-select" v-model.number="t_categoria">
                    <option value="1">Trabalho</option>
                    <option value="2">Pessoal</option>
                    <option value="3">Estudos</option>
                    <option value="4">Urgente</option>
                    <option value="5">Casa</option>
                    <option value="6">Saúde</option>
                </select>

                <p ref="inserirTarefaAlert"></p>

                <input type="submit" value="Inserir" @click.prevent="inserir_tarefa">
            </form>
        </section>
        <section id="tarefas"> </section>
    </main>
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
            t_categoria: 2
        }
    },
    methods: {
        async inserir_tarefa() {
            const dados = {
                titulo: this.t_titulo,
                descricao: this.t_desc,
                status: this.t_status,
                prioridade: this.t_prioridade,
                categoria_id: this.t_categoria
            }

            try {
                console.log('dados enviados: ', dados)
                const response = await axios.post('http://127.0.0.1:8000/api/tarefa/register', dados)
                this.$refs.inserirTarefaAlert.style.color = 'green'
                this.$refs.inserirTarefaAlert.innerText = response.data.message
            } catch (error){
                console.log(error)
                this.$refs.inserirTarefaAlert.style.color = 'red'
                this.$refs.inserirTarefaAlert.innerText = 'Preencha todos os campos corretamente'
            } finally {
                setTimeout(() => {
                if (this.$refs.inserirTarefaAlert) {
                    this.$refs.inserirTarefaAlert.innerText = ''
                }
            }, 5000)
            }
        }
    }
}
</script>

<style src="../assets/static.css"></style>
<style>

</style>