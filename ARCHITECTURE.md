# Arquitetura do Sistema RAG

## Visão Geral

```
┌─────────────────┐
│   Frontend       │
│   (Next.js)      │
│   Port: 3000     │
└────────┬────────┘
         │ HTTP/REST
         │
┌────────▼────────┐
│   Backend API    │
│   (FastAPI)      │
│   Port: 8000     │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│ Qdrant│ │OpenAI │
│ :6333 │ │ API   │
└───────┘ └───────┘
```

## Fluxo de Dados

### 1. Pipeline de Ingestão (Offline)

```
PDFs → PDF Processor → Chunking → Embeddings → Qdrant
```

1. **PDF Processor**: Extrai texto de cada PDF
2. **Chunking**: Divide texto em chunks semânticos
3. **Embeddings**: Gera vetores usando OpenAI
4. **Qdrant**: Armazena vetores + metadados

### 2. Fluxo de Consulta (Online)

```
User Question → Embedding → Qdrant Search → Context → LLM → Response
```

1. **User Question**: Pergunta do usuário
2. **Embedding**: Gera vetor da pergunta
3. **Qdrant Search**: Busca chunks relevantes
4. **Context Building**: Monta contexto com chunks
5. **LLM**: Gera resposta usando GPT-4
6. **Response**: Retorna resposta + fontes

## Componentes Principais

### Backend

#### `api/chat.py`
- Endpoint `/api/chat`
- Recebe perguntas e filtros
- Retorna respostas contextualizadas

#### `rag/rag_engine.py`
- Motor principal RAG
- Orquestra busca e geração
- Gerencia prompt engineering

#### `rag/vector_store.py`
- Interface com Qdrant
- Busca semântica
- Filtros por metadados

#### `rag/embeddings.py`
- Geração de embeddings
- Usa OpenAI text-embedding-ada-002

#### `ingestion/`
- Pipeline completo de ingestão
- Processamento de PDFs
- Chunking e indexação

### Frontend

#### `components/ChatInterface.tsx`
- Interface principal de chat
- Gerencia estado das mensagens
- Integração com API

#### `components/ChatMessage.tsx`
- Exibe mensagens do chat
- Mostra fontes citadas

#### `components/ChatInput.tsx`
- Input de perguntas
- Envio de mensagens

#### `services/chatService.ts`
- Cliente HTTP para API
- Comunicação com backend

## Estrutura de Dados

### Chunk no Qdrant

```json
{
  "id": 123456789,
  "vector": [0.123, -0.456, ...],
  "payload": {
    "text": "Conteúdo do chunk...",
    "titulo_palestra": "Estratégia de Produto",
    "palestrante": "João Silva",
    "tipo": "keynote",
    "tema": "estratégia",
    "pagina_ou_slide": "1-1",
    "fonte": "Product Camp 2025"
  }
}
```

### Request/Response

**Request:**
```json
{
  "question": "Quais são os principais temas?",
  "filters": {
    "palestrante": "João Silva",
    "tipo": "keynote"
  }
}
```

**Response:**
```json
{
  "answer": "Resposta gerada pelo LLM...",
  "sources": [
    {
      "titulo_palestra": "...",
      "palestrante": "...",
      "tipo": "...",
      "tema": "...",
      "pagina_ou_slide": "...",
      "score": 0.85
    }
  ],
  "query": "Quais são os principais temas?"
}
```

## Prompt Engineering

### System Prompt
- Define papel do assistente
- Estabelece regras de comportamento
- Proíbe alucinações

### User Prompt
- Inclui contexto das palestras
- Formatação clara
- Instruções específicas

### Estratégias
- Baixa temperatura (0.1) para precisão
- Contexto estruturado com citações
- Instruções explícitas sobre fontes

## Segurança e Boas Práticas

- Variáveis de ambiente para secrets
- Validação de inputs (Pydantic)
- Tratamento de erros robusto
- Logging estruturado
- CORS configurado
- Type safety (TypeScript)

## Escalabilidade

### Possíveis Melhorias
- Cache de embeddings
- Rate limiting
- Async processing
- Múltiplas collections
- Sharding no Qdrant
- CDN para frontend

## Monitoramento

- Logs estruturados
- Health check endpoint
- Métricas de performance
- Tracking de queries

