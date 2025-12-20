'use client'

export default function Header() {
  return (
    <header className="bg-white/80 backdrop-blur-sm shadow-sm border-b border-gray-200 sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4 sm:py-5">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl sm:text-3xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Product Camp 2025
            </h1>
            <p className="text-sm sm:text-base text-gray-600 mt-1">
              Assistente RAG - Consulte todas as palestras
            </p>
          </div>
          <div className="hidden sm:flex items-center space-x-2 bg-gradient-to-r from-blue-50 to-indigo-50 px-4 py-2 rounded-lg border border-blue-100">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-sm font-medium text-blue-900">RAG System</span>
          </div>
        </div>
      </div>
    </header>
  )
}
