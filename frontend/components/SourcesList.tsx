'use client'

import type { Source } from '@/types/chat'

interface SourcesListProps {
  sources: Source[]
}

export default function SourcesList({ sources }: SourcesListProps) {
  return (
    <div className="space-y-2">
      {sources.map((source, index) => (
        <div
          key={index}
          className="bg-gray-50 border border-gray-200 rounded-lg p-3 hover:bg-gray-100 transition-colors"
        >
          <div className="flex items-start justify-between">
            <div className="flex-1 min-w-0">
              <h4 className="text-sm font-semibold text-gray-900 truncate">
                {source.titulo_palestra}
              </h4>
              <div className="mt-1.5 flex flex-wrap items-center gap-2 text-xs text-gray-600">
                <span className="font-medium">{source.palestrante}</span>
                {source.tema && (
                  <>
                    <span>•</span>
                    <span>{source.tema}</span>
                  </>
                )}
                {source.pagina_ou_slide && (
                  <>
                    <span>•</span>
                    <span>Página/Slide: {source.pagina_ou_slide}</span>
                  </>
                )}
              </div>
            </div>
            {source.score && (
              <div className="ml-3 flex-shrink-0">
                <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800">
                  {Math.round(source.score * 100)}%
                </span>
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}
