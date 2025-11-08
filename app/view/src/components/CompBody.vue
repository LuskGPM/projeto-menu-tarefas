<template>
  <main class="main-body">
    <button class="button-body-geral" :class="{ 'color-white': btn_insert_active }" type="button"
      data-bs-toggle="collapse" data-bs-target="#formInsertTarefa" aria-expanded="false"
      aria-controls="formInsertTarefa" @click="toggleBTN">Inserir tarefa</button>
    <div class="collapse multi-collapse" id="formInsertTarefa">
      <CompInserirTarefa class="comp-inserir" />
    </div>
  </main>
</template>

<script>
import CompInserirTarefa from './CompInserirTarefa.vue';

export default {
  name: 'CompBody',
  components: {
    CompInserirTarefa
  },
  data() {
    return {
      btn_insert_active: false
    }
  },
  methods: {
    toggleBTN() {
      this.btn_insert_active = !this.btn_insert_active
      this.animateGradient()
    },
    animateGradient() {
      const button = this.$el.querySelector('.button-body-geral')
      let progress = 0
      const duration = 300 // ms
      const startTime = performance.now()

      const animate = (currentTime) => {
        progress = Math.min((currentTime - startTime) / duration, 1)

        // Interpola entre as cores
        const r1 = this.btn_insert_active ? 255 + (84 - 255) * progress : 84 + (255 - 84) * progress
        const g1 = this.btn_insert_active ? 255 + (224 - 255) * progress : 224 + (255 - 224) * progress
        const b1 = this.btn_insert_active ? 255 + (182 - 255) * progress : 182 + (255 - 182) * progress

        button.style.background = `linear-gradient(49deg, rgba(${r1}, ${g1}, ${b1}, 1) 1%, rgba(165, 215, 238, 1) 100%)`

        if (progress < 1) {
          requestAnimationFrame(animate)
        }
      }

      requestAnimationFrame(animate)
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
  background: #FFF;
  background: linear-gradient(107deg, rgba(255, 255, 255, 1) 0%, rgba(165, 215, 238, 1) 100%);
  box-shadow: 5px 5px 7px rgba(0, 0, 0, 0.279);
  transition: all .3s ease-out;
  font-size: 1.3em;
}

.color-white {
  color: var(--branco-painel-texto);
}

.comp-inserir {
  margin-top: 15px;
}
</style>