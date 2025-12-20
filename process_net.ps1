$url = "https://pcamp2025.up.railway.app/api/ingest"
$apiKey = "fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB"

try {
    $request = [System.Net.HttpWebRequest]::Create($url)
    $request.Method = "POST"
    $request.ContentType = "application/json"
    $request.Headers.Add("X-API-Key", $apiKey)
    $request.Timeout = 300000
    
    $response = $request.GetResponse()
    $reader = New-Object System.IO.StreamReader($response.GetResponseStream())
    $content = $reader.ReadToEnd()
    
    Write-Host "SUCESSO! Status: $($response.StatusCode)"
    Write-Host "Resposta: $content"
    
    $reader.Close()
    $response.Close()
} catch {
    Write-Host "ERRO: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        $statusCode = [int]$_.Exception.Response.StatusCode
        Write-Host "Status Code: $statusCode"
    }
}

