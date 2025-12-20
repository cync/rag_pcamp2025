'use client'

import { useState, useRef, useEffect, useCallback } from 'react'
import ChatMessage from './ChatMessage'
import ChatInput from './ChatInput'
import SuggestedQuestions from './SuggestedQuestions'
import PalestraFilter from './PalestraFilter'
import { chatService, type ChatFilters } from '@/services/chatService'
import type { Message } from '@/types/chat'

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [selectedPalestra, setSelectedPalestra] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [])

  useEffect(() => {
    scrollToBottom()
  }, [messages, scrollToBottom])

  const handleSendMessage = useCallback(async (question: string) => {
    if (!question.trim() || isLoading) return

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: question,
      timestamp: new Date(),
    }
    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)
    setError(null)

    try {
      const filters: ChatFilters | null = selectedPalestra
        ? { titulo_palestra: selectedPalestra }
        : null

      const response = await chatService.sendMessage(question, filters)
      
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: response.answer,
        sources: response.sources,
        timestamp: new Date(),
      }
      
      setMessages((prev) => [...prev, assistantMessage])
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || err.message || 'Erro ao processar pergunta'
      setError(errorMessage)
      
      const errorMsg: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: `Desculpe, ocorreu um erro: ${errorMessage}`,
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMsg])
    } finally {
      setIsLoading(false)
    }
  }, [isLoading, selectedPalestra])

  const handleSuggestedQuestion = useCallback((question: string) => {
    handleSendMessage(question)
  }, [handleSendMessage])

  return (
    <div className="flex flex-col h-[calc(100vh-180px)] max-h-[900px] bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-100">
      {/* Header com filtro */}
      <div className="px-6 py-4 border-b border-gray-100 bg-gradient-to-r from-gray-50 to-white">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <h2 className="text-lg font-semibold text-gray-900">Consultas RAG</h2>
            <p className="text-sm text-gray-500 mt-0.5">
              {selectedPalestra ? 'Filtrado por palestra específica' : 'Todas as palestras'}
            </p>
          </div>
          <div className="w-full sm:w-80">
            <PalestraFilter
              selectedPalestra={selectedPalestra}
              onSelectPalestra={setSelectedPalestra}
            />
          </div>
        </div>
      </div>

      {/* Área de mensagens */}
      <div className="flex-1 overflow-y-auto px-6 py-6 space-y-6 bg-gray-50/50">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-center px-4">
            <div className="mb-8">
              <div className="w-20 h-20 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-lg">
                <svg
                  className="w-10 h-10 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                  />
                </svg>
              </div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">
                Bem-vindo ao Assistente RAG
              </h2>
              <p className="text-gray-600 max-w-md mx-auto">
                Faça perguntas sobre as palestras do Product Camp 2025
                {selectedPalestra && (
                  <span className="block mt-2 text-blue-600 font-medium">
                    Filtrando por: {selectedPalestra}
                  </span>
                )}
              </p>
            </div>
            <SuggestedQuestions onSelect={handleSuggestedQuestion} />
          </div>
        ) : (
          <>
            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
            ))}
            {isLoading && (
              <div className="flex items-center space-x-3 text-gray-500">
                <div className="animate-spin rounded-full h-5 w-5 border-2 border-gray-300 border-t-blue-600"></div>
                <span className="text-sm">Processando sua pergunta...</span>
              </div>
            )}
            <div ref={messagesEndRef} />
          </>
        )}
      </div>

      {/* Input */}
      <div className="border-t border-gray-200 p-4 bg-white">
        <ChatInput
          onSend={handleSendMessage}
          disabled={isLoading}
          placeholder={
            selectedPalestra
              ? `Pergunte sobre "${selectedPalestra}"...`
              : 'Digite sua pergunta sobre as palestras...'
          }
        />
        {error && (
          <div className="mt-3 text-sm text-red-600 bg-red-50 border border-red-200 px-4 py-2.5 rounded-lg">
            {error}
          </div>
        )}
      </div>
    </div>
  )
}
