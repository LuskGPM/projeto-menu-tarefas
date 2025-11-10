<template>
  <main class="main-body">
    <button class="button-body-geral" :class="{ 'focus': btn_insert_active }" type="button" data-bs-toggle="collapse"
      data-bs-target="#formInsertTarefa" aria-expanded="false" aria-controls="formInsertTarefa"
      @click="toggleBTN(true)">Inserir tarefa</button>
    <div class="collapse multi-collapse" id="formInsertTarefa">
      <CompInserirTarefa />
    </div>
    <div class="card">
      <div class="card-header header-principal">
        <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          Ordenar por
        </button>
        <ul class="dropdown-menu">
          <li><button class="dropdown-item" :class="{'active': ordenarBody === 'prioridade'}" @click="ordenarPor('prioridade')">Prioridade</button></li>
          <li><button class="dropdown-item" :class="{'active': ordenarBody === 'status'}" @click="ordenarPor('status')">Status</button></li>
          <li><button class="dropdown-item" :class="{'active': ordenarBody === 'data'}" @click="ordenarPor('data')">Data</button></li>
        </ul>
        <div class="input-group" role="search">
          <span class="input-group-text">
            <i class="bi bi-search"></i>
          </span>
          <input class="form-control me-2" type="search" placeholder="Buscar Titulo" aria-label="Search"
            @input="buscarTitulo" style="max-width: 250px;"/>
        </div>
      </div>
      <div id="formMostrarTarefas" class="card-body">
        <CompMostrarTarefas ref="mostrarTarefasRef" />
      </div>
    </div>
  </main>
</template>

<script>
import CompInserirTarefa from './CompInserirTarefa.vue';
import CompMostrarTarefas from './CompMostrarTarefas.vue';

export default {
  name: 'CompBody',
  components: {
    CompInserirTarefa,
    CompMostrarTarefas
  },
  data() {
    return {
      btn_insert_active: false,
      btn_show_active: false,
      ordenarBody: 'prioridade'
    }
  },
  methods: {
    toggleBTN(is_insert_btn) {
      if (is_insert_btn) {
        this.btn_insert_active = !this.btn_insert_active
      } else { this.btn_show_active = !this.btn_show_active }
    },
    ordenarPor(valor) {
      this.ordenarBody = valor
      this.$refs.mostrarTarefasRef.ordenar = this.ordenarBody
    },
    buscarTitulo(event) {
      const termo = event.target.value
      this.$refs.mostrarTarefasRef.filtroTitulo = termo
    }
  }
}

</script>

<style src="../assets/static.css"></style>
<style>
.main-body {
  display: flex;
  flex-direction: column;
}

.button-body-geral {
  padding: 20px;
  width: 100%;
  border: 2px solid var(--azul-claro);
  border-radius: 10px;
  background-color: var(--azul-claro);
  box-shadow: 5px 5px 7px rgba(0, 0, 0, 0.279);
  transition: all .3s ease-out;
  font-size: 1.3em;
  margin-top: 20px;

  &:first-child {
    margin-top: 0;
  }
}

.focus {
  color: var(--branco-painel-texto);
  background-color: var(--azul-escuro);
}

.card-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.header-principal {
  display: flex;
  flex-direction: column-reverse;
  align-items: flex-start;
  gap: 10px;
}
</style>