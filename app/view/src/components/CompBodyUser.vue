<template>
    <div class="card">
        <div class="card-header">
            Perfil
        </div>
        <div class="card-body">
            <CompPerfilUser />
        </div>
    </div>
</template>

<script>
import CompPerfilUser from './CompPerfilUser.vue';

export default {
    name: 'CompBodyUser',
    components: {
        CompPerfilUser
    }
}
</script>

<style src="../assets/static.css"></style>
<style></style>