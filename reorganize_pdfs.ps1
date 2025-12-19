# Script para reorganizar PDFs: Dia 1 = 4 PDFs, Dia 2 = 6 PDFs

Write-Host "============================================================"
Write-Host "Reorganizar PDFs - Product Camp 2025"
Write-Host "Dia 1: 4 PDFs | Dia 2: 6 PDFs"
Write-Host "============================================================"
Write-Host ""

# Limpar diretórios
Remove-Item "data\pdfs\dia1\*" -Filter "*.pdf" -Force -ErrorAction SilentlyContinue
Remove-Item "data\pdfs\dia2\*" -Filter "*.pdf" -Force -ErrorAction SilentlyContinue

# Listar todos os PDFs disponíveis
$allPdfs = Get-ChildItem "data\pdfs\temp" -Filter "*.pdf" -ErrorAction SilentlyContinue

if ($null -eq $allPdfs -or $allPdfs.Count -eq 0) {
    Write-Host "Nenhum PDF encontrado em data\pdfs\temp" -ForegroundColor Red
    Write-Host "Copiando do diretorio origem..." -ForegroundColor Yellow
    
    $sourceDir = (Get-ChildItem "C:\Users\Felipe\Downloads" | Where-Object { $_.Name -like "*Apresenta*Product*Camp*" -and $_.PSIsContainer }).FullName
    if ($sourceDir) {
        New-Item -ItemType Directory -Path "data\pdfs\temp" -Force | Out-Null
        Get-ChildItem -Path $sourceDir -Filter "*.pdf" -Recurse | Copy-Item -Destination "data\pdfs\temp\" -Force
        $allPdfs = Get-ChildItem "data\pdfs\temp" -Filter "*.pdf"
    }
}

Write-Host "PDFs disponiveis ($($allPdfs.Count)):" -ForegroundColor Cyan
Write-Host ""
$i = 1
foreach ($pdf in $allPdfs) {
    Write-Host "$i. $($pdf.Name)" -ForegroundColor White
    $i++
}

Write-Host ""
Write-Host "============================================================"
Write-Host "INSTRUCOES:" -ForegroundColor Yellow
Write-Host "1. Selecione 4 PDFs para DIA 1 (digite os numeros separados por virgula)"
Write-Host "2. Os 6 restantes vao automaticamente para DIA 2"
Write-Host "============================================================"
Write-Host ""

$dia1Numbers = Read-Host "Digite os numeros dos 4 PDFs para DIA 1 (ex: 1,2,3,4)"

$selectedNumbers = $dia1Numbers -split "," | ForEach-Object { [int]($_.Trim()) }

if ($selectedNumbers.Count -ne 4) {
    Write-Host "ERRO: Voce deve selecionar exatamente 4 PDFs!" -ForegroundColor Red
    exit 1
}

$dia1Count = 0
$dia2Count = 0

$i = 1
foreach ($pdf in $allPdfs) {
    if ($selectedNumbers -contains $i) {
        Copy-Item $pdf.FullName -Destination "data\pdfs\dia1\" -Force
        Write-Host "  Dia 1: $($pdf.Name)" -ForegroundColor Green
        $dia1Count++
    } else {
        Copy-Item $pdf.FullName -Destination "data\pdfs\dia2\" -Force
        Write-Host "  Dia 2: $($pdf.Name)" -ForegroundColor Cyan
        $dia2Count++
    }
    $i++
}

Write-Host ""
Write-Host "============================================================"
Write-Host "Reorganizacao concluida!" -ForegroundColor Green
Write-Host "  Dia 1: $dia1Count PDFs" -ForegroundColor Green
Write-Host "  Dia 2: $dia2Count PDFs" -ForegroundColor Cyan
Write-Host "============================================================"

