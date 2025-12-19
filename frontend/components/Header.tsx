'use client'

export default function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">
              Product Camp 2025
            </h1>
            <p className="text-gray-600 mt-1">
              Assistente RAG - Consulte todas as palestras do evento
            </p>
          </div>
          <div className="hidden md:block">
            <div className="bg-primary-100 text-primary-800 px-4 py-2 rounded-lg">
              <span className="text-sm font-semibold">RAG System</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}

