# 🔧 Corrigir Erro "Connection Refused" no Railway

## 🔴 Problema Identificado

O Railway está retornando erro **502** com "connection refused", o que significa que:
- ❌ O container não está respondendo na porta esperada
- ❌ O container pode estar crashando ao iniciar
- ❌ A porta pode não estar configurada corretamente

---

## 🔍 Diagnóstico Passo a Passo

### 1. Verificar Logs no Railway

1. Acesse: https://railway.app
2. Abra seu projeto → Serviço Backend
3. Vá em **Logs**
4. Procure por:
   - Erros de inicialização
   - Mensagens sobre porta
   - Erros de importação de módulos
   - Erros de variáveis de ambiente

### 2. Verificar Variáveis de Ambiente

No Railway Dashboard → Backend → **Variables**, confirme:

#### Obrigatórias:
- ✅ `OPENAI_API_KEY` - Configurada?
- ✅ `QDRANT_URL` - Configurada?
- ✅ `QDRANT_API_KEY` - Configurada?
- ✅ `QDRANT_COLLECTION_NAME` - Configurada?

#### Opcionais (mas importantes):
- ✅ `INGESTION_API_KEY` - Configurada?
- ✅ `ENVIRONMENT` - `production`
- ✅ `LOG_LEVEL` - `INFO`

### 3. Verificar Porta

O Railway usa a variável `PORT` automaticamente. Verifique:

1. Railway Dashboard → Backend → **Settings**
2. Verifique se há alguma configuração de porta
3. O código deve usar `PORT` do ambiente (já configurado no Dockerfile)

---

## 🛠️ Soluções Comuns

### Solução 1: Verificar Erros nos Logs

Os logs podem mostrar:
- `OPENAI_API_KEY não encontrada` → Adicione a variável
- `Erro ao conectar ao Qdrant` → Verifique QDRANT_URL e QDRANT_API_KEY
- `ModuleNotFoundError` → Problema no código (improvável)
- `ImportError` → Problema no código (improvável)

### Solução 2: Verificar Dockerfile

O Dockerfile deve estar configurado para usar a variável `PORT`:

```dockerfile
CMD ["sh", "-c", "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000}"]
```

Isso já está configurado corretamente.

### Solução 3: Forçar Redeploy

1. Railway Dashboard → Backend → **Settings**
2. Clique em **Redeploy** ou **Deploy**
3. Aguarde o deploy completar
4. Verifique os logs novamente

### Solução 4: Verificar Build Logs

1. Railway Dashboard → Backend → **Deployments**
2. Clique no deployment mais recente
3. Veja os logs de build
4. Procure por erros durante o build

---

## ✅ Checklist de Diagnóstico

- [ ] Logs mostram erros específicos?
- [ ] Todas as variáveis de ambiente estão configuradas?
- [ ] O deploy está completo (verde)?
- [ ] Build foi bem-sucedido?
- [ ] Tentei fazer redeploy?

---

## 🚀 Após Corrigir

Quando o backend estiver rodando corretamente:

1. **Teste o health check:**
   ```powershell
   $url = "https://web-production-42847.up.railway.app"
   Invoke-WebRequest -Uri "$url/api/health"
   ```

2. **Deve retornar:**
   ```json
   {"status":"healthy","service":"Product Camp 2025 RAG API"}
   ```

3. **Processe os PDFs:**
   ```powershell
   .\process_with_retry.ps1
   ```

---

## 📝 Próximos Passos

1. **Verifique os logs no Railway Dashboard**
2. **Identifique o erro específico**
3. **Corrija o problema**
4. **Faça redeploy se necessário**
5. **Teste novamente**

---

**Verifique os logs no Railway Dashboard para identificar o erro específico! 🔍**

