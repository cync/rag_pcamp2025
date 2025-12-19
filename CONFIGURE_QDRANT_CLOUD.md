# ☁️ Configurar Qdrant Cloud no Railway

## ✅ Você tem um Cluster Qdrant Cloud!

Perfeito! Vamos configurar para usar seu cluster Qdrant Cloud com API Key.

---

## 🔧 Configuração no Railway

### 1. Acessar Variáveis de Ambiente

1. Acesse: https://railway.app
2. Abra seu projeto
3. Clique no serviço **Backend**
4. Vá em **Variables**

### 2. Adicionar Variáveis do Qdrant Cloud

Adicione as seguintes variáveis:

```
QDRANT_URL=https://seu-cluster.qdrant.io
QDRANT_API_KEY=sua-api-key-aqui
QDRANT_COLLECTION_NAME=product_camp_2025
```

> ⚠️ **IMPORTANTE**: 
> - `QDRANT_URL` deve ser a URL completa do seu cluster (ex: `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io`)
> - `QDRANT_API_KEY` é a chave de API do seu cluster Qdrant Cloud
> - Não precisa configurar `QDRANT_HOST` ou `QDRANT_PORT` quando usar Qdrant Cloud

### 3. Exemplo de Configuração

Se seu cluster Qdrant Cloud é:
- **URL**: `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io`
- **API Key**: `your-api-key-here`

Configure no Railway:

```
QDRANT_URL=https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io
QDRANT_API_KEY=your-api-key-here
QDRANT_COLLECTION_NAME=product_camp_2025
```

---

## ✅ Verificar se Funcionou

Após adicionar as variáveis, o Railway fará **redeploy automático**. 

### Logs Esperados (Sucesso):

```
INFO:rag.vector_store:Conectando ao Qdrant Cloud: https://seu-cluster.qdrant.io
INFO:rag.vector_store:Collection 'product_camp_2025' encontrada
```

ou

```
INFO:rag.vector_store:Conectando ao Qdrant Cloud: https://seu-cluster.qdrant.io
WARNING:rag.vector_store:Collection 'product_camp_2025' não encontrada. Execute o script de ingestão primeiro.
```

> ⚠️ O warning é **normal** se você ainda não processou os PDFs. A collection será criada durante a ingestão.

---

## 🚀 Processar PDFs

Após configurar, você pode processar os PDFs:

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "sua-chave-secreta"
```

Ou se você configurou `INGESTION_API_KEY` no Railway:

```powershell
$url = "https://web-production-42847.up.railway.app"
$apiKey = "sua-ingestion-api-key"

Invoke-WebRequest -Uri "$url/api/ingest" `
  -Method POST `
  -Headers @{"X-API-Key" = $apiKey}
```

---

## 📝 Checklist

- [ ] `QDRANT_URL` configurada com URL completa do cluster
- [ ] `QDRANT_API_KEY` configurada com sua chave de API
- [ ] `QDRANT_COLLECTION_NAME` configurada como `product_camp_2025`
- [ ] `OPENAI_API_KEY` configurada
- [ ] Railway fez redeploy após adicionar variáveis
- [ ] Logs mostram conexão bem-sucedida ao Qdrant Cloud

---

## 🔍 Troubleshooting

### Erro de Conexão

Se ainda aparecer erro de conexão:

1. **Verifique a URL**: Deve começar com `https://` e ser a URL completa do cluster
2. **Verifique a API Key**: Deve ser a chave correta do seu cluster
3. **Verifique os logs**: Veja mensagens de erro específicas no Railway Dashboard

### Collection Não Existe

Se aparecer warning sobre collection não existir:
- Isso é **normal** antes de processar os PDFs
- A collection será criada automaticamente durante a ingestão
- Não é um erro!

---

**Configure as variáveis acima e seu Qdrant Cloud estará pronto! 🚀**

