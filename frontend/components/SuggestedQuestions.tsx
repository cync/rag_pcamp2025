'use client'

interface SuggestedQuestionsProps {
  onSelect: (question: string) => void
}

const SUGGESTED_QUESTIONS = [
  'Quais são os principais temas abordados nas palestras?',
  'Quem são os palestrantes do evento?',
  'Quais frameworks de produto foram mencionados?',
  'Há alguma palestra sobre estratégia de produto?',
  'Quais são as principais tendências discutidas?',
]

export default function SuggestedQuestions({
  onSelect,
}: SuggestedQuestionsProps) {
  return (
    <div className="w-full max-w-2xl">
      <h3 className="text-sm font-semibold text-gray-700 mb-3">
        Perguntas sugeridas:
      </h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {SUGGESTED_QUESTIONS.map((question, index) => (
          <button
            key={index}
            onClick={() => onSelect(question)}
            className="text-left p-3 bg-white border border-gray-200 rounded-lg hover:border-primary-500 hover:bg-primary-50 transition-colors text-sm text-gray-700"
          >
            {question}
          </button>
        ))}
      </div>
    </div>
  )
}

