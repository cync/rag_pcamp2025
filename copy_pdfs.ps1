# Script interativo para copiar PDFs organizados por dia
# Uso: .\copy_pdfs.ps1

$sourceDir = "C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001"
$dia1Dir = "data\pdfs\dia1"
$dia2Dir = "data\pdfs\dia2"

# Verificar se diretório origem existe
if (-not (Test-Path $sourceDir)) {
    Write-Host "ERRO: Diretório origem não encontrado: $sourceDir" -ForegroundColor Red
    exit 1
}

# Criar diretórios destino
New-Item -ItemType Directory -Path $dia1Dir -Force | Out-Null
New-Item -ItemType Directory -Path $dia2Dir -Force | Out-Null

Write-Host "=" * 60
Write-Host "Organizador de PDFs - Product Camp 2025"
Write-Host "=" * 60
Write-Host ""
Write-Host "Origem: $sourceDir"
Write-Host "Dia 1:  $dia1Dir"
Write-Host "Dia 2:  $dia2Dir"
Write-Host ""

# Listar todos os PDFs
$pdfs = Get-ChildItem -Path $sourceDir -Filter "*.pdf" -Recurse

if ($pdfs.Count -eq 0) {
    Write-Host "Nenhum PDF encontrado no diretório origem!" -ForegroundColor Yellow
    exit 0
}

Write-Host "Encontrados $($pdfs.Count) arquivos PDF"
Write-Host ""
Write-Host "Por favor, organize os PDFs:"
Write-Host ""

# Listar PDFs e perguntar para cada um
$dia1Count = 0
$dia2Count = 0

foreach ($pdf in $pdfs) {
    Write-Host "Arquivo: $($pdf.Name)" -ForegroundColor Cyan
    $choice = Read-Host "Copiar para (1=Dia1, 2=Dia2, p=Pular, a=Abortar)"
    
    switch ($choice.ToLower()) {
        "1" {
            Copy-Item $pdf.FullName -Destination $dia1Dir -Force
            Write-Host "  ✓ Copiado para Dia 1" -ForegroundColor Green
            $dia1Count++
        }
        "2" {
            Copy-Item $pdf.FullName -Destination $dia2Dir -Force
            Write-Host "  ✓ Copiado para Dia 2" -ForegroundColor Green
            $dia2Count++
        }
        "p" {
            Write-Host "  ⊘ Pulado" -ForegroundColor Yellow
        }
        "a" {
            Write-Host "Operação abortada pelo usuário" -ForegroundColor Red
            exit 0
        }
        default {
            Write-Host "  ⊘ Opção inválida, pulando..." -ForegroundColor Yellow
        }
    }
    Write-Host ""
}

Write-Host "=" * 60
Write-Host "Resumo:"
Write-Host "  Dia 1: $dia1Count arquivos"
Write-Host "  Dia 2: $dia2Count arquivos"
Write-Host "=" * 60
Write-Host ""
Write-Host "Próximo passo: Processar os PDFs"
Write-Host "  python backend/process_pdfs.py dia1"
Write-Host "  python backend/process_pdfs.py dia2"

