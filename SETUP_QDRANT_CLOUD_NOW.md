# ⚡ Configurar Qdrant Cloud AGORA

## 🔴 Problema Identificado

Os logs mostram:
```
WARNING:rag.vector_store:Usando host:port. Se você tem Qdrant Cloud, configure QDRANT_URL e QDRANT_API_KEY
```

Isso significa que as variáveis do Qdrant Cloud **não estão configuradas** no Railway.

---

## ✅ Solução Rápida

### 1. Acessar Railway Dashboard

1. Acesse: https://railway.app
2. Abra seu projeto
3. Clique no serviço **Backend**
4. Vá em **Variables** (ou "Variables & Secrets")

### 2. Adicionar Variáveis do Qdrant Cloud

Clique em **"+ New Variable"** e adicione **EXATAMENTE** estas 3 variáveis:

#### Variável 1: QDRANT_URL
```
Nome: QDRANT_URL
Valor: https://seu-cluster.qdrant.io
```

> ⚠️ **IMPORTANTE**: 
> - Substitua `seu-cluster.qdrant.io` pela URL real do seu cluster Qdrant Cloud
> - Deve começar com `https://`
> - Exemplo: `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io`

#### Variável 2: QDRANT_API_KEY
```
Nome: QDRANT_API_KEY
Valor: sua-api-key-aqui
```

> ⚠️ **IMPORTANTE**: 
> - Substitua `sua-api-key-aqui` pela sua chave de API real do Qdrant Cloud
> - Não deve ter espaços extras
> - Não deve ter aspas

#### Variável 3: QDRANT_COLLECTION_NAME
```
Nome: QDRANT_COLLECTION_NAME
Valor: product_camp_2025
```

### 3. Exemplo Completo

Se seu cluster Qdrant Cloud é:
- **URL**: `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io`
- **API Key**: `your-secret-api-key-here`

Configure no Railway:

| Nome | Valor |
|------|-------|
| `QDRANT_URL` | `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io` |
| `QDRANT_API_KEY` | `your-secret-api-key-here` |
| `QDRANT_COLLECTION_NAME` | `product_camp_2025` |

---

## ✅ Após Adicionar

1. **Railway fará redeploy automático** (aguarde 1-2 minutos)
2. **Verifique os logs** - deve mostrar:
   ```
   INFO:rag.vector_store:Conectando ao Qdrant Cloud: https://seu-cluster.qdrant.io
   INFO:rag.vector_store:Usando autenticação com API Key
   ```

3. **Se ainda aparecer erro 404**, verifique:
   - A URL está correta? (deve começar com `https://`)
   - A API Key está correta?
   - Não há espaços extras nas variáveis?

---

## 🚀 Processar PDFs

Após configurar e o backend conectar ao Qdrant Cloud:

```powershell
.\PROCESS_WITH_URL.ps1 -ApiKey "sua-ingestion-api-key"
```

---

## 📝 Checklist

- [ ] `QDRANT_URL` adicionada (URL completa com `https://`)
- [ ] `QDRANT_API_KEY` adicionada (sua chave real)
- [ ] `QDRANT_COLLECTION_NAME` adicionada (`product_camp_2025`)
- [ ] Railway fez redeploy
- [ ] Logs mostram "Conectando ao Qdrant Cloud"

---

**Adicione as 3 variáveis acima no Railway e aguarde o redeploy! 🚀**

