# 🚀 Processar PDFs AGORA

## ✅ Tudo Configurado!

- ✅ Qdrant Cloud conectado
- ✅ Backend rodando
- ✅ INGESTION_API_KEY configurada no Railway

---

## 🚀 Executar Processamento

### Opção 1: Via Script PowerShell (Recomendado)

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "zIm50kxry9lqtjsPWeJKhGQCoaDwfivF"
```

### Opção 2: Via API HTTP Direta

```powershell
$url = "https://web-production-42847.up.railway.app"
$apiKey = "zIm50kxry9lqtjsPWeJKhGQCoaDwfivF"

Write-Host "Processando PDFs..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "$url/api/ingest" `
        -Method POST `
        -Headers @{"X-API-Key" = $apiKey} `
        -ContentType "application/json" `
        -ErrorAction Stop
    
    Write-Host "✅ Processamento iniciado!" -ForegroundColor Green
    Write-Host "Resposta: $($response.Content)" -ForegroundColor White
    Write-Host ""
    Write-Host "Verifique os logs no Railway Dashboard para acompanhar o progresso." -ForegroundColor Yellow
} catch {
    Write-Host "❌ Erro: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $statusCode = $_.Exception.Response.StatusCode.value__
        Write-Host "Status Code: $statusCode" -ForegroundColor Yellow
    }
}
```

---

## ⚠️ Importante: PDFs no Railway

Os PDFs precisam estar acessíveis no container do Railway. Verifique:

### Opção A: PDFs no Git

Se os PDFs estão commitados em `data/pdfs/`:
- Railway pode acessá-los durante o build
- Verifique se estão no repositório Git

### Opção B: Via Volume no Railway

1. No Railway Dashboard, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume
3. Execute a ingestão

### Opção C: Via Railway CLI

```powershell
railway run python backend/run_ingestion_dia.py dia1
railway run python backend/run_ingestion_dia.py dia2
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

### O que Esperar:

- ✅ Processamento pode levar vários minutos (dependendo do número de PDFs)
- ✅ Você verá logs de cada PDF sendo processado
- ✅ Collection será criada automaticamente
- ✅ Chunks serão armazenados no Qdrant Cloud

---

## ✅ Testar Após Processar

Após o processamento completar, teste a API:

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

**Execute o processamento agora! 🚀**

