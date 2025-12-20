'use client'

import ChatInterface from '@/components/ChatInterface'
import Header from '@/components/Header'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-50">
      <Header />
      <div className="container mx-auto px-4 py-6 sm:py-8 max-w-6xl">
        <ChatInterface />
      </div>
    </main>
  )
}
