# 🚀 Processar PDFs AGORA

## ✅ Qdrant Cloud Configurado!

Agora você pode processar os PDFs!

---

## 📋 Opções para Processar

### Opção 1: Via Script PowerShell (Recomendado)

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "sua-ingestion-api-key"
```

**Você precisa:**
- `INGESTION_API_KEY` configurada no Railway (variável de ambiente)
- Use essa mesma chave no comando acima

### Opção 2: Via API HTTP Direta

```powershell
$url = "https://web-production-42847.up.railway.app"
$apiKey = "sua-ingestion-api-key"

Invoke-WebRequest -Uri "$url/api/ingest" `
  -Method POST `
  -Headers @{"X-API-Key" = $apiKey} `
  -ContentType "application/json"
```

### Opção 3: Via Railway CLI

Se você tem Railway CLI configurado:

```powershell
railway run python backend/run_ingestion_dia.py dia1
railway run python backend/run_ingestion_dia.py dia2
```

---

## ⚠️ Importante: PDFs no Railway

Os PDFs precisam estar acessíveis no container do Railway. Opções:

### Opção A: PDFs no Git (Recomendado)

Se os PDFs estão commitados em `data/pdfs/`:
- Railway pode acessá-los durante o build
- Mas arquivos grandes podem não estar no Git

### Opção B: Via Volume no Railway

1. No Railway Dashboard, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume
3. Execute a ingestão

### Opção C: Via Railway CLI (Upload)

```powershell
railway run bash
# Dentro do container:
cd /app
# Os PDFs devem estar em data/pdfs/
python backend/run_ingestion_dia.py dia1
```

---

## 📊 Verificar Processamento

### Ver Logs no Railway:

1. Railway Dashboard → Serviço Backend → **Logs**
2. Você verá progresso como:
   ```
   Processando: data/pdfs/dia1/arquivo.pdf
   → X chunks criados
   ✓ Processado com sucesso
   ```

### Testar após Processar:

```powershell
$url = "https://web-production-42847.up.railway.app"
$body = @{
    question = "Quais palestras foram no Dia 1?"
    filters = $null
} | ConvertTo-Json

Invoke-WebRequest -Uri "$url/api/chat" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

---

## ✅ Checklist

- [ ] Qdrant Cloud configurado (`QDRANT_URL` e `QDRANT_API_KEY`)
- [ ] `OPENAI_API_KEY` configurada
- [ ] `INGESTION_API_KEY` configurada (para processar via API)
- [ ] PDFs acessíveis no Railway (Git ou Volume)
- [ ] Backend está rodando (health check OK)

---

**Execute o processamento e aguarde alguns minutos! 🚀**

