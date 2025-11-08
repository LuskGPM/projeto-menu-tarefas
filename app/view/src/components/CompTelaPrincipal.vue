<template>

    <body>
        <CompHeader class="header-pp" />
        <CompBody class="body-pp" />
    </body>
</template>

<script>
import CompHeader from './CompHeader.vue';
import { useSessionMonitor } from '../composables/useSessionMonitor'
import CompBody from './CompBody.vue';

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
    }
}
</script>

<style src="../assets/static.css"></style>

<style>
body {
    width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: 150px 1fr;

    .header-pp {
        grid-column: 1/-1;
        grid-row: 1/2;
    }

    .body-pp {
        grid-column: 2/-2;
        grid-row: 2/3;
        align-self: start;
    }
}
</style>