import { createRouter, createWebHistory } from 'vue-router'
import CompLogin from '../components/CompLogin.vue'
import CompTelaPrincipal from '../components/CompTelaPrincipal.vue'
import CompCadastro from '../components/CompCadastro.vue'
import CompTelaUsuario from '../components/CompTelaUsuario.vue'

const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: CompLogin
    },
    {
        path: '/tela-principal',
        name: 'tela-principal',
        component: CompTelaPrincipal
    },
    {
        path: '/cadastro',
        name: 'cadastro',
        component: CompCadastro
    },
    {
        path: '/tela-user',
        name: 'tela-user',
        component: CompTelaUsuario
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
