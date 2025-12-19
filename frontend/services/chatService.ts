import axios from 'axios'
import type { ChatResponse } from '@/types/chat'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const chatService = {
  async sendMessage(question: string): Promise<ChatResponse> {
    try {
      const response = await apiClient.post<ChatResponse>('/api/chat', {
        question,
        filters: null,
      })
      return response.data
    } catch (error: any) {
      console.error('Erro ao enviar mensagem:', error)
      throw error
    },
  },
}

