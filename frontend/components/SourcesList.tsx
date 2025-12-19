'use client'

import type { Source } from '@/types/chat'

interface SourcesListProps {
  sources: Source[]
}

export default function SourcesList({ sources }: SourcesListProps) {
  if (!sources || sources.length === 0) return null

  return (
    <div className="mt-3">
      <div className="text-xs font-semibold text-gray-700 mb-2">
        📚 Fontes citadas:
      </div>
      <div className="space-y-2">
        {sources.map((source, index) => (
          <div
            key={index}
            className="bg-white bg-opacity-50 rounded p-2 text-xs border border-gray-200"
          >
            <div className="font-semibold text-gray-900">
              {source.titulo_palestra}
            </div>
            <div className="text-gray-600 mt-1">
              <span className="font-medium">Palestrante:</span> {source.palestrante}
            </div>
            <div className="flex items-center space-x-3 mt-1 text-gray-500">
              <span>
                <span className="font-medium">Tipo:</span> {source.tipo}
              </span>
              {source.tema && (
                <span>
                  <span className="font-medium">Tema:</span> {source.tema}
                </span>
              )}
              {source.pagina_ou_slide && (
                <span>
                  <span className="font-medium">Slide:</span> {source.pagina_ou_slide}
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

