<template>
    <p id="direitos-autorais">
        Imagem de fundo: <a
            href="https://pt.vecteezy.com/?utm_source=vecteezy-download&utm_medium=license-info-pdf&utm_campaign=license-info-document">Vecteezy.com</a>
    </p>
</template>

<script>
export default {
    name: 'CompDireitosAutorais'
}
</script>

<style>
#direitos-autorais {
    position: absolute;
    bottom: 0;
    text-align: center;
    color: var(--azul-escuro);
    text-shadow: 1px 1px white;

    a {
        color: rgb(255, 149, 0);
    }
}
</style>