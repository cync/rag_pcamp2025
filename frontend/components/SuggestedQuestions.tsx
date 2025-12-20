'use client'

interface SuggestedQuestionsProps {
  onSelect: (question: string) => void
}

const suggestedQuestions = [
  'Quais são os principais temas abordados nas palestras?',
  'Quais palestras falam sobre Product Management?',
  'Resuma as principais ideias do evento',
  'Quais frameworks foram apresentados?',
]

export default function SuggestedQuestions({
  onSelect,
}: SuggestedQuestionsProps) {
  return (
    <div className="w-full max-w-2xl">
      <p className="text-sm text-gray-500 mb-4">Perguntas sugeridas:</p>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {suggestedQuestions.map((question, index) => (
          <button
            key={index}
            onClick={() => onSelect(question)}
            className="text-left px-4 py-3 bg-white border border-gray-200 rounded-lg hover:border-blue-300 hover:bg-blue-50 transition-all duration-200 text-sm text-gray-700 hover:text-gray-900 shadow-sm hover:shadow"
          >
            {question}
          </button>
        ))}
      </div>
    </div>
  )
}
