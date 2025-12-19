# Script para reorganizar PDFs: Dia 1 = 4 PDFs, Dia 2 = 6 PDFs
# Uso: .\reorganize_pdfs_param.ps1 "1,2,3,4"
# Ou: .\reorganize_pdfs_param.ps1  # Usa primeiros 4 por padrão

param(
    [string]$Dia1Numbers = "1,2,3,4"
)

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
    Write-Host "Copiando PDFs do diretorio origem..." -ForegroundColor Yellow
    $sourceDir = (Get-ChildItem "C:\Users\Felipe\Downloads" | Where-Object { $_.Name -like "*Apresenta*Product*Camp*" -and $_.PSIsContainer }).FullName
    if ($sourceDir) {
        New-Item -ItemType Directory -Path "data\pdfs\temp" -Force | Out-Null
        Get-ChildItem -Path $sourceDir -Filter "*.pdf" -Recurse | Copy-Item -Destination "data\pdfs\temp\" -Force
        $allPdfs = Get-ChildItem "data\pdfs\temp" -Filter "*.pdf"
    } else {
        Write-Host "ERRO: Nao foi possivel encontrar os PDFs!" -ForegroundColor Red
        exit 1
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
Write-Host "Usando configuracao: Dia 1 = PDFs $Dia1Numbers" -ForegroundColor Yellow
Write-Host ""

$selectedNumbers = $Dia1Numbers -split "," | ForEach-Object { [int]($_.Trim()) }

if ($selectedNumbers.Count -ne 4) {
    Write-Host "ERRO: Deve selecionar exatamente 4 PDFs!" -ForegroundColor Red
    Write-Host "Uso: .\reorganize_pdfs_param.ps1 '1,2,3,4'" -ForegroundColor Yellow
    exit 1
}

$dia1Count = 0
$dia2Count = 0

$i = 1
foreach ($pdf in $allPdfs) {
    if ($selectedNumbers -contains $i) {
        Copy-Item $pdf.FullName -Destination "data\pdfs\dia1\" -Force
        Write-Host "[$i] Dia 1: $($pdf.Name)" -ForegroundColor Green
        $dia1Count++
    } else {
        Copy-Item $pdf.FullName -Destination "data\pdfs\dia2\" -Force
        Write-Host "[$i] Dia 2: $($pdf.Name)" -ForegroundColor Cyan
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

