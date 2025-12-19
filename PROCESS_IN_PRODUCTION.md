# 🚀 Processar PDFs em Produção (Railway)

## 📋 Opções para Processar no Railway

### Opção 1: Via Railway CLI (Recomendado)

#### 1. Instalar Railway CLI

```powershell
npm install -g @railway/cli
```

#### 2. Login e Link

```powershell
railway login
railway link
```

#### 3. Upload PDFs para Railway

Você precisa fazer upload dos PDFs primeiro. Opções:

**A. Via Volume no Railway:**
1. No Railway Dashboard, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume via Railway CLI ou interface

**B. Via Git (não recomendado para arquivos grandes):**
- Os PDFs já estão no repositório em `data/pdfs/`
- Railway pode acessá-los durante o build

#### 4. Processar

```powershell
# Processar Dia 1
railway run python backend/run_ingestion_dia.py dia1

# Processar Dia 2
railway run python backend/run_ingestion_dia.py dia2

# Ou processar todos
railway run python backend/run_ingestion_dia.py all
```

---

### Opção 2: Via Endpoint de Ingestão

Se você configurou `INGESTION_API_KEY` no Railway:

```powershell
$apiKey = "sua-chave-secreta"
$railwayUrl = "https://seu-app.railway.app"

curl -X POST "$railwayUrl/api/ingest" `
  -H "X-API-Key: $apiKey"
```

**Nota**: Para isso funcionar, os PDFs precisam estar acessíveis no container do Railway.

---

### Opção 3: Via Shell do Railway

1. No Railway Dashboard → **Deployments**
2. Clique no deployment mais recente
3. Abra **Shell**
4. Execute:
   ```bash
   cd backend
   python run_ingestion_dia.py dia1
   python run_ingestion_dia.py dia2
   ```

---

## 📝 Preparação

### 1. Verificar Variáveis de Ambiente no Railway

Certifique-se de que estão configuradas:
- `OPENAI_API_KEY` ✅
- `QDRANT_HOST` (nome do serviço Qdrant)
- `QDRANT_PORT` (6333)
- `QDRANT_COLLECTION_NAME` (product_camp_2025)

### 2. Verificar Qdrant no Railway

- Serviço Qdrant deve estar rodando
- Nome do serviço deve estar em `QDRANT_HOST`

---

## 🚀 Executar Agora

Vou instalar o Railway CLI e executar o processamento:

