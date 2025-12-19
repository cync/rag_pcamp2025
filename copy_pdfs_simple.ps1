# Script simples para copiar PDFs organizados por dia
param([string]$SourceDir = "")

$dia1Dir = "data\pdfs\dia1"
$dia2Dir = "data\pdfs\dia2"

New-Item -ItemType Directory -Path $dia1Dir -Force | Out-Null
New-Item -ItemType Directory -Path $dia2Dir -Force | Out-Null

Write-Host "============================================================"
Write-Host "Organizador de PDFs - Product Camp 2025"
Write-Host "============================================================"
Write-Host ""

if ([string]::IsNullOrEmpty($SourceDir)) {
    Write-Host "Informe o caminho do diretorio com os PDFs:"
    Write-Host "Exemplo: C:\Users\Felipe\Downloads\Apresentacoes Product Camp-20251219T151033Z-3-001"
    Write-Host ""
    $SourceDir = Read-Host "Caminho"
}

if (-not (Test-Path $SourceDir)) {
    Write-Host ""
    Write-Host "ERRO: Diretorio nao encontrado: $SourceDir" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, execute novamente com o caminho correto:"
    Write-Host "  .\copy_pdfs_simple.ps1 'C:\caminho\completo\para\pdfs'"
    exit 1
}

Write-Host "Origem: $SourceDir" -ForegroundColor Cyan
Write-Host "Dia 1:  $dia1Dir" -ForegroundColor Cyan
Write-Host "Dia 2:  $dia2Dir" -ForegroundColor Cyan
Write-Host ""

$pdfs = Get-ChildItem -Path $SourceDir -Filter "*.pdf" -Recurse -ErrorAction SilentlyContinue

if ($null -eq $pdfs -or $pdfs.Count -eq 0) {
    Write-Host "Nenhum PDF encontrado!" -ForegroundColor Yellow
    exit 0
}

Write-Host "Encontrados $($pdfs.Count) arquivos PDF" -ForegroundColor Green
Write-Host ""
Write-Host "Opcoes:"
Write-Host "  1 = Copiar para Dia 1"
Write-Host "  2 = Copiar para Dia 2"
Write-Host "  p = Pular"
Write-Host "  a = Abortar"
Write-Host ""

$dia1Count = 0
$dia2Count = 0
$skippedCount = 0

foreach ($pdf in $pdfs) {
    Write-Host "Arquivo: $($pdf.Name)" -ForegroundColor Cyan
    $choice = Read-Host "Escolha"
    
    if ($choice -eq "1") {
        Copy-Item $pdf.FullName -Destination $dia1Dir -Force
        Write-Host "  OK - Copiado para Dia 1" -ForegroundColor Green
        $dia1Count++
    }
    elseif ($choice -eq "2") {
        Copy-Item $pdf.FullName -Destination $dia2Dir -Force
        Write-Host "  OK - Copiado para Dia 2" -ForegroundColor Green
        $dia2Count++
    }
    elseif ($choice -eq "p") {
        Write-Host "  Pulado" -ForegroundColor Yellow
        $skippedCount++
    }
    elseif ($choice -eq "a") {
        Write-Host "Abortado" -ForegroundColor Red
        exit 0
    }
    else {
        Write-Host "  Opcao invalida, pulando..." -ForegroundColor Yellow
        $skippedCount++
    }
    Write-Host ""
}

Write-Host "============================================================"
Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "  Dia 1: $dia1Count arquivos" -ForegroundColor Green
Write-Host "  Dia 2: $dia2Count arquivos" -ForegroundColor Green
Write-Host "  Pulados: $skippedCount arquivos" -ForegroundColor Yellow
Write-Host "============================================================"
Write-Host ""
Write-Host "Proximo passo: Processar os PDFs" -ForegroundColor Cyan
Write-Host "  cd backend"
Write-Host "  python process_pdfs.py dia1"
Write-Host "  python process_pdfs.py dia2"

