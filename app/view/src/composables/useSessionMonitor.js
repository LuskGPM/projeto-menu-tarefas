// useSessionMonitor.js
import axios from 'axios'
import { ref, onUnmounted } from 'vue'
import router from '../router'

export function useSessionMonitor() {
    const intervalId = ref(null)
    
    const iniciarMonitoramento = () => {
        intervalId.value = setInterval(async () => {
            try {
                await axios.get('http://127.0.0.1:8000/api/user/verificar-sessao')
                // Status 200 = sessão ativa, não faz nada
            } catch (error) {
                // Qualquer erro (401, 403, etc.) = redireciona
                router.push('/login')
            }
        }, 300000) // 5 minutos
    }
    
    const pararMonitoramento = () => {
        if (intervalId.value) {
            clearInterval(intervalId.value)
        }
    }
    
    onUnmounted(pararMonitoramento)
    
    return { iniciarMonitoramento, pararMonitoramento }
}
