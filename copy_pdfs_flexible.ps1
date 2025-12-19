# Script flexível para copiar PDFs organizados por dia
# Uso: .\copy_pdfs_flexible.ps1 [caminho_origem]

param(
    [string]$SourceDir = ""
)

$dia1Dir = "data\pdfs\dia1"
$dia2Dir = "data\pdfs\dia2"

# Criar diretórios destino
New-Item -ItemType Directory -Path $dia1Dir -Force | Out-Null
New-Item -ItemType Directory -Path $dia2Dir -Force | Out-Null

Write-Host "=" * 60
Write-Host "Organizador de PDFs - Product Camp 2025"
Write-Host "=" * 60
Write-Host ""

# Se não forneceu caminho, perguntar
if ([string]::IsNullOrEmpty($SourceDir)) {
    Write-Host "Por favor, informe o caminho do diretório com os PDFs:"
    Write-Host "Exemplo: C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001"
    Write-Host ""
    $SourceDir = Read-Host "Caminho"
}

# Verificar se diretório origem existe
if (-not (Test-Path $SourceDir)) {
    Write-Host ""
    Write-Host "ERRO: Diretório não encontrado: $SourceDir" -ForegroundColor Red
    Write-Host ""
    Write-Host "Tentando encontrar automaticamente..." -ForegroundColor Yellow
    
    # Tentar encontrar no Downloads
    $possiblePaths = @(
        "C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001",
        "C:\Users\Felipe\Downloads\*Product*Camp*",
        "C:\Users\Felipe\Downloads"
    )
    
    foreach ($path in $possiblePaths) {
        $found = Get-ChildItem -Path $path -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "*Product*" -or $_.PSIsContainer }
        if ($found) {
            Write-Host "Encontrado: $($found.FullName)" -ForegroundColor Green
            $SourceDir = $found.FullName
            break
        }
    }
    
    if (-not (Test-Path $SourceDir)) {
        Write-Host "Não foi possível encontrar o diretório automaticamente." -ForegroundColor Red
        Write-Host "Por favor, execute o script novamente fornecendo o caminho correto:" -ForegroundColor Yellow
        Write-Host "  .\copy_pdfs_flexible.ps1 'C:\caminho\completo\para\pdfs'" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "Origem: $SourceDir" -ForegroundColor Cyan
Write-Host "Dia 1:  $dia1Dir" -ForegroundColor Cyan
Write-Host "Dia 2:  $dia2Dir" -ForegroundColor Cyan
Write-Host ""

# Listar todos os PDFs (recursivo)
$pdfs = Get-ChildItem -Path $SourceDir -Filter "*.pdf" -Recurse -ErrorAction SilentlyContinue

if ($null -eq $pdfs -or $pdfs.Count -eq 0) {
    Write-Host "Nenhum PDF encontrado no diretório!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Verifique se:"
    Write-Host "  1. O caminho está correto"
    Write-Host "  2. Existem arquivos .pdf no diretório"
    exit 0
}

Write-Host "Encontrados $($pdfs.Count) arquivos PDF" -ForegroundColor Green
Write-Host ""
Write-Host "Organize os PDFs:"
Write-Host "  1 = Copiar para Dia 1"
Write-Host "  2 = Copiar para Dia 2"
Write-Host "  p = Pular este arquivo"
Write-Host "  a = Abortar e sair"
Write-Host "  t = Copiar todos restantes para Dia 1"
Write-Host "  u = Copiar todos restantes para Dia 2"
Write-Host ""

$dia1Count = 0
$dia2Count = 0
$skippedCount = 0
$copyAllTo = $null

foreach ($pdf in $pdfs) {
    if ($copyAllTo) {
        # Modo copiar todos
        $destDir = if ($copyAllTo -eq "1") { $dia1Dir } else { $dia2Dir }
        Copy-Item $pdf.FullName -Destination $destDir -Force
        if ($copyAllTo -eq "1") { $dia1Count++ } else { $dia2Count++ }
        Write-Host "  ✓ $($pdf.Name) -> $destDir" -ForegroundColor Green
        continue
    }
    
    Write-Host "Arquivo: $($pdf.Name)" -ForegroundColor Cyan
    Write-Host "  1 = Dia 1, 2 = Dia 2, p = Pular, a = Abortar, t = Todos Dia1, u = Todos Dia2"
    $choice = Read-Host "Escolha"
    
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
            $skippedCount++
        }
        "t" {
            Copy-Item $pdf.FullName -Destination $dia1Dir -Force
            Write-Host "  ✓ Copiado para Dia 1 (modo copiar todos)" -ForegroundColor Green
            $dia1Count++
            $copyAllTo = "1"
        }
        "u" {
            Copy-Item $pdf.FullName -Destination $dia2Dir -Force
            Write-Host "  ✓ Copiado para Dia 2 (modo copiar todos)" -ForegroundColor Green
            $dia2Count++
            $copyAllTo = "2"
        }
        "a" {
            Write-Host "Operacao abortada pelo usuario" -ForegroundColor Red
            exit 0
        }
        default {
            Write-Host "  ⊘ Opção inválida, pulando..." -ForegroundColor Yellow
            $skippedCount++
        }
    }
    Write-Host ""
}

Write-Host ("=" * 60)
Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "  Dia 1: $dia1Count arquivos" -ForegroundColor Green
Write-Host "  Dia 2: $dia2Count arquivos" -ForegroundColor Green
Write-Host "  Pulados: $skippedCount arquivos" -ForegroundColor Yellow
Write-Host "=" * 60
Write-Host ""
Write-Host "Próximo passo: Processar os PDFs" -ForegroundColor Cyan
Write-Host "  cd backend"
Write-Host "  python process_pdfs.py dia1"
Write-Host "  python process_pdfs.py dia2"
Write-Host ""

