# Script para Processar PDFs em Produção no Railway
# Executa automaticamente se estiver logado e linkado

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processar PDFs em Producao - Railway" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se está logado
Write-Host "Verificando login no Railway..." -ForegroundColor Yellow
$whoami = railway whoami 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Nao esta logado no Railway!" -ForegroundColor Red
    Write-Host ""
    Write-Host "INSTRUCOES:" -ForegroundColor Yellow
    Write-Host "  1. Execute: railway login" -ForegroundColor White
    Write-Host "  2. Execute: railway link" -ForegroundColor White
    Write-Host "  3. Execute este script novamente: .\process_production_auto.ps1" -ForegroundColor White
    Write-Host ""
    exit 1
}
Write-Host "✅ Logado como: $whoami" -ForegroundColor Green
Write-Host ""

# Verificar se está linkado
Write-Host "Verificando projeto linkado..." -ForegroundColor Yellow
$status = railway status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Nenhum projeto linkado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "INSTRUCOES:" -ForegroundColor Yellow
    Write-Host "  1. Execute: railway link" -ForegroundColor White
    Write-Host "  2. Selecione o projeto do Product Camp 2025" -ForegroundColor White
    Write-Host "  3. Execute este script novamente: .\process_production_auto.ps1" -ForegroundColor White
    Write-Host ""
    exit 1
}
Write-Host "✅ Projeto linkado!" -ForegroundColor Green
Write-Host ""

# Processar Dia 1
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processando Dia 1 (4 PDFs)..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
railway run python backend/run_ingestion_dia.py dia1

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Dia 1 processado com sucesso!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Erro ao processar Dia 1" -ForegroundColor Red
    Write-Host "Verifique os logs com: railway logs" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Aguardando 5 segundos antes de processar Dia 2..." -ForegroundColor Gray
Start-Sleep -Seconds 5
Write-Host ""

# Processar Dia 2
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processando Dia 2 (6 PDFs)..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
railway run python backend/run_ingestion_dia.py dia2

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Dia 2 processado com sucesso!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Erro ao processar Dia 2" -ForegroundColor Red
    Write-Host "Verifique os logs com: railway logs" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Processamento concluido!" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para ver os logs completos:" -ForegroundColor Yellow
Write-Host "  railway logs" -ForegroundColor White
Write-Host ""
Write-Host "Para testar a API:" -ForegroundColor Yellow
Write-Host "  Veja a URL do seu app no Railway Dashboard" -ForegroundColor White
Write-Host ""

