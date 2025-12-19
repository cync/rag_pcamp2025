# 🚀 Executar Processamento AGORA

## ⚡ Opção 1: Via Railway CLI (Recomendado)

### Passo a Passo:

1. **Abra um terminal PowerShell** (novo terminal, não este)

2. **Login no Railway:**
   ```powershell
   railway login
   ```
   - Isso abrirá o navegador para autenticação
   - Faça login com sua conta Railway

3. **Link ao projeto:**
   ```powershell
   railway link
   ```
   - Selecione o projeto do Product Camp 2025

4. **Executar processamento:**
   ```powershell
   .\process_production_auto.ps1
   ```

   Ou manualmente:
   ```powershell
   railway run python backend/run_ingestion_dia.py dia1
   railway run python backend/run_ingestion_dia.py dia2
   ```

---

## 🌐 Opção 2: Via Endpoint de Ingestão (Se configurado)

Se você configurou `INGESTION_API_KEY` no Railway:

1. **Obtenha a URL do seu app no Railway Dashboard**
   - Vá em: Railway Dashboard → Seu Projeto → Backend Service
   - Copie a URL pública (ex: `https://seu-app.railway.app`)

2. **Execute:**
   ```powershell
   $apiKey = "sua-chave-secreta"  # A mesma configurada no Railway
   $railwayUrl = "https://seu-app.railway.app"
   
   Invoke-WebRequest -Uri "$railwayUrl/api/ingest" `
     -Method POST `
     -Headers @{"X-API-Key" = $apiKey}
   ```

**Nota**: Para isso funcionar, os PDFs precisam estar no container do Railway.

---

## 📋 Checklist Antes de Executar

- [ ] Railway CLI instalado (`railway --version`)
- [ ] Login feito (`railway login`)
- [ ] Projeto linkado (`railway link`)
- [ ] Variáveis de ambiente configuradas no Railway:
  - [ ] `OPENAI_API_KEY`
  - [ ] `QDRANT_HOST`
  - [ ] `QDRANT_PORT`
  - [ ] `QDRANT_COLLECTION_NAME`
- [ ] PDFs acessíveis no Railway (via Git ou Volume)

---

## 🔍 Verificar Logs

Durante o processamento:
```powershell
railway logs
```

Ou no Railway Dashboard → **Deployments** → **Logs**

---

## ✅ Testar Após Processar

```powershell
$url = "https://seu-app.railway.app"
$body = @{
    question = "Quais palestras foram no Dia 1?"
    filters = $null
} | ConvertTo-Json

Invoke-WebRequest -Uri "$url/api/chat" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

---

**Execute os comandos acima no seu terminal PowerShell! 🚀**

