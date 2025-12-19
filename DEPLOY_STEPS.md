# 🚀 Passo a Passo: Deploy Railway + Vercel

## ⚡ Guia Rápido de Execução

### PRÉ-REQUISITOS
- ✅ Conta no GitHub (ou GitLab)
- ✅ Conta no Railway (https://railway.app)
- ✅ Conta no Vercel (https://vercel.com)
- ✅ OpenAI API Key
- ✅ Código commitado no Git

---

## 📦 PARTE 1: Preparar Código

### 1.1 Commit e Push

```bash
# Verificar status
git status

# Adicionar todos os arquivos
git add .

# Commit
git commit -m "Prepare for production deploy"

# Push (se ainda não fez)
git remote add origin SEU_REPOSITORIO_URL
git push -u origin main
```

---

## 🔧 PARTE 2: Deploy Backend no Railway

### 2.1 Criar Projeto no Railway

1. Acesse: https://railway.app
2. **Login** com GitHub
3. **New Project** → **Deploy from GitHub repo**
4. Selecione seu repositório
5. Clique em **Deploy**

### 2.2 Adicionar Qdrant

1. No projeto Railway, clique em **+ New**
2. **Add Database** → **Qdrant**
3. Aguarde criação do serviço
4. Anote o nome do serviço (geralmente `qdrant`)

### 2.3 Configurar Variáveis de Ambiente

No serviço do **Backend**, vá em **Variables** e adicione:

```
OPENAI_API_KEY=sua-chave-openai-aqui
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=production
LOG_LEVEL=INFO
CORS_ORIGINS=https://seu-app.vercel.app,https://seu-app.vercel.app
INGESTION_API_KEY=uma-chave-secreta-aleatoria-aqui
```

> 💡 **Dica**: Gere uma chave aleatória para `INGESTION_API_KEY` (ex: `openssl rand -hex 32`)

### 2.4 Configurar Settings

1. **Settings** → **Root Directory**: `backend`
2. **Settings** → **Start Command**: (deixe vazio, já configurado no railway.json)

### 2.5 Aguardar Deploy

- Railway fará build automaticamente
- Aguarde até ver "Deployed"
- Anote a **URL pública** (ex: `https://seu-app.railway.app`)

### 2.6 Testar Backend

```bash
curl https://seu-app.railway.app/api/health
```

Deve retornar:
```json
{"status":"healthy","service":"Product Camp 2025 RAG API"}
```

---

## 🎨 PARTE 3: Deploy Frontend no Vercel

### 3.1 Importar Projeto

1. Acesse: https://vercel.com
2. **Login** com GitHub
3. **Add New** → **Project**
4. **Import** seu repositório
5. Clique em **Import**

### 3.2 Configurar Projeto

**Configure Project:**
- **Framework Preset**: Next.js
- **Root Directory**: `frontend`
- **Build Command**: `npm run build` (ou deixe padrão)
- **Output Directory**: `.next` (ou deixe padrão)
- **Install Command**: `cd frontend && npm install`

### 3.3 Configurar Variáveis de Ambiente

**Environment Variables:**
```
NEXT_PUBLIC_API_URL=https://seu-app.railway.app
```

> ⚠️ **IMPORTANTE**: Substitua `seu-app.railway.app` pela URL real do seu backend no Railway

### 3.4 Atualizar vercel.json

Edite `vercel.json` e substitua `YOUR_RAILWAY_URL` pela URL real:

```json
{
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://seu-app.railway.app/api/:path*"
    }
  ]
}
```

### 3.5 Deploy

1. Clique em **Deploy**
2. Aguarde build completar
3. Anote a **URL pública** (ex: `https://seu-app.vercel.app`)

### 3.6 Atualizar CORS no Railway

Volte ao Railway e atualize a variável `CORS_ORIGINS`:

```
CORS_ORIGINS=https://seu-app.vercel.app,https://seu-app.vercel.app
```

Railway reiniciará automaticamente.

---

## 📊 PARTE 4: Processar PDFs

### Opção A: Via Railway CLI (Recomendado)

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link ao projeto
railway link

# Upload PDFs (se necessário)
# Copie PDFs para data/pdfs/ localmente primeiro

# Executar ingestão
railway run python backend/run_ingestion.py
```

### Opção B: Via Endpoint de Ingestão

```bash
curl -X POST https://seu-app.railway.app/api/ingest \
  -H "X-API-Key: sua-chave-secreta"
```

> ⚠️ **IMPORTANTE**: Use a mesma chave configurada em `INGESTION_API_KEY`

### Opção C: Via Volume no Railway

1. No Railway, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume
3. Execute ingestão via CLI ou endpoint

---

## ✅ Verificação Final

### Testar Backend
```bash
# Health check
curl https://seu-app.railway.app/api/health

# Teste de chat
curl -X POST https://seu-app.railway.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "Teste", "filters": null}'
```

### Testar Frontend
1. Acesse: `https://seu-app.vercel.app`
2. Faça uma pergunta de teste
3. Verifique se recebe resposta

### Verificar Qdrant
1. No Railway, abra o serviço Qdrant
2. Verifique logs
3. Verifique se há dados (via dashboard se disponível)

---

## 🔧 Troubleshooting

### Backend não inicia
- Verificar logs no Railway
- Verificar se `gunicorn` está instalado
- Verificar variáveis de ambiente

### Frontend não conecta
- Verificar `NEXT_PUBLIC_API_URL`
- Verificar CORS no backend
- Verificar console do navegador (F12)

### Qdrant não conecta
- Verificar `QDRANT_HOST` (deve ser o nome do serviço)
- Verificar se Qdrant está no mesmo projeto
- Verificar logs do Qdrant

### PDFs não processados
- Verificar se PDFs estão acessíveis
- Verificar logs da ingestão
- Verificar permissões

---

## 📝 Checklist Completo

### Preparação
- [ ] Código commitado no Git
- [ ] Repositório no GitHub
- [ ] Contas criadas (Railway, Vercel)

### Backend (Railway)
- [ ] Projeto criado
- [ ] Qdrant adicionado
- [ ] Variáveis de ambiente configuradas
- [ ] Root directory: `backend`
- [ ] Deploy realizado
- [ ] Health check funcionando
- [ ] URL anotada

### Frontend (Vercel)
- [ ] Projeto importado
- [ ] Root directory: `frontend`
- [ ] `NEXT_PUBLIC_API_URL` configurada
- [ ] `vercel.json` atualizado
- [ ] Deploy realizado
- [ ] URL anotada
- [ ] CORS atualizado no backend

### PDFs
- [ ] PDFs disponíveis
- [ ] Ingestão executada
- [ ] Chunks no Qdrant

### Testes
- [ ] Backend respondendo
- [ ] Frontend acessível
- [ ] Chat funcionando
- [ ] Respostas sendo geradas

---

**Deploy completo! 🎉**

