<template>
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2024 Menu de Tarefas. Desenvolvido por LuskGPM. Todos os direitos reservados</p>
                </div>
                <div class="col-md-6 text-end">
                    <p>Vue.js + FastAPI + Redis + MySQL</p>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'CompFooter'
}
</script>

<style>
.footer {
    background-color: var(--azul-escuro);
    color: var(--branco-painel-texto);
    padding: 30px 0;
    margin-top: auto;
    text-align: center;
}

.footer p {
    margin: 0;
    font-size: 0.9em;
}

@media (max-width: 768px) {
    .footer .text-end {
        text-align: center !important;
    }
}
</style>