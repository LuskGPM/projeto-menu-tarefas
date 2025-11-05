import axios from 'axios'

export function useAuth() {
    const verificarSessao = async () => {
        try {
            await axios('http://127.0.0.1:8000/api/user/verificar-sessao')
            return true
        } catch (error) {
            console.log('Erro: ', error)
            return false
        }
    }
    return {verificarSessao}
}