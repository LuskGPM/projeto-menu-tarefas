<template>
    <header>
        <nav>
            <div id="header-sanduiche">
                <span class="material-symbols-outlined" @click="toggle_menu">
                    menu
                </span>
            <div class="sidebar" :class="{'sidebar-aberto': true}">
                </div>
                <div id="header-perfil">
                    <span class="material-symbols-outlined">
                        logout
                    </span>
                </div>
                <div id="header-logout">
                    <span class="material-symbols-outlined">
                        account_circle
                    </span>
                </div>
            </div>
        </nav>
    </header>
</template>

<script>
export default {
    name: 'CompHeader',
    methods: {
        toggle_menu() {

        }
    }
}
</script>

<style>
@import url('../assets/static.css');


</style>