import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/js/bootstrap.bundle'
import 'bootstrap-icons/font/bootstrap-icons.css'


const app = createApp(App)

app.use(router)

router.isReady().then(() => {
    app.mount('#app')
})
