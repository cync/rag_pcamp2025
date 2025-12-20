import axios from 'axios'
import type { ChatResponse } from '@/types/chat'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface ChatFilters {
  titulo_palestra?: string
  palestrante?: string
  tema?: string
  tipo?: string
  dia?: string
}

export const chatService = {
  async sendMessage(
    question: string,
    filters?: ChatFilters | null
  ): Promise<ChatResponse> {
    try {
      const response = await apiClient.post<ChatResponse>('/api/chat', {
        question,
        filters: filters || null,
      })
      return response.data
    } catch (error: any) {
      console.error('Erro ao enviar mensagem:', error)
      throw error
    }
  },

  async getPalestras(): Promise<Array<{
    titulo_palestra: string
    palestrante: string
    tipo: string
    tema?: string | null
    dia?: string | null
  }>> {
    try {
      const response = await apiClient.get('/api/palestras')
      return response.data
    } catch (error: any) {
      console.error('Erro ao buscar palestras:', error)
      return []
    }
  },
}

