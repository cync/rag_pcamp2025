# Guia de Setup Rápido

## Passo a Passo para Começar

### 1. Instalar Qdrant (Docker)

```bash
docker-compose up -d
```

Ou manualmente:
```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 2. Configurar Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env e adicionar OPENAI_API_KEY
```

### 3. Configurar Frontend

```bash
cd frontend

# Instalar dependências
npm install

# Configurar variáveis (opcional)
cp .env.example .env.local
```

### 4. Adicionar PDFs

```bash
# Criar diretório se não existir
mkdir -p data/pdfs

# Copiar seus PDFs para data/pdfs/
# Exemplo:
# cp /caminho/para/palestras/*.pdf data/pdfs/
```

### 5. Executar Ingestão

```bash
cd backend
python run_ingestion.py
```

Ou:
```bash
python -m ingestion.ingestion_pipeline
```

### 6. Iniciar Servidores

**Terminal 1 - Backend:**
```bash
cd backend
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 7. Acessar Aplicação

- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

## Verificação

1. Verificar Qdrant: http://localhost:6333/dashboard
2. Verificar API: http://localhost:8000/api/health
3. Testar chat no frontend

## Troubleshooting

### Qdrant não conecta
- Verifique se está rodando: `docker ps`
- Verifique porta 6333: `curl http://localhost:6333/health`

### Erro de OpenAI API Key
- Verifique se está no arquivo `.env`
- Verifique se a chave é válida

### PDFs não processados
- Verifique se estão em `data/pdfs/`
- Verifique se são PDFs válidos
- Verifique logs do pipeline

### Frontend não conecta ao backend
- Verifique `NEXT_PUBLIC_API_URL` no `.env.local`
- Verifique se backend está rodando na porta 8000
- Verifique CORS no backend

