<template>
  <main class="main-body">
    <button class="button-insert" type="button" data-bs-toggle="collapse" data-bs-target="#formInsertTarefa"
      aria-expanded="false" aria-controls="formInsertTarefa">Inserir tarefa</button>
    <div class="collapse multi-collapse" id="formInsertTarefa">
      <CompInserirTarefa />
    </div>
  </main>
</template>

<script>
import CompInserirTarefa from './CompInserirTarefa.vue';

export default {
  name: 'CompBody',
  components: {
    CompInserirTarefa
  }
}
</script>

<style src="../assets/static.css"></style>
<style>
.main-body {
  display: flex;
  flex-direction: column;
}

.button-insert {
  padding: 20px;
  width: 100%;
  border: 1px solid black;
  border-radius: 10px;
  background-color: var(--b);
}
</style>