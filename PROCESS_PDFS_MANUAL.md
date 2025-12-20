# 🚀 Processar PDFs Manualmente

## 📋 Comandos para Executar

### Opção 1: PowerShell (Recomendado)

Abra um **novo terminal PowerShell** e execute:

```powershell
$url = "https://pcamp2025.up.railway.app"
$apiKey = "fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB"

Invoke-WebRequest -Uri "$url/api/ingest" `
  -Method POST `
  -Headers @{"X-API-Key" = $apiKey} `
  -ContentType "application/json"
```

### Opção 2: Usando curl (se disponível)

```bash
curl -X POST https://pcamp2025.up.railway.app/api/ingest \
  -H "X-API-Key: fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB" \
  -H "Content-Type: application/json"
```

### Opção 3: Via Navegador (usando extensão)

Use uma extensão como **Postman** ou **Thunder Client** no VS Code:

- **URL**: `https://pcamp2025.up.railway.app/api/ingest`
- **Method**: `POST`
- **Headers**:
  - `X-API-Key`: `fOj0k7thk2AxcSMVW1YMW6MsiRCD5YuB`
  - `Content-Type`: `application/json`

---

## ✅ Resposta Esperada

Se funcionar, você verá:

```json
{
  "status": "success",
  "message": "Ingestion completed successfully"
}
```

---

## 📊 Verificar Processamento

### No Railway Dashboard:

1. Acesse: https://railway.app
2. Abra seu projeto → Serviço Backend
3. Vá em **Logs**
4. Você verá o progresso:
   ```
   Processando: data/pdfs/dia1/arquivo.pdf
   → X chunks criados
   ✓ Processado com sucesso
   Ingestão concluída! Total de chunks: X
   ```

---

## ⚠️ Se Retornar Erro

### Erro 502:
- Backend ainda não está respondendo
- Aguarde mais alguns minutos após o deploy
- Verifique os logs no Railway Dashboard

### Erro 403:
- API Key incorreta
- Verifique se `INGESTION_API_KEY` está configurada no Railway

### Erro 500:
- Erro interno do servidor
- Verifique os logs no Railway Dashboard para detalhes

---

**Execute os comandos acima em um novo terminal PowerShell! 🚀**

