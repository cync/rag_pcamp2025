# ✅ Pronto para Processar PDFs!

## 🎉 Sucesso!

Os logs mostram que:
- ✅ Backend está rodando
- ✅ Qdrant Cloud está conectado
- ✅ Collection será criada automaticamente durante a ingestão

A mensagem "Collection 'product_camp_2025' não encontrada" é **NORMAL** - significa que você ainda não processou os PDFs.

---

## 🚀 Processar PDFs AGORA

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

### Opção A: PDFs no Git

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
   Ingestão concluída! Total de chunks: X
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

## ✅ Checklist Antes de Processar

- [x] Qdrant Cloud conectado ✅
- [x] Backend rodando ✅
- [ ] `INGESTION_API_KEY` configurada no Railway
- [ ] PDFs acessíveis no Railway (Git ou Volume)
- [ ] Pronto para executar ingestão

---

## 🎯 Próximo Passo

**Execute o processamento agora:**

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "sua-ingestion-api-key"
```

Ou configure `INGESTION_API_KEY` no Railway e execute via API!

---

**Tudo pronto! Processe os PDFs agora! 🚀**

