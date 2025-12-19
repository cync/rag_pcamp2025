# 🔍 Diagnóstico: Backend Railway com Erro 502

## ❌ Problema

O backend está retornando erro **502 Bad Gateway**, o que significa que o serviço não está respondendo corretamente.

---

## 🔧 Verificar no Railway Dashboard

### 1. Verificar Status do Serviço

1. Acesse: https://railway.app
2. Abra seu projeto
3. Clique no serviço **Backend**
4. Verifique se está **"Deployed"** (verde)

### 2. Verificar Logs

1. No serviço Backend, vá em **Logs**
2. Procure por erros recentes
3. Erros comuns:
   - `OPENAI_API_KEY não encontrada`
   - `Erro ao conectar ao Qdrant`
   - `ModuleNotFoundError`
   - `ImportError`

### 3. Verificar Variáveis de Ambiente

No serviço Backend, vá em **Variables** e verifique se estão configuradas:

#### Obrigatórias:
- ✅ `OPENAI_API_KEY` - Sua chave da OpenAI
- ✅ `QDRANT_HOST` - Nome do serviço Qdrant (ex: `qdrant`)
- ✅ `QDRANT_PORT` - `6333`
- ✅ `QDRANT_COLLECTION_NAME` - `product_camp_2025`

#### Opcionais (mas recomendadas):
- `ENVIRONMENT` - `production`
- `LOG_LEVEL` - `INFO`
- `CORS_ORIGINS` - URL do frontend
- `INGESTION_API_KEY` - Chave para processar PDFs

### 4. Verificar Qdrant

1. No projeto Railway, verifique se há um serviço **Qdrant**
2. Se não houver, adicione:
   - **+ New** → **Add Database** → **Qdrant**
3. O nome do serviço deve estar em `QDRANT_HOST`

---

## 🚀 Soluções Comuns

### Solução 1: Variáveis de Ambiente Faltando

Se `OPENAI_API_KEY` não estiver configurada:

1. Vá em **Variables**
2. Adicione: `OPENAI_API_KEY=sk-sua-chave-aqui`
3. Railway fará redeploy automaticamente
4. Aguarde o deploy completar

### Solução 2: Qdrant Não Conectado

Se `QDRANT_HOST` estiver incorreto:

1. Verifique o nome do serviço Qdrant no Railway
2. Atualize `QDRANT_HOST` com o nome correto
3. Railway fará redeploy automaticamente

### Solução 3: Erro no Código

Se houver erros de importação ou código:

1. Verifique os logs no Railway
2. Verifique se o código está atualizado no Git
3. Force um novo deploy:
   - **Settings** → **Redeploy**

---

## ✅ Testar Após Corrigir

### 1. Health Check

```powershell
$url = "https://web-production-42847.up.railway.app"
Invoke-WebRequest -Uri "$url/api/health"
```

Deve retornar:
```json
{"status":"healthy","service":"Product Camp 2025 RAG API"}
```

### 2. Processar PDFs

Após o backend estar funcionando:

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "sua-chave-secreta"
```

---

## 📝 Checklist de Diagnóstico

- [ ] Serviço Backend está "Deployed" (verde)
- [ ] Logs não mostram erros críticos
- [ ] `OPENAI_API_KEY` configurada
- [ ] `QDRANT_HOST` configurado corretamente
- [ ] Serviço Qdrant existe e está rodando
- [ ] Health check retorna 200 OK
- [ ] `INGESTION_API_KEY` configurada (para processar PDFs)

---

**Corrija os problemas acima e tente novamente! 🚀**

