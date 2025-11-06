<template>
    <main>
        <section id="inserirTarefa">
            <form>
                <label for="tarefaTitulo">Titulo</label>
                <input type="text" id="tarefaTitulo" v-model="t_titulo">

                <label for="tarefaDesc">Descrição</label>
                <input type="text" id="tarefaDesc" v-model="t_desc">

                <label for="tarefaStatus">Status</label>
            </form>
        </section>
        <section id="tarefas"></section>
    </main>
</template>

<script>
export default {
    name: 'CompBody',
    data() {
        return {
            t_titulo: '',
            t_desc: ''
        }
    }
}
</script>

<style></style>