# Script para processar PDFs com retry automatico
param(
    [string]$ApiKey = "zIm50kxry9lqtjsPWeJKhGQCoaDwfivF",
    [int]$MaxRetries = 5,
    [int]$WaitSeconds = 30
)

$RailwayUrl = "https://web-production-42847.up.railway.app"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processar PDFs via API - Railway (com Retry)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "URL: $RailwayUrl" -ForegroundColor Gray
Write-Host "API Key: $($ApiKey.Substring(0, 10))..." -ForegroundColor Gray
Write-Host ""

# Funcao para testar health check
function Test-BackendHealth {
    param([string]$Url)
    try {
        $response = Invoke-WebRequest -Uri "$Url/api/health" -Method GET -TimeoutSec 10 -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

# Funcao para processar PDFs
function Process-PDFs {
    param([string]$Url, [string]$Key)
    try {
        $response = Invoke-WebRequest -Uri "$Url/api/ingest" `
            -Method POST `
            -Headers @{"X-API-Key" = $Key} `
            -ContentType "application/json" `
            -TimeoutSec 300 `
            -ErrorAction Stop
        
        return @{
            Success = $true
            Message = $response.Content
            StatusCode = $response.StatusCode
        }
    } catch {
        $statusCode = 0
        if ($_.Exception.Response) {
            $statusCode = $_.Exception.Response.StatusCode.value__
        }
        return @{
            Success = $false
            Message = $_.Exception.Message
            StatusCode = $statusCode
        }
    }
}

# Tentar verificar backend
Write-Host "1. Verificando backend..." -ForegroundColor Yellow
$backendReady = $false

for ($i = 1; $i -le $MaxRetries; $i++) {
    Write-Host "   Tentativa $i/$MaxRetries..." -ForegroundColor Gray
    
    if (Test-BackendHealth -Url $RailwayUrl) {
        Write-Host "   Backend esta respondendo!" -ForegroundColor Green
        $backendReady = $true
        break
    } else {
        Write-Host "   Backend ainda nao esta pronto..." -ForegroundColor Yellow
        if ($i -lt $MaxRetries) {
            Write-Host "   Aguardando $WaitSeconds segundos antes de tentar novamente..." -ForegroundColor Gray
            Start-Sleep -Seconds $WaitSeconds
        }
    }
}

if (-not $backendReady) {
    Write-Host ""
    Write-Host "Backend nao esta respondendo apos $MaxRetries tentativas." -ForegroundColor Red
    Write-Host ""
    Write-Host "Verifique no Railway Dashboard:" -ForegroundColor Yellow
    Write-Host "  1. O servico backend esta 'Deployed' (verde)?" -ForegroundColor White
    Write-Host "  2. Os logs mostram 'Application startup complete'?" -ForegroundColor White
    Write-Host "  3. Ha erros nos logs?" -ForegroundColor White
    Write-Host ""
    Write-Host "Aguarde alguns minutos e execute novamente:" -ForegroundColor Cyan
    Write-Host "  .\process_with_retry.ps1" -ForegroundColor Gray
    exit 1
}

Write-Host ""

# Processar PDFs
Write-Host "2. Processando PDFs..." -ForegroundColor Yellow
$result = Process-PDFs -Url $RailwayUrl -Key $ApiKey

if ($result.Success) {
    Write-Host "   Processamento iniciado com sucesso!" -ForegroundColor Green
    Write-Host "   Resposta: $($result.Message)" -ForegroundColor White
    Write-Host "   Status Code: $($result.StatusCode)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   O processamento pode levar varios minutos." -ForegroundColor Yellow
    Write-Host "   Verifique os logs no Railway Dashboard para acompanhar:" -ForegroundColor Yellow
    Write-Host "      Railway Dashboard -> Backend -> Logs" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   Voce vera logs como:" -ForegroundColor Cyan
    Write-Host "      Processando: data/pdfs/dia1/arquivo.pdf" -ForegroundColor Gray
    Write-Host "      -> X chunks criados" -ForegroundColor Gray
    Write-Host "      Processado com sucesso" -ForegroundColor Gray
} else {
    Write-Host "   Erro ao processar:" -ForegroundColor Red
    Write-Host "   $($result.Message)" -ForegroundColor Red
    
    if ($result.StatusCode -eq 403) {
        Write-Host ""
        Write-Host "   A API Key esta incorreta ou nao esta configurada." -ForegroundColor Yellow
        Write-Host "   Verifique se INGESTION_API_KEY esta configurada no Railway." -ForegroundColor White
    } elseif ($result.StatusCode -eq 500) {
        Write-Host ""
        Write-Host "   Erro interno do servidor." -ForegroundColor Yellow
        Write-Host "   Verifique os logs no Railway Dashboard." -ForegroundColor White
    } elseif ($result.StatusCode -eq 0) {
        Write-Host ""
        Write-Host "   Nao foi possivel conectar ao servidor." -ForegroundColor Yellow
        Write-Host "   Verifique se o backend esta rodando." -ForegroundColor White
    }
}

Write-Host ""
