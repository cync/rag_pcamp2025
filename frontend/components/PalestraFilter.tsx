'use client'

import { useState, useEffect } from 'react'
import { chatService } from '@/services/chatService'

export interface Palestra {
  titulo_palestra: string
  palestrante: string
  tipo: string
  tema?: string | null
  dia?: string | null
}

interface PalestraFilterProps {
  selectedPalestra: string | null
  onSelectPalestra: (titulo: string | null) => void
}

export default function PalestraFilter({
  selectedPalestra,
  onSelectPalestra,
}: PalestraFilterProps) {
  const [palestras, setPalestras] = useState<Palestra[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    const loadPalestras = async () => {
      try {
        const data = await chatService.getPalestras()
        setPalestras(data)
      } catch (error) {
        console.error('Erro ao carregar palestras:', error)
      } finally {
        setIsLoading(false)
      }
    }

    loadPalestras()
  }, [])

  const selectedPalestraData = palestras.find(
    (p) => p.titulo_palestra === selectedPalestra
  )

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between px-4 py-2.5 bg-white border border-gray-200 rounded-lg hover:border-gray-300 transition-colors text-left"
        aria-label="Filtrar por palestra"
      >
        <div className="flex items-center space-x-2 min-w-0 flex-1">
          <svg
            className="w-5 h-5 text-gray-400 flex-shrink-0"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
            />
          </svg>
          <span className="text-sm text-gray-700 truncate">
            {selectedPalestra
              ? selectedPalestraData?.titulo_palestra || selectedPalestra
              : 'Todas as palestras'}
          </span>
        </div>
        <svg
          className={`w-4 h-4 text-gray-400 transition-transform flex-shrink-0 ${
            isOpen ? 'rotate-180' : ''
          }`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {isOpen && (
        <>
          <div
            className="fixed inset-0 z-10"
            onClick={() => setIsOpen(false)}
          />
          <div className="absolute z-20 w-full mt-2 bg-white border border-gray-200 rounded-lg shadow-lg max-h-96 overflow-y-auto">
            {isLoading ? (
              <div className="p-4 text-center text-gray-500 text-sm">
                Carregando palestras...
              </div>
            ) : palestras.length === 0 ? (
              <div className="p-4 text-center text-gray-500 text-sm">
                Nenhuma palestra encontrada
              </div>
            ) : (
              <>
                <button
                  onClick={() => {
                    onSelectPalestra(null)
                    setIsOpen(false)
                  }}
                  className={`w-full px-4 py-2.5 text-left text-sm hover:bg-gray-50 transition-colors ${
                    !selectedPalestra
                      ? 'bg-blue-50 text-blue-700 font-medium'
                      : 'text-gray-700'
                  }`}
                >
                  <div className="flex items-center space-x-2">
                    <span>Todas as palestras</span>
                  </div>
                </button>
                <div className="border-t border-gray-200" />
                {palestras.map((palestra) => (
                  <button
                    key={palestra.titulo_palestra}
                    onClick={() => {
                      onSelectPalestra(palestra.titulo_palestra)
                      setIsOpen(false)
                    }}
                    className={`w-full px-4 py-3 text-left hover:bg-gray-50 transition-colors ${
                      selectedPalestra === palestra.titulo_palestra
                        ? 'bg-blue-50 border-l-4 border-blue-600'
                        : ''
                    }`}
                  >
                    <div className="flex flex-col space-y-1">
                      <span
                        className={`text-sm ${
                          selectedPalestra === palestra.titulo_palestra
                            ? 'text-blue-900 font-medium'
                            : 'text-gray-900'
                        }`}
                      >
                        {palestra.titulo_palestra}
                      </span>
                      <div className="flex items-center space-x-3 text-xs text-gray-500">
                        <span>{palestra.palestrante}</span>
                        {palestra.dia && (
                          <>
                            <span>•</span>
                            <span>{palestra.dia}</span>
                          </>
                        )}
                      </div>
                    </div>
                  </button>
                ))}
              </>
            )}
          </div>
        </>
      )}
    </div>
  )
}

