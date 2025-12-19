# Exemplos de Uso

## Exemplos de Perguntas

### Perguntas Gerais
- "Quais são os principais temas abordados nas palestras?"
- "Quem são os palestrantes do evento?"
- "Resuma as principais ideias do evento"

### Perguntas Específicas
- "O que foi dito sobre estratégia de produto?"
- "Quais frameworks foram mencionados?"
- "Há alguma palestra sobre métricas de produto?"

### Comparações
- "Compare as abordagens de diferentes palestrantes sobre X"
- "Quais são as diferenças entre as palestras sobre Y?"

### Consultas por Palestrante
- "O que o palestrante [Nome] falou sobre [tema]?"
- "Quais são as principais ideias de [Nome]?"

## Exemplos de Uso da API

### cURL

```bash
# Pergunta simples
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quais são os principais temas das palestras?",
    "filters": null
  }'

# Com filtro por palestrante
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "O que foi dito sobre estratégia?",
    "filters": {
      "palestrante": "João Silva"
    }
  }'

# Com filtro por tipo
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quais são os principais pontos?",
    "filters": {
      "tipo": "keynote"
    }
  }'
```

### Python

```python
import requests

url = "http://localhost:8000/api/chat"
headers = {"Content-Type": "application/json"}

# Pergunta simples
response = requests.post(
    url,
    json={
        "question": "Quais são os principais temas das palestras?",
        "filters": None
    },
    headers=headers
)

result = response.json()
print(result["answer"])
print("\nFontes:")
for source in result["sources"]:
    print(f"- {source['titulo_palestra']} por {source['palestrante']}")
```

### JavaScript/TypeScript

```typescript
const response = await fetch('http://localhost:8000/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    question: 'Quais são os principais temas das palestras?',
    filters: null,
  }),
});

const result = await response.json();
console.log(result.answer);
console.log('Fontes:', result.sources);
```

## Resposta da API

```json
{
  "answer": "Com base nas palestras do Product Camp 2025, os principais temas abordados incluem...",
  "sources": [
    {
      "titulo_palestra": "Estratégia de Produto",
      "palestrante": "João Silva",
      "tipo": "keynote",
      "tema": "estratégia",
      "pagina_ou_slide": "1-1",
      "score": 0.85
    }
  ],
  "query": "Quais são os principais temas das palestras?"
}
```

## Filtros Disponíveis

- `palestrante`: Filtrar por nome do palestrante
- `tipo`: Filtrar por tipo (keynote, workshop, palestra)
- `tema`: Filtrar por tema/trilha

Exemplo de filtros combinados:
```json
{
  "question": "O que foi dito sobre métricas?",
  "filters": {
    "tipo": "workshop",
    "tema": "métricas"
  }
}
```

