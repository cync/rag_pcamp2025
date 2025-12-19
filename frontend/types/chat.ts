export interface Source {
  titulo_palestra: string
  palestrante: string
  tipo: string
  tema?: string | null
  pagina_ou_slide?: string | null
  score: number
}

export interface ChatResponse {
  answer: string
  sources: Source[]
  query: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  sources?: Source[]
  timestamp: Date
}

