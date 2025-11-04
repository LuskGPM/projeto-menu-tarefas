<template>
    <main id="cad-main">
        <section id="cad-section">
            <div id="cad-grid">
                <div id="logo">
                    <span class="material-symbols-outlined">
                        app_registration
                    </span> 
                </div>
                <div id="inputs">

                </div>
                <div id="cad-login">
                    <router-link to="/login" class="link">
                        Possuí uma conta? 
                    </router-link>
                </div>
            </div>
        </section>
        <CompDireitosAutorais/>
    </main>
</template>

<script>
    import CompDireitosAutorais from './CompDireitosAutorais.vue';

    export default {
        name: 'CompCadastro',
        components: {
            CompDireitosAutorais
        }
    }
</script>

<style src="../style/CompCadastro.css"></style>
<style src="../assets/static.css"></style>