import { createRouter, createWebHistory } from 'vue-router'
import CompLogin from '../components/CompLogin.vue'
import CompTelaPrincipal from '../components/CompTelaPrincipal.vue'
import CompCadastro from '../components/CompCadastro.vue'

console.log('CompLogin importado:', CompLogin)

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

console.log('Router criado:', router)
console.log('Rotas:', routes)

export default router
