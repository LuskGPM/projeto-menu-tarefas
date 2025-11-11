<template>
    <div class="tela-usuario">
        <CompHeader class="header-pu" />
        <CompBodyUser class="body-pu"/>
        <CompFooter class="footer-pu"/>
    </div>
</template>

<script>
import CompHeader from './CompHeader.vue';
import { useSessionMonitor } from '../composables/useSessionMonitor'
import CompBodyUser from './CompBodyUser.vue';
import CompFooter from './CompFooter.vue';

export default {
    name: 'CompTelaUsuario',
    components: {
        CompHeader,
        CompBodyUser,
        CompFooter
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
.tela-usuario {
    width: 100vw;
    height: auto;
    min-height: 100vh;
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: 150px 1fr 150px;
    background-color: var(--cinza-claro);

    .header-pu {
        grid-column: 1/-1;
        grid-row: 1/2;
    }

    .body-pu {
        grid-column: 2/-2;
        grid-row: 2/-2;
        box-shadow: 5px 5px 7px rgba(0, 0, 0, 0.178);
    }

    .footer-pu {
        grid-column: 1/-1;
        grid-row: -2/-1;
    }
}
</style>