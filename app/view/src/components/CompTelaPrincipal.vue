<template>
    <CompHeader/>
</template>

<script>
    import CompHeader from './CompHeader.vue';
    //import axios from 'axios';
    import { useAuth } from '../composables/useAuth';

    export default {
        name: 'CompTelaPrincipal',
        components: {
            CompHeader
        },
        async created() {
            const { verificarSessao } = useAuth()
            if (!await verificarSessao()) {
                this.$router.push('/login')
            }
        },
        methods: {
        }
    }
</script>

<style>

</style>