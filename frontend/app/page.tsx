'use client'

import { useState } from 'react'
import ChatInterface from '@/components/ChatInterface'
import Header from '@/components/Header'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <Header />
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <ChatInterface />
      </div>
    </main>
  )
}

