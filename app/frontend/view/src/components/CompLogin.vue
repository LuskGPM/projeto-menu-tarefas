<template>
    <main id="login-main">
        <section id="login-section">
            <div id="login-grid">
                <div id="logo">
                   <span class="material-symbols-outlined">
                        login
                    </span> 
                </div>
                <div id="login-inputs">
                    <label for="loginNickname" class="label">Nickname</label>
                    <input type="text" class="input" id="loginNickname"/>
                    
                    <label for="loginSenha" class="label">Senha</label>
                    <input type="password" class="input" id="loginSenha"/>
                    
                    <input type="button" value="Login" class="input" id="submit"/>
                </div>
                <div id="login-cadastrar">
                    <router-link to="/cadastro" class="link">
                        Não tem conta? Cadastre-se
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
        name: 'CompLogin',
        components: {
            CompDireitosAutorais
        }
    }
</script>

<style src="../style/CompLogin.css"></style>
