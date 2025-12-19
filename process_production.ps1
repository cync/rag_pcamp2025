# Script para processar PDFs em produção no Railway
# Execute após fazer: railway login e railway link

Write-Host "============================================================"
Write-Host "Processar PDFs em Producao - Railway"
Write-Host "============================================================"
Write-Host ""

# Verificar se está logado
Write-Host "Verificando login no Railway..." -ForegroundColor Cyan
$whoami = railway whoami 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERRO: Nao esta logado no Railway!" -ForegroundColor Red
    Write-Host "Execute primeiro: railway login" -ForegroundColor Yellow
    exit 1
}
Write-Host "Logado como: $whoami" -ForegroundColor Green
Write-Host ""

# Verificar se está linkado
Write-Host "Verificando projeto linkado..." -ForegroundColor Cyan
$status = railway status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERRO: Nenhum projeto linkado!" -ForegroundColor Red
    Write-Host "Execute primeiro: railway link" -ForegroundColor Yellow
    exit 1
}
Write-Host "Projeto linkado!" -ForegroundColor Green
Write-Host ""

# Processar Dia 1
Write-Host "============================================================"
Write-Host "Processando Dia 1..." -ForegroundColor Cyan
Write-Host "============================================================"
railway run python backend/run_ingestion_dia.py dia1

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dia 1 processado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "✗ Erro ao processar Dia 1" -ForegroundColor Red
}

Write-Host ""

# Processar Dia 2
Write-Host "============================================================"
Write-Host "Processando Dia 2..." -ForegroundColor Cyan
Write-Host "============================================================"
railway run python backend/run_ingestion_dia.py dia2

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dia 2 processado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "✗ Erro ao processar Dia 2" -ForegroundColor Red
}

Write-Host ""
Write-Host "============================================================"
Write-Host "Processamento concluido!" -ForegroundColor Cyan
Write-Host "============================================================"

