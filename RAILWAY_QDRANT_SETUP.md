# 🔧 Configurar Qdrant no Railway

## 🔴 Problema: Qdrant 404 Not Found

O erro indica que o Qdrant não está acessível ou a configuração está incorreta.

---

## ✅ Solução: Adicionar e Configurar Qdrant

### Passo 1: Adicionar Qdrant como Serviço

1. **No Railway Dashboard**, no seu projeto
2. Clique em **"+ New"**
3. Selecione **"Add Database"** ou **"Add Service"**
4. Escolha **"Qdrant"**
5. Railway criará automaticamente um serviço Qdrant

### Passo 2: Verificar Nome do Serviço

1. No projeto Railway, veja a lista de serviços
2. Anote o **nome do serviço Qdrant** (geralmente `qdrant` ou `qdrant-xxxxx`)

### Passo 3: Configurar Variáveis de Ambiente

No serviço **Backend**, vá em **Variables** e configure:

#### Opção A: Usar Nome do Serviço (Recomendado)

```
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
```

> ⚠️ **Importante**: Use o **nome exato do serviço** que aparece no Railway

#### Opção B: Railway pode fornecer variáveis automáticas

Railway pode criar automaticamente variáveis como:
- `QDRANT_URL`
- `QDRANT_HOST`
- `QDRANT_PORT`

Verifique na aba **Variables** do serviço Backend se há variáveis relacionadas ao Qdrant.

### Passo 4: Verificar Conexão

Após configurar, o Railway fará redeploy. Verifique os logs:

- ✅ Deve ver: "Tentando conectar ao Qdrant em qdrant:6333"
- ✅ Deve ver: "Collection 'product_camp_2025' encontrada" (ou warning se não existir)

---

## 🔍 Troubleshooting

### Erro 404 persiste

1. **Verifique o nome do serviço**:
   - No Railway, veja o nome exato do serviço Qdrant
   - Use esse nome em `QDRANT_HOST`

2. **Verifique se o serviço está rodando**:
   - No Railway, veja se o serviço Qdrant está "Running"
   - Se não estiver, clique em "Deploy" ou "Start"

3. **Tente usar URL completa**:
   - Railway pode fornecer `QDRANT_URL`
   - Se disponível, use ela em vez de host:port

4. **Verifique a porta**:
   - Qdrant geralmente usa porta `6333`
   - Mas Railway pode usar outra porta interna

### Verificar Logs do Qdrant

1. No Railway, clique no serviço **Qdrant**
2. Vá em **Logs**
3. Verifique se há erros ou avisos

---

## 📝 Exemplo de Configuração Correta

### No Railway Dashboard:

**Serviço Backend → Variables:**

```
OPENAI_API_KEY=sk-...
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
```

**Serviço Qdrant:**
- Nome: `qdrant` (ou similar)
- Status: Running ✅

---

## ✅ Após Configurar

1. **Salve as variáveis**
2. **Railway fará redeploy automaticamente**
3. **Aguarde o deploy**
4. **Teste**: `curl https://seu-app.railway.app/api/health`

---

## 🚀 Próximo Passo: Processar PDFs

Após o Qdrant estar conectado, você precisará:

1. **Processar PDFs** (ingestão)
2. **Criar a collection** no Qdrant
3. **Popular com dados**

Veja `RAILWAY_ENV_VARS.md` para mais detalhes.

---

**Configure o Qdrant e o erro 404 deve desaparecer!** ✅

