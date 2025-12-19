# 🚀 Deploy: Railway (Backend) + Vercel (Frontend)

## 📋 Visão Geral

- **Backend**: Railway.app (FastAPI + Qdrant)
- **Frontend**: Vercel (Next.js)

---

## 🔧 PARTE 1: Deploy do Backend no Railway

### Passo 1: Preparar Repositório

1. **Criar repositório Git** (se ainda não tem):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push para GitHub/GitLab**:
   ```bash
   git remote add origin seu-repositorio-url
   git push -u origin main
   ```

### Passo 2: Configurar Railway

1. **Acesse**: https://railway.app
2. **Crie conta** (pode usar GitHub)
3. **New Project** → **Deploy from GitHub repo**
4. **Selecione seu repositório**

### Passo 3: Configurar Variáveis de Ambiente

No Railway, vá em **Variables** e adicione:

```
OPENAI_API_KEY=sua-chave-openai
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=production
LOG_LEVEL=INFO
```

### Passo 4: Adicionar Qdrant no Railway

1. **No mesmo projeto Railway**, clique em **+ New**
2. **Add Database** → **Qdrant**
3. Railway criará automaticamente um serviço Qdrant
4. **Atualize a variável** `QDRANT_HOST` com o host do Qdrant criado
   - Railway fornece automaticamente via variável `QDRANT_HOST`
   - Ou use o nome do serviço: `qdrant`

### Passo 5: Configurar Build

Railway detecta automaticamente Python, mas vamos garantir:

1. **Settings** → **Build Command**: (deixe vazio ou remova)
2. **Settings** → **Start Command**: 
   ```
   cd backend && gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
   ```
3. **Settings** → **Root Directory**: `backend`

### Passo 6: Adicionar Arquivo railway.json (Opcional)

Criar `railway.json` na raiz:
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "cd backend && gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Passo 7: Adicionar requirements.txt com gunicorn

Verificar se `backend/requirements.txt` tem:
```
gunicorn==21.2.0
```

### Passo 8: Deploy

1. Railway fará deploy automaticamente ao fazer push
2. Ou clique em **Deploy** manualmente
3. Aguarde o build completar
4. Anote a **URL pública** (ex: `https://seu-app.railway.app`)

### Passo 9: Processar PDFs (Ingestão)

**Opção A: Via Railway CLI**
```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link ao projeto
railway link

# Executar ingestão
cd backend
railway run python run_ingestion.py
```

**Opção B: Via Terminal SSH do Railway**
1. No Railway, vá em **Settings** → **Deployments**
2. Clique no deployment mais recente
3. Abra **Shell**
4. Execute:
   ```bash
   cd backend
   python run_ingestion.py
   ```

**Opção C: Criar endpoint temporário para ingestão**
(Ver seção abaixo)

---

## 🎨 PARTE 2: Deploy do Frontend no Vercel

### Passo 1: Preparar Frontend

1. **Criar arquivo `vercel.json`** na raiz do projeto:
```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/.next",
  "installCommand": "cd frontend && npm install",
  "framework": "nextjs",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://seu-backend.railway.app/api/:path*"
    }
  ]
}
```

### Passo 2: Configurar Variáveis de Ambiente

No Vercel, você precisará configurar:

1. **Acesse**: https://vercel.com
2. **Import Project** → Selecione seu repositório
3. **Configure Project**:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Next.js
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

4. **Environment Variables**:
   ```
   NEXT_PUBLIC_API_URL=https://seu-backend.railway.app
   ```

### Passo 3: Deploy

1. Vercel fará deploy automaticamente
2. Aguarde o build
3. Anote a **URL pública** (ex: `https://seu-app.vercel.app`)

### Passo 4: Atualizar CORS no Backend

No Railway, atualize as variáveis de ambiente do backend:

```
CORS_ORIGINS=https://seu-app.vercel.app,https://seu-app.vercel.app
```

E atualize `backend/main.py` para usar essa variável.

---

## 🔄 PARTE 3: Atualizar Código para Produção

### Atualizar CORS no Backend

Editar `backend/main.py`:

```python
# Configurar CORS
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Atualizar URL da API no Frontend

O frontend já usa `NEXT_PUBLIC_API_URL`, então basta configurar no Vercel.

---

## 📊 PARTE 4: Processar PDFs em Produção

### Opção A: Endpoint de Ingestão (Recomendado)

Criar endpoint temporário para executar ingestão:

**Criar `backend/api/ingestion.py`:**
```python
from fastapi import APIRouter, HTTPException
from ingestion.ingestion_pipeline import IngestionPipeline
import os

ingestion_router = APIRouter()

@ingestion_router.post("/ingest")
async def run_ingestion():
    """Endpoint para executar ingestão de PDFs"""
    # Proteger com API key em produção
    api_key = os.getenv("INGESTION_API_KEY")
    if not api_key:
        raise HTTPException(status_code=403, detail="Ingestion not configured")
    
    try:
        pipeline = IngestionPipeline()
        pipeline.run()
        return {"status": "success", "message": "Ingestion completed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Adicionar ao `backend/main.py`:**
```python
from api.ingestion import ingestion_router
app.include_router(ingestion_router, prefix="/api", tags=["ingestion"])
```

**Chamar via curl:**
```bash
curl -X POST https://seu-backend.railway.app/api/ingest \
  -H "X-API-Key: sua-chave-secreta"
```

### Opção B: Railway CLI (Mais Seguro)

```bash
railway run python backend/run_ingestion.py
```

---

## ✅ Checklist Final

### Backend (Railway)
- [ ] Repositório no GitHub
- [ ] Projeto criado no Railway
- [ ] Qdrant adicionado como serviço
- [ ] Variáveis de ambiente configuradas
- [ ] Build configurado
- [ ] Deploy realizado
- [ ] URL pública anotada
- [ ] Health check funcionando: `https://seu-backend.railway.app/api/health`

### Frontend (Vercel)
- [ ] Projeto importado no Vercel
- [ ] Root directory: `frontend`
- [ ] Variável `NEXT_PUBLIC_API_URL` configurada
- [ ] Deploy realizado
- [ ] URL pública anotada
- [ ] Teste de conexão com backend

### PDFs
- [ ] PDFs enviados para Railway (via volume ou upload)
- [ ] Ingestão executada
- [ ] Chunks armazenados no Qdrant

### Testes
- [ ] Frontend acessível
- [ ] Backend respondendo
- [ ] Chat funcionando
- [ ] Respostas sendo geradas

---

## 🔧 Troubleshooting

### Backend não inicia no Railway
- Verificar logs no Railway
- Verificar se `gunicorn` está no requirements.txt
- Verificar variáveis de ambiente

### Frontend não conecta ao backend
- Verificar `NEXT_PUBLIC_API_URL`
- Verificar CORS no backend
- Verificar se backend está acessível publicamente

### Qdrant não conecta
- Verificar variável `QDRANT_HOST`
- Verificar se Qdrant está no mesmo projeto Railway
- Verificar logs do serviço Qdrant

### PDFs não processados
- Verificar se PDFs estão acessíveis
- Verificar logs da ingestão
- Verificar permissões de arquivo

---

## 📝 Notas Importantes

1. **Custos**: Railway e Vercel têm planos gratuitos, mas verifique limites
2. **PDFs**: Considere usar storage externo (S3, etc.) para PDFs grandes
3. **Segurança**: Proteja endpoints de ingestão com API keys
4. **Monitoramento**: Configure alertas no Railway e Vercel
5. **Backup**: Configure backup do Qdrant

---

**Pronto para deploy! 🚀**

