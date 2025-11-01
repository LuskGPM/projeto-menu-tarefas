import { createRouter, createWebHistory } from 'vue-router'
import CompLogin from '../components/CompLogin.vue'
import CompHeader from '../components/CompHeader.vue'
import CompLerJson from '../components/CompLerJson.vue'

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
        path: '/header',
        name: 'header',
        component: CompHeader
    },
    {
        path: '/tarefa',
        name: 'tarefa',
        component: CompLerJson
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

console.log('Router criado:', router)
console.log('Rotas:', routes)

export default router
