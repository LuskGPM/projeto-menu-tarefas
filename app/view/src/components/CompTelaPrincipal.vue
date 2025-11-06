<template>
    <CompHeader/>
    <CompBody/>
</template>

<script>
import CompHeader from './CompHeader.vue';
import CompBody from './CompBody.vue';
import { useSessionMonitor } from '../composables/useSessionMonitor'

export default {
    name: 'CompTelaPrincipal',
    components: {
        CompHeader,
        CompBody
    },
    data() {
        return {
            intervalId: null
        }
    },
    async created() {
        const { iniciarMonitoramento } = useSessionMonitor()
        iniciarMonitoramento()
    },
    methods: {
    }
}
</script>

<style>
</style>