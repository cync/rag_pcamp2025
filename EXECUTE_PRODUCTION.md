# 🚀 Executar Processamento em Produção - Passo a Passo

## ✅ Railway CLI Instalado

O Railway CLI está instalado. Agora você precisa:

---

## 📋 Passo a Passo

### 1. Login no Railway

Abra um terminal PowerShell e execute:

```powershell
railway login
```

Isso abrirá o navegador para autenticação.

### 2. Link ao Projeto

```powershell
railway link
```

Selecione o projeto do Product Camp 2025.

### 3. Verificar Variáveis de Ambiente

Certifique-se de que no Railway Dashboard estão configuradas:
- ✅ `OPENAI_API_KEY` (já configurada)
- ✅ `QDRANT_HOST` (nome do serviço Qdrant)
- ✅ `QDRANT_PORT` (6333)
- ✅ `QDRANT_COLLECTION_NAME` (product_camp_2025)

### 4. Upload PDFs (se necessário)

Os PDFs precisam estar acessíveis no Railway. Opções:

**Opção A: Via Volume**
1. No Railway, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume

**Opção B: Os PDFs já estão no Git**
- Railway pode acessá-los durante o build
- Mas precisam estar commitados no repositório

### 5. Processar PDFs

```powershell
# Processar Dia 1
railway run python backend/run_ingestion_dia.py dia1

# Processar Dia 2  
railway run python backend/run_ingestion_dia.py dia2

# Ou processar todos
railway run python backend/run_ingestion_dia.py all
```

---

## 🔄 Alternativa: Via Endpoint de Ingestão

Se você configurou `INGESTION_API_KEY` no Railway:

```powershell
$apiKey = "sua-chave-secreta"
$railwayUrl = "https://seu-app.railway.app"

Invoke-WebRequest -Uri "$railwayUrl/api/ingest" `
  -Method POST `
  -Headers @{"X-API-Key" = $apiKey}
```

**Nota**: Para isso funcionar, os PDFs precisam estar no container.

---

## 📝 Verificar Logs

Durante o processamento, veja os logs:

```powershell
railway logs
```

Ou no Railway Dashboard → **Deployments** → **Logs**

---

## ✅ Após Processar

Teste a API:

```powershell
$railwayUrl = "https://seu-app.railway.app"
Invoke-WebRequest -Uri "$railwayUrl/api/chat" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"question": "Quais palestras foram no Dia 1?", "filters": null}'
```

---

**Execute os comandos acima no seu terminal! 🚀**

