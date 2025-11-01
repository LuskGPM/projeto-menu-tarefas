<template>

<main>
    <p :style="{color: cor}">Tarefas</p>
    <div v-for="(tarefa, index) in arrayTarefas" :key="index">
        <input type="text" :value="tarefa">
    </div>
</main>

</template>

<script>
    export default {
        name: 'lerJson',
        data() {
            return {
                arrayTarefas: {
                'titulo': 'primeira tarefa',
                'descricao': 'minha primeira tarefa',
                'status': 'em_andamento'
                },
                cor: '#84ffb5'
            }
        }
    }
</script>

<style>
</style>