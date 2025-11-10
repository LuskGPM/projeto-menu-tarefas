import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as bootstrap from 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

// Disponibiliza Bootstrap globalmente
window.bootstrap = bootstrap

const app = createApp(App)
app.use(router)

router.isReady().then(() => {
    app.mount('#app')
})
