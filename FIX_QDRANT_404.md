# 🔧 Corrigir Erro Qdrant 404 no Railway

## ❌ Problema

Os logs mostram:
```
WARNING:rag.vector_store:Não foi possível verificar collections: Unexpected Response: 404 (Not Found)
```

Isso significa que o **Qdrant não está acessível** ou não está configurado corretamente.

---

## ✅ Solução Passo a Passo

### 1. Verificar se Qdrant Existe no Railway

1. Acesse: https://railway.app
2. Abra seu projeto
3. Veja a lista de serviços
4. **Verifique se há um serviço Qdrant**

### 2. Se NÃO Existe - Adicionar Qdrant

1. No projeto Railway, clique em **"+ New"**
2. Selecione **"Add Database"** ou **"Add Service"**
3. Escolha **"Qdrant"**
4. Railway criará automaticamente
5. **Anote o nome do serviço** (geralmente `qdrant` ou `qdrant-xxxxx`)

### 3. Configurar Variáveis de Ambiente

No serviço **Backend**, vá em **Variables** e adicione/verifique:

```
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
```

> ⚠️ **IMPORTANTE**: 
> - `QDRANT_HOST` deve ser o **nome exato do serviço** que aparece no Railway
> - Se o serviço se chama `qdrant-abc123`, use `qdrant-abc123`
> - Geralmente é apenas `qdrant`

### 4. Verificar Variáveis Automáticas do Railway

Railway pode criar automaticamente variáveis quando você adiciona Qdrant:

1. No serviço **Backend** → **Variables**
2. Procure por variáveis como:
   - `QDRANT_URL`
   - `QDRANT_HOST` (pode já estar criada)
   - `QDRANT_PORT` (pode já estar criada)

3. **Se existirem**, use essas variáveis ao invés de criar manualmente

### 5. Verificar Status do Serviço Qdrant

1. No Railway, clique no serviço **Qdrant**
2. Verifique se está **"Running"** ou **"Deployed"** (verde)
3. Se não estiver, clique em **"Deploy"** ou **"Start"**

---

## 🔍 Verificar se Funcionou

Após configurar, o Railway fará **redeploy automático**. Verifique os logs:

### ✅ Logs Esperados (Sucesso):

```
INFO:rag.vector_store:Tentando conectar ao Qdrant em qdrant:6333
INFO:rag.vector_store:Collection 'product_camp_2025' encontrada
```

ou

```
INFO:rag.vector_store:Tentando conectar ao Qdrant em qdrant:6333
WARNING:rag.vector_store:Collection 'product_camp_2025' não encontrada. Execute o script de ingestão primeiro.
```

> ⚠️ O warning é **normal** se você ainda não processou os PDFs. A collection será criada durante a ingestão.

### ❌ Logs de Erro (Ainda com Problema):

```
ERROR:rag.vector_store:Erro ao conectar ao Qdrant
WARNING:rag.vector_store:Não foi possível verificar collections: 404 Not Found
```

Se ainda aparecer erro 404:
- Verifique se o nome do serviço está correto
- Verifique se o serviço Qdrant está rodando
- Tente usar `QDRANT_URL` se Railway forneceu

---

## 🚀 Após Corrigir

Quando o Qdrant estiver conectado:

1. **Teste o health check:**
   ```powershell
   Invoke-WebRequest -Uri "https://web-production-42847.up.railway.app/api/health"
   ```

2. **Processe os PDFs:**
   ```powershell
   .\PROCESS_WITH_URL.ps1 -ApiKey "sua-chave-secreta"
   ```

---

## 📝 Checklist

- [ ] Serviço Qdrant existe no Railway
- [ ] Serviço Qdrant está "Running" (verde)
- [ ] `QDRANT_HOST` configurado com nome correto do serviço
- [ ] `QDRANT_PORT` configurado como `6333`
- [ ] `QDRANT_COLLECTION_NAME` configurado como `product_camp_2025`
- [ ] Logs não mostram mais erro 404
- [ ] Health check retorna 200 OK

---

**Siga os passos acima e o Qdrant deve conectar! 🚀**

