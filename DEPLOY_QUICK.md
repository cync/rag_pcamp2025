# ⚡ Deploy Rápido: Railway + Vercel

## 🎯 Resumo Executivo

**Backend**: Railway.app  
**Frontend**: Vercel  
**Tempo estimado**: 15-20 minutos

---

## 📋 Checklist Rápido

### 1. Preparar Código (2 min)
```bash
git add .
git commit -m "Prepare for production"
git push
```

### 2. Railway - Backend (5 min)

1. **Acesse**: https://railway.app → New Project → GitHub repo
2. **Adicione Qdrant**: + New → Add Database → Qdrant
3. **Variáveis de Ambiente**:
   ```
   OPENAI_API_KEY=sua-chave
   QDRANT_HOST=qdrant
   QDRANT_PORT=6333
   CORS_ORIGINS=https://seu-app.vercel.app
   ```
4. **Settings**: Root Directory = `backend`
5. **Aguarde deploy** → Anote URL

### 3. Vercel - Frontend (5 min)

1. **Acesse**: https://vercel.com → Import Project
2. **Configurações**:
   - Root Directory: `frontend`
   - Framework: Next.js
3. **Environment Variable**:
   ```
   NEXT_PUBLIC_API_URL=https://seu-app.railway.app
   ```
4. **Deploy** → Anote URL

### 4. Atualizar CORS (1 min)

No Railway, atualize:
```
CORS_ORIGINS=https://seu-app.vercel.app
```

### 5. Processar PDFs (5 min)

```bash
npm i -g @railway/cli
railway login
railway link
railway run python backend/run_ingestion.py
```

---

## ✅ Testar

- Backend: `https://seu-app.railway.app/api/health`
- Frontend: `https://seu-app.vercel.app`

---

**Pronto! 🚀**

Para detalhes completos, veja `DEPLOY_STEPS.md`

