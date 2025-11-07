// useSessionMonitor.js
import axios from 'axios'
import { ref, onUnmounted } from 'vue'
import router from '../router'

export function useSessionMonitor() {
    const intervalId = ref(null)
    const iniciarMonitoramento = () => {
    intervalId.value = setInterval(async () => {
        try {
            await axios('http://127.0.0.1:8000/api/user/verificar-sessao')
        } catch (error) {
            router.push('/login')
        }
    }, 300000)
}
    const pararMonitoramento = () => {
        if (intervalId.value) {
            clearInterval(intervalId.value)
        }
    }
    onUnmounted(pararMonitoramento)
    return { iniciarMonitoramento, pararMonitoramento }
}
