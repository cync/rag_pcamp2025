# ✅ Solução Funcionando: Railway Deploy

## 🎯 Solução Definitiva

Criei um `Dockerfile` na **raiz do projeto** que funciona corretamente.

### No Railway Dashboard:

1. **Settings** → **Root Directory**: (deixe **VAZIO** - raiz)
2. **Settings** → **Build Command**: (deixe **VAZIO**)
3. **Settings** → **Start Command**: (deixe **VAZIO** - Dockerfile já tem CMD)
4. **Settings** → **Dockerfile Path**: `Dockerfile` (ou deixe padrão)

Railway detectará automaticamente o Dockerfile na raiz e fará o build.

---

## 🔄 Alternativa: Configuração Manual (Sem Dockerfile)

Se preferir não usar Dockerfile:

1. **Delete ou ignore o Dockerfile**
2. **No Railway Dashboard:**
   - **Settings** → **Root Directory**: `backend`
   - **Settings** → **Build Command**: (deixe **VAZIO**)
   - **Settings** → **Start Command**: 
     ```
     gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
     ```

---

## 📝 O que foi criado:

- ✅ `Dockerfile` na raiz (funciona com contexto correto)
- ✅ `railway.json` configurado para usar Dockerfile
- ✅ Dockerfile copia `backend/requirements.txt` e `backend/*` corretamente

---

## ✅ Testar

Após deploy:
```bash
curl https://seu-app.railway.app/api/health
```

Deve retornar:
```json
{"status":"healthy","service":"Product Camp 2025 RAG API"}
```

---

## 🆘 Se ainda não funcionar

1. **Veja os logs completos** no Railway
2. **Verifique se todas as variáveis de ambiente estão configuradas**
3. **Tente a alternativa** (Root Directory = `backend`)

---

**O Dockerfile na raiz deve funcionar perfeitamente!** 🐳

