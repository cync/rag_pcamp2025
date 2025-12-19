# ⚡ Processar em Produção - Guia Rápido

## 🚀 Execução Rápida

### 1. Login e Link (Primeira vez)

Abra PowerShell e execute:

```powershell
railway login
railway link
```

### 2. Executar Processamento

**Opção A: Script Automático**
```powershell
.\process_production.ps1
```

**Opção B: Manual**
```powershell
railway run python backend/run_ingestion_dia.py dia1
railway run python backend/run_ingestion_dia.py dia2
```

---

## ⚠️ Importante: PDFs no Railway

Os PDFs precisam estar acessíveis no Railway. Verifique:

1. **PDFs estão no Git?**
   - Se sim, Railway pode acessá-los
   - Verifique se não estão no .gitignore

2. **PDFs via Volume?**
   - Adicione Volume no Railway Dashboard
   - Upload PDFs para o volume

---

## 📊 Verificar Processamento

### Ver Logs:
```powershell
railway logs
```

### Testar API:
```powershell
$url = "https://seu-app.railway.app"
Invoke-WebRequest -Uri "$url/api/chat" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"question": "Quais palestras foram no Dia 1?", "filters": null}'
```

---

**Execute: `railway login` e `railway link` primeiro, depois `.\process_production.ps1`** 🚀

