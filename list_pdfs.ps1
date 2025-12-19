# Script para listar PDFs e copiar manualmente
$sourceBase = "C:\Users\Felipe\Downloads"

Write-Host "Procurando diretorios com PDFs do Product Camp..."
Write-Host ""

$dirs = Get-ChildItem -Path $sourceBase -Directory -ErrorAction SilentlyContinue | Where-Object { 
    $_.Name -like "*Product*" -or $_.Name -like "*Camp*" -or $_.Name -like "*2025*"
}

if ($dirs) {
    Write-Host "Diretorios encontrados:" -ForegroundColor Green
    $i = 1
    foreach ($dir in $dirs) {
        $pdfCount = (Get-ChildItem -Path $dir.FullName -Filter "*.pdf" -Recurse -ErrorAction SilentlyContinue).Count
        Write-Host "  $i. $($dir.Name) ($pdfCount PDFs)" -ForegroundColor Cyan
        Write-Host "     $($dir.FullName)"
        $i++
    }
    Write-Host ""
    Write-Host "Para copiar os PDFs, use:" -ForegroundColor Yellow
    Write-Host "  Get-ChildItem 'CAMINHO_COMPLETO' -Filter '*.pdf' -Recurse | Copy-Item -Destination 'data\pdfs\dia1\'"
    Write-Host "  Get-ChildItem 'CAMINHO_COMPLETO' -Filter '*.pdf' -Recurse | Copy-Item -Destination 'data\pdfs\dia2\'"
} else {
    Write-Host "Nenhum diretorio encontrado. Verifique o caminho:" -ForegroundColor Yellow
    Write-Host "  $sourceBase"
}

