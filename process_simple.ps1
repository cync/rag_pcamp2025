$url = "https://pcamp2025.up.railway.app"
$apiKey = "fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB"

try {
    $response = Invoke-WebRequest -Uri "$url/api/ingest" -Method POST -Headers @{"X-API-Key" = $apiKey} -ContentType "application/json" -TimeoutSec 300
    Write-Host "SUCESSO! Status: $($response.StatusCode)"
    Write-Host "Resposta: $($response.Content)"
} catch {
    Write-Host "ERRO: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        Write-Host "Status Code: $($_.Exception.Response.StatusCode.value__)"
    }
}

