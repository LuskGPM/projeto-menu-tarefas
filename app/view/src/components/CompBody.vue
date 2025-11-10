<template>
  <main class="main-body">
    <button :class="{ 'focus': btn_insert_active }" @click="btn_insert_active = !btn_insert_active" class="button-body"
      type="button" data-bs-toggle="collapse" data-bs-target="#formInsertTarefa" aria-expanded="false"
      aria-controls="formInsertTarefa">Inserir tarefa</button>
    <div class="collapse multi-collapse" id="formInsertTarefa">
      <CompInserirTarefa @tarefa-inserida="atualizarTarefas" />
    </div>
    <div class="card">
      <div class="card-header header-principal">
        <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" id="buttonOrdenar">
          Ordenar por
        </button>
        <ul class="dropdown-menu">
          <li><button class="dropdown-item" :class="{ 'active': ordenarBody === 'prioridade' }"
              @click="ordenarPor('prioridade')">Prioridade</button></li>
          <li><button class="dropdown-item" :class="{ 'active': ordenarBody === 'status' }"
              @click="ordenarPor('status')">Status</button></li>
          <li><button class="dropdown-item" :class="{ 'active': ordenarBody === 'data' }"
              @click="ordenarPor('data')">Data</button></li>
        </ul>
        <div class="input-group" id="inputSearch"  role="search">
          <span class="input-group-text">
            <i class="bi bi-search"></i>
          </span>
          <input class="form-control me-2" type="search" placeholder="Buscar Titulo" aria-label="Search"
            @input="buscarTitulo"/>
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
    ordenarPor(valor) {
      this.ordenarBody = valor
      this.$refs.mostrarTarefasRef.ordenar = this.ordenarBody
    },
    buscarTitulo(event) {
      const termo = event.target.value
      this.$refs.mostrarTarefasRef.filtroTitulo = termo
    },
    atualizarTarefas() {
      this.$refs.mostrarTarefasRef.atualizarTarefas()
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

.button-body {
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

  #inputSearch {
    max-width: 250px;
  }
}

@media screen and (min-width: 600px) {
  .header-principal {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;

    #inputSearch {
      grid-column: 2/-1;
      justify-self: flex-end;
    }
    #buttonOrdenar {
      grid-column: 1/2;
      justify-self: flex-start;
    }
  }
}
</style>