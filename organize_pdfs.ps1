# Script para organizar PDFs em Dia1 e Dia2
# Uso: .\organize_pdfs.ps1

$sourceDir = "C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001"
$dia1Dir = "data\pdfs\dia1"
$dia2Dir = "data\pdfs\dia2"

# Criar diretórios se não existirem
New-Item -ItemType Directory -Path $dia1Dir -Force | Out-Null
New-Item -ItemType Directory -Path $dia2Dir -Force | Out-Null

Write-Host "Organizando PDFs..."
Write-Host "Origem: $sourceDir"
Write-Host ""

# Listar todos os PDFs
$pdfs = Get-ChildItem -Path $sourceDir -Filter "*.pdf" -Recurse

Write-Host "Encontrados $($pdfs.Count) arquivos PDF"
Write-Host ""
Write-Host "Por favor, organize manualmente:"
Write-Host "1. PDFs do Dia 1 -> $dia1Dir"
Write-Host "2. PDFs do Dia 2 -> $dia2Dir"
Write-Host ""
Write-Host "Ou use o script interativo abaixo para copiar:"
Write-Host ""

# Listar PDFs encontrados
$pdfs | ForEach-Object {
    Write-Host "  - $($_.Name)"
}

Write-Host ""
Write-Host "Para copiar manualmente, use:"
Write-Host "Copy-Item 'caminho\arquivo.pdf' '$dia1Dir\'"
Write-Host "Copy-Item 'caminho\arquivo.pdf' '$dia2Dir\'"

