# 🔧 Corrigir Erro 502 no Railway

## 🔴 Problema

Ambas as URLs estão retornando **502 Gateway Error**:
- `https://web-production-42847.up.railway.app`
- `https://pcamp2025.up.railway.app`

Isso significa que o **backend não está respondendo** corretamente.

---

## 🔍 Diagnóstico Passo a Passo

### 1. Verificar Logs no Railway Dashboard

1. Acesse: https://railway.app
2. Abra seu projeto → Serviço Backend
3. Vá em **Logs**
4. Veja os logs **mais recentes** (últimos 5 minutos)
5. Procure por:
   - ✅ "Application startup complete" (backend iniciou)
   - ❌ Erros após o startup
   - ❌ Mensagens de crash
   - ❌ Erros de variáveis faltando

### 2. Erros Comuns nos Logs

#### Erro 1: Variável Faltando
```
ValueError: OPENAI_API_KEY não encontrada
```
**Solução**: Adicione `OPENAI_API_KEY` no Railway → Variables

#### Erro 2: Qdrant Não Conecta
```
Erro ao conectar ao Qdrant
```
**Solução**: Verifique `QDRANT_URL` e `QDRANT_API_KEY`

#### Erro 3: Container Crashando
```
Traceback (most recent call last):
...
```
**Solução**: Veja o erro específico e corrija

### 3. Verificar Variáveis de Ambiente

No Railway Dashboard → Backend → **Variables**, confirme:

#### Obrigatórias:
- ✅ `OPENAI_API_KEY` - Sua chave da OpenAI
- ✅ `QDRANT_URL` - URL completa do cluster (https://...)
- ✅ `QDRANT_API_KEY` - Sua chave do Qdrant Cloud
- ✅ `QDRANT_COLLECTION_NAME` - `product_camp_2025`

#### Opcionais (mas recomendadas):
- ✅ `INGESTION_API_KEY` - `fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB`
- ✅ `ENVIRONMENT` - `production`
- ✅ `LOG_LEVEL` - `INFO`

### 4. Verificar Status do Deploy

No Railway Dashboard → Backend:
- Status deve mostrar **"Deployed"** (verde)
- Se mostrar **"Building"** ou **"Failed"**, há um problema

---

## 🛠️ Soluções

### Solução 1: Verificar e Corrigir Erros nos Logs

1. Identifique o erro específico nos logs
2. Corrija o problema (variável faltando, etc.)
3. Railway fará redeploy automático
4. Aguarde o deploy completar
5. Teste novamente

### Solução 2: Forçar Redeploy

1. Railway Dashboard → Backend → **Settings**
2. Clique em **Redeploy**
3. Aguarde o deploy completar
4. Verifique os logs
5. Teste novamente

### Solução 3: Verificar Build Logs

1. Railway Dashboard → Backend → **Deployments**
2. Clique no deployment mais recente
3. Veja os logs de build
4. Procure por erros durante o build

---

## ✅ Após Corrigir

Quando o backend estiver funcionando:

1. **Teste o health check:**
   ```powershell
   $url = "https://pcamp2025.up.railway.app"
   Invoke-WebRequest -Uri "$url/api/health"
   ```
   Deve retornar: `{"status":"healthy","service":"Product Camp 2025 RAG API"}`

2. **Processe os PDFs:**
   ```powershell
   .\PROCESS_WITH_URL.ps1
   ```

---

## 📝 Checklist

- [ ] Logs verificados no Railway Dashboard
- [ ] Erro específico identificado
- [ ] Variáveis de ambiente todas configuradas
- [ ] Deploy status = "Deployed" (verde)
- [ ] Health check retorna 200 OK
- [ ] Processamento executado com sucesso

---

**Verifique os logs no Railway Dashboard e compartilhe os erros encontrados para eu ajudar a corrigir! 🔍**

