# Copiar todos os PDFs para um diretorio temporario primeiro
$sourceDir = (Get-ChildItem "C:\Users\Felipe\Downloads" | Where-Object { $_.Name -like "*Apresenta*Product*Camp*" -and $_.PSIsContainer }).FullName
$tempDir = "data\pdfs\temp"

Write-Host "Copiando todos os PDFs para diretorio temporario..." -ForegroundColor Cyan
Write-Host "Origem: $sourceDir"

New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

$pdfs = Get-ChildItem -Path $sourceDir -Filter "*.pdf" -Recurse
$pdfs | Copy-Item -Destination $tempDir -Force

Write-Host "Copiados $($pdfs.Count) PDFs para $tempDir" -ForegroundColor Green
Write-Host ""
Write-Host "Agora organize manualmente:" -ForegroundColor Yellow
Write-Host "  1. Abra o Explorer e va para: $tempDir"
Write-Host "  2. Copie os PDFs do Dia 1 para: data\pdfs\dia1\"
Write-Host "  3. Copie os PDFs do Dia 2 para: data\pdfs\dia2\"
Write-Host ""
Write-Host "Ou use os comandos PowerShell:" -ForegroundColor Cyan
Write-Host "  Get-ChildItem '$tempDir' | Where-Object { \$_.Name -like '*dia1*' } | Copy-Item -Destination 'data\pdfs\dia1\'"
Write-Host "  Get-ChildItem '$tempDir' | Where-Object { \$_.Name -like '*dia2*' } | Copy-Item -Destination 'data\pdfs\dia2\'"

