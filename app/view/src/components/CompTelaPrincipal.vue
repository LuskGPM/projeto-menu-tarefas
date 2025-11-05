<template>
    <CompHeader />
</template>

<script>
import CompHeader from './CompHeader.vue';
import { useSessionMonitor } from '../composables/useSessionMonitor'

export default {
    name: 'CompTelaPrincipal',
    components: {
        CompHeader
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

<style></style>