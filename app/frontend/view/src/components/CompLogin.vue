<template>
    <main id="login-main">
        <section id="login">
            <div id="grid-login">
                <div id="logo">
                   <span class="material-symbols-outlined">
                        lock
                    </span> 
                </div>
                <div id="inputs">
                    <input type="text" class="input" placeholder="Nickname"/>
                    <input type="password" class="input" placeholder="Senha"/>
                    <input type="button" value="Submit" class="input" id="submit"/>
                </div>
                <div id="cadastrar">
                    <a href="#" class="link">Não tem conta? Cadastre-se</a>
                </div>
            </div>
        </section>
    </main>
</template>

<script>
    export default {
        name: 'CompLogin'
    }
</script>

<style src="../style/CompLogin.css"></style>
