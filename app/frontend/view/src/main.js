import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

console.log('Router no main.js:', router)

const app = createApp(App)
console.log('App criado:', app)

app.use(router)
console.log('Router adicionado ao app')

router.isReady().then(() => {
    app.mount('#app')
    console.log('App montado após router ready')
})
