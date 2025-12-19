# Script para processar PDFs via API HTTP (com parâmetros)
# Uso: .\process_via_api_param.ps1 -RailwayUrl "https://seu-app.railway.app" -ApiKey "sua-chave"

param(
    [Parameter(Mandatory=$true)]
    [string]$RailwayUrl,
    
    [Parameter(Mandatory=$true)]
    [string]$ApiKey
)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processar PDFs via API HTTP" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "URL: $RailwayUrl" -ForegroundColor Gray
Write-Host "Processando via API..." -ForegroundColor Cyan
Write-Host ""

try {
    $response = Invoke-WebRequest -Uri "$RailwayUrl/api/ingest" `
        -Method POST `
        -Headers @{"X-API-Key" = $ApiKey} `
        -ContentType "application/json" `
        -ErrorAction Stop

    Write-Host "✅ Resposta recebida:" -ForegroundColor Green
    Write-Host $response.Content -ForegroundColor White
    
    if ($response.StatusCode -eq 200) {
        Write-Host ""
        Write-Host "✅ Processamento iniciado com sucesso!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Nota: O processamento pode levar alguns minutos." -ForegroundColor Yellow
        Write-Host "Verifique os logs no Railway Dashboard para acompanhar o progresso." -ForegroundColor Yellow
    }
} catch {
    Write-Host ""
    Write-Host "❌ Erro ao processar:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Resposta do servidor:" -ForegroundColor Yellow
        Write-Host $responseBody -ForegroundColor White
    }
    
    Write-Host ""
    Write-Host "Verifique:" -ForegroundColor Yellow
    Write-Host "  1. A URL do Railway esta correta?" -ForegroundColor White
    Write-Host "  2. A INGESTION_API_KEY esta configurada no Railway?" -ForegroundColor White
    Write-Host "  3. O backend esta rodando?" -ForegroundColor White
    Write-Host "  4. Os PDFs estao acessiveis no Railway?" -ForegroundColor White
}

Write-Host ""

