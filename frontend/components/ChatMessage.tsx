'use client'

import type { Message } from '@/types/chat'
import SourcesList from './SourcesList'

interface ChatMessageProps {
  message: Message
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === 'user'

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-[80%] rounded-lg p-4 ${
          isUser
            ? 'bg-primary-600 text-white'
            : 'bg-gray-100 text-gray-900'
        }`}
      >
        <div className="whitespace-pre-wrap">{message.content}</div>
        
        {message.sources && message.sources.length > 0 && (
          <div className="mt-4 pt-4 border-t border-gray-300">
            <SourcesList sources={message.sources} />
          </div>
        )}
        
        <div
          className={`text-xs mt-2 ${
            isUser ? 'text-primary-100' : 'text-gray-500'
          }`}
        >
          {message.timestamp.toLocaleTimeString('pt-BR', {
            hour: '2-digit',
            minute: '2-digit',
          })}
        </div>
      </div>
    </div>
  )
}

