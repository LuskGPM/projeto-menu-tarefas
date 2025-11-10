import { createRouter, createWebHistory } from 'vue-router'
import CompLogin from '../components/CompLogin.vue'
import CompTelaPrincipal from '../components/CompTelaPrincipal.vue'
import CompCadastro from '../components/CompCadastro.vue'

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
        name: 'tela',
        component: CompTelaPrincipal
    },
    {
        path: '/cadastro',
        name: 'cadastro',
        component: CompCadastro
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
