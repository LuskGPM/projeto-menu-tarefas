<template>
    <CompDadosUser />
    <CompAlterarSenha />
    <CompDeletarUser />
</template>

<script>
import CompAlterarSenha from './CompAlterarSenha.vue';
import CompDadosUser from './CompDadosUser.vue';
import CompDeletarUser from './CompDeletarUser.vue';

export default {
    name: 'CompPerfilUser',
    components: {
        CompAlterarSenha,
        CompDadosUser,
        CompDeletarUser
    }
}
</script>

<style src="../assets/static.css"></style>