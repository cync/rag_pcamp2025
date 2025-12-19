# Product Camp 2025 - Sistema RAG

Sistema completo de Retrieval-Augmented Generation (RAG) para consultas sobre palestras do Product Camp 2025.

## 🎯 Objetivo

Permitir que participantes do evento façam perguntas e consultas sobre todas as palestras, com base exclusivamente nos PDFs das apresentações, recebendo respostas contextualizadas, confiáveis e citadas.

## 🏗️ Arquitetura

- **Frontend**: Next.js 14 + React + TypeScript + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Vector Database**: Qdrant
- **LLM**: OpenAI (GPT-4 ou GPT-3.5-turbo)
- **Embeddings**: OpenAI text-embedding-ada-002

## 📁 Estrutura do Projeto

```
.
├── backend/
│   ├── api/              # Endpoints da API
│   │   ├── chat.py       # Endpoint /chat
│   │   └── health.py     # Health check
│   ├── rag/              # Módulo RAG
│   │   ├── rag_engine.py      # Motor principal RAG
│   │   ├── vector_store.py    # Interface com Qdrant
│   │   └── embeddings.py      # Geração de embeddings
│   ├── ingestion/        # Pipeline de ingestão
│   │   ├── pdf_processor.py   # Processamento de PDFs
│   │   ├── chunking.py        # Divisão em chunks
│   │   └── ingestion_pipeline.py  # Pipeline completo
│   ├── main.py           # Aplicação FastAPI
│   └── requirements.txt  # Dependências Python
│
├── frontend/
│   ├── app/              # Next.js App Router
│   ├── components/       # Componentes React
│   ├── services/         # Serviços de API
│   ├── types/           # TypeScript types
│   └── package.json     # Dependências Node
│
└── data/
    └── pdfs/            # Diretório para PDFs das palestras
```

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.9+
- Node.js 18+
- Qdrant (Docker ou instalação local)

### 1. Instalar Qdrant

**Opção A: Docker (Recomendado)**
```bash
docker run -p 6333:6333 qdrant/qdrant
```

**Opção B: Instalação Local**
Siga as instruções em: https://qdrant.tech/documentation/guides/installation/

### 2. Configurar Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Copiar e configurar variáveis de ambiente
cp .env.example .env
# Editar .env e adicionar sua OPENAI_API_KEY
```

### 3. Configurar Frontend

```bash
cd frontend

# Instalar dependências
npm install

# Copiar e configurar variáveis de ambiente
cp .env.example .env.local
# Editar .env.local se necessário (API_URL)
```

## 📊 Ingestão de PDFs

Antes de usar o sistema, é necessário processar os PDFs das palestras:

1. **Colocar PDFs no diretório**:
   ```bash
   mkdir -p data/pdfs
   # Copiar seus PDFs para data/pdfs/
   ```

2. **Executar pipeline de ingestão**:
   ```bash
   cd backend
   python -m ingestion.ingestion_pipeline
   ```

   O pipeline irá:
   - Extrair texto de cada PDF
   - Dividir em chunks semânticos
   - Gerar embeddings
   - Armazenar no Qdrant

### Formato de Nome dos PDFs (Opcional)

Para melhor organização, você pode nomear os PDFs com metadados:
```
Titulo_Palestra_Palestrante_Tipo_Tema.pdf
```

Exemplo:
```
Estrategia_Produto_Joao_Silva_keynote_estrategia.pdf
```

Se não seguir esse formato, o sistema usará valores padrão.

## 🏃 Executar Aplicação

### Backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API estará disponível em: http://localhost:8000

### Frontend

```bash
cd frontend
npm run dev
```

Aplicação estará disponível em: http://localhost:3000

## 📝 Uso

1. Acesse http://localhost:3000
2. Faça perguntas sobre as palestras
3. Receba respostas contextualizadas com citações das fontes

### Exemplos de Perguntas

- "Quais são os principais temas abordados nas palestras?"
- "Quem são os palestrantes do evento?"
- "Quais frameworks de produto foram mencionados?"
- "Há alguma palestra sobre estratégia de produto?"
- "Compare as abordagens de diferentes palestrantes sobre X"

## 🔧 Configurações Avançadas

### Ajustar Modelo LLM

No arquivo `backend/rag/rag_engine.py`, altere:
```python
self.model = "gpt-4-turbo-preview"  # ou "gpt-3.5-turbo"
```

### Ajustar Parâmetros de Busca

No arquivo `backend/rag/vector_store.py`:
- `top_k`: Número de chunks a recuperar (padrão: 5)
- `score_threshold`: Threshold mínimo de relevância (padrão: 0.3)

### Ajustar Chunking

No arquivo `backend/ingestion/chunking.py`, você pode ajustar:
- Tamanho máximo dos chunks
- Estratégia de divisão
- Overlap entre chunks

## 🧪 Testes

### Testar API diretamente

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quais são os principais temas das palestras?",
    "filters": null
  }'
```

### Health Check

```bash
curl http://localhost:8000/api/health
```

## 📚 Documentação da API

Acesse a documentação interativa em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Next.js**: Framework React para produção
- **Qdrant**: Banco de dados vetorial
- **OpenAI**: LLM e embeddings
- **Tailwind CSS**: Framework CSS utilitário
- **TypeScript**: Tipagem estática para JavaScript

## 📋 Checklist de Deploy

- [ ] Configurar variáveis de ambiente
- [ ] Instalar e configurar Qdrant
- [ ] Processar todos os PDFs (ingestão)
- [ ] Testar API endpoints
- [ ] Testar frontend
- [ ] Configurar CORS para produção
- [ ] Configurar domínio/URLs
- [ ] Revisar logs e monitoramento

## 🤝 Contribuindo

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto foi desenvolvido para o Product Camp 2025.

## 🆘 Suporte

Para problemas ou dúvidas:
1. Verifique os logs do backend
2. Verifique se o Qdrant está rodando
3. Verifique se a OPENAI_API_KEY está configurada
4. Verifique se os PDFs foram processados corretamente

---

**Desenvolvido com ❤️ para Product Camp 2025**

