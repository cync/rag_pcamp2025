# Script para processar PDFs com a URL do Railway
# Uso: .\PROCESS_WITH_URL.ps1 -ApiKey "sua-chave" (opcional)

param(
    [string]$ApiKey = "fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB"
)

$RailwayUrl = "https://pcamp2025.up.railway.app"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processar PDFs via API - Railway" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "URL: $RailwayUrl" -ForegroundColor Gray
Write-Host ""

# Testar health check primeiro
Write-Host "1. Testando conexao com backend..." -ForegroundColor Yellow
try {
    $healthResponse = Invoke-WebRequest -Uri "$RailwayUrl/api/health" -Method GET -ErrorAction Stop
    Write-Host "   ✅ Backend esta rodando!" -ForegroundColor Green
    Write-Host "   Resposta: $($healthResponse.Content)" -ForegroundColor White
} catch {
    Write-Host "   ❌ Backend nao esta respondendo!" -ForegroundColor Red
    Write-Host "   Erro: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "   Verifique no Railway Dashboard:" -ForegroundColor Yellow
    Write-Host "   1. O servico backend esta rodando?" -ForegroundColor White
    Write-Host "   2. As variaveis de ambiente estao configuradas?" -ForegroundColor White
    Write-Host "   3. O Qdrant esta conectado?" -ForegroundColor White
    Write-Host "   4. Veja os logs no Railway Dashboard" -ForegroundColor White
    exit 1
}

Write-Host ""

# Se ApiKey foi fornecida, tentar processar
if ($ApiKey) {
    Write-Host "2. Tentando processar PDFs..." -ForegroundColor Yellow
    try {
        $response = Invoke-WebRequest -Uri "$RailwayUrl/api/ingest" `
            -Method POST `
            -Headers @{"X-API-Key" = $ApiKey} `
            -ContentType "application/json" `
            -ErrorAction Stop

        Write-Host "   ✅ Processamento iniciado!" -ForegroundColor Green
        Write-Host "   Resposta: $($response.Content)" -ForegroundColor White
        Write-Host ""
        Write-Host "   Nota: O processamento pode levar varios minutos." -ForegroundColor Yellow
        Write-Host "   Verifique os logs no Railway Dashboard para acompanhar." -ForegroundColor Yellow
    } catch {
        Write-Host "   ❌ Erro ao processar:" -ForegroundColor Red
        Write-Host "   $($_.Exception.Message)" -ForegroundColor Red
        
        if ($_.Exception.Response) {
            $statusCode = $_.Exception.Response.StatusCode.value__
            Write-Host "   Status Code: $statusCode" -ForegroundColor Yellow
            
            if ($statusCode -eq 403) {
                Write-Host ""
                Write-Host "   A API Key esta incorreta ou nao esta configurada." -ForegroundColor Yellow
                Write-Host "   Configure INGESTION_API_KEY no Railway Dashboard:" -ForegroundColor White
                Write-Host "   1. Vá em Variables" -ForegroundColor Gray
                Write-Host "   2. Adicione: INGESTION_API_KEY = sua-chave-secreta" -ForegroundColor Gray
                Write-Host "   3. Execute novamente com: .\PROCESS_WITH_URL.ps1 -ApiKey 'sua-chave'" -ForegroundColor Gray
            } elseif ($statusCode -eq 500) {
                Write-Host ""
                Write-Host "   Erro interno do servidor." -ForegroundColor Yellow
                Write-Host "   Verifique os logs no Railway Dashboard." -ForegroundColor White
            }
        }
    }
} else {
    Write-Host "2. Para processar, execute com a API Key:" -ForegroundColor Yellow
    Write-Host "   .\PROCESS_WITH_URL.ps1 -ApiKey 'sua-chave-secreta'" -ForegroundColor White
    Write-Host ""
    Write-Host "   A API Key deve ser a mesma configurada em INGESTION_API_KEY no Railway." -ForegroundColor Gray
}

Write-Host ""

