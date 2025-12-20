# 🧪 Testar Após Correção da Configuração

## ✅ Correção Aplicada

O Dockerfile foi atualizado para:
- ✅ Usar variável `PORT` do Railway dinamicamente
- ✅ Bind em `0.0.0.0` (todas as interfaces)
- ✅ Configurado para produção

---

## 🧪 Testar Manualmente

### 1. Testar Health Check

No PowerShell ou terminal:

```powershell
$url = "https://pcamp2025.up.railway.app"
Invoke-WebRequest -Uri "$url/api/health"
```

**Ou usando curl (se disponível):**
```bash
curl https://pcamp2025.up.railway.app/api/health
```

**Resposta esperada:**
```json
{"status":"healthy","service":"Product Camp 2025 RAG API"}
```

### 2. Processar PDFs

```powershell
$url = "https://pcamp2025.up.railway.app"
$apiKey = "fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB"

Invoke-WebRequest -Uri "$url/api/ingest" `
  -Method POST `
  -Headers @{"X-API-Key" = $apiKey} `
  -ContentType "application/json"
```

**Ou usando curl:**
```bash
curl -X POST https://pcamp2025.up.railway.app/api/ingest \
  -H "X-API-Key: fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB" \
  -H "Content-Type: application/json"
```

---

## ⏳ Aguardar Deploy

O Railway está fazendo deploy automático após o push. Aguarde:

1. **2-3 minutos** para o deploy completar
2. Verifique no Railway Dashboard → Backend → Deployments
3. Aguarde até mostrar **"Deployed"** (verde)
4. Teste novamente

---

## 🔍 Verificar Logs

Se ainda retornar 502:

1. Railway Dashboard → Backend → **Logs**
2. Veja os logs mais recentes
3. Procure por:
   - "Application startup complete"
   - Erros após o startup
   - Mensagens sobre porta

---

## ✅ O que foi corrigido

- ✅ Dockerfile agora usa `${PORT}` do Railway
- ✅ Bind em `0.0.0.0` para aceitar conexões de qualquer IP
- ✅ Configurado para produção

---

**Aguarde o deploy completar e teste manualmente! 🚀**

