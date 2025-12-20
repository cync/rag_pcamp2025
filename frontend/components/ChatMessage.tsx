'use client'

import { useState } from 'react'
import SourcesList from './SourcesList'
import type { Message } from '@/types/chat'

interface ChatMessageProps {
  message: Message
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const [showSources, setShowSources] = useState(false)

  const isUser = message.role === 'user'

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[85%] sm:max-w-[75%] ${
          isUser
            ? 'bg-gradient-to-br from-blue-600 to-blue-700 text-white rounded-2xl rounded-tr-sm px-5 py-3.5 shadow-md'
            : 'bg-white border border-gray-200 rounded-2xl rounded-tl-sm px-5 py-4 shadow-sm'
        }`}
      >
        <div className="prose prose-sm max-w-none">
          <p className={`whitespace-pre-wrap ${isUser ? 'text-white' : 'text-gray-900'}`}>
            {message.content}
          </p>
        </div>

        {!isUser && message.sources && message.sources.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-200">
            <button
              onClick={() => setShowSources(!showSources)}
              className="flex items-center space-x-2 text-xs text-gray-600 hover:text-gray-900 transition-colors"
            >
              <svg
                className={`w-4 h-4 transition-transform ${showSources ? 'rotate-180' : ''}`}
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
              <span className="font-medium">
                {message.sources.length} fonte{message.sources.length > 1 ? 's' : ''}
              </span>
            </button>
            {showSources && (
              <div className="mt-3">
                <SourcesList sources={message.sources} />
              </div>
            )}
          </div>
        )}

        <div className={`mt-2 text-xs ${isUser ? 'text-blue-100' : 'text-gray-400'}`}>
          {new Date(message.timestamp).toLocaleTimeString('pt-BR', {
            hour: '2-digit',
            minute: '2-digit',
          })}
        </div>
      </div>
    </div>
  )
}
