# 🔍 Verificar Configuração do Qdrant

## ⚠️ Erro 404 Detectado

Os logs mostram que o Qdrant está retornando erro 404. Vamos verificar a configuração.

---

## 🔧 Verificar Variáveis no Railway

### 1. Acessar Variáveis

1. Railway Dashboard → Seu Projeto → Serviço Backend
2. Vá em **Variables**

### 2. Verificar Variáveis Configuradas

Você deve ter **UMA** das seguintes configurações:

#### Opção A: Qdrant Cloud (Recomendado se você tem cluster)

```
QDRANT_URL=https://seu-cluster.qdrant.io
QDRANT_API_KEY=sua-api-key-aqui
QDRANT_COLLECTION_NAME=product_camp_2025
```

**Verifique:**
- ✅ `QDRANT_URL` começa com `https://`
- ✅ `QDRANT_URL` é a URL completa do cluster
- ✅ `QDRANT_API_KEY` está configurada
- ✅ Não há espaços extras nas variáveis

#### Opção B: Qdrant como Serviço Railway

```
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
```

**Verifique:**
- ✅ Existe um serviço Qdrant no projeto Railway
- ✅ `QDRANT_HOST` é o nome exato do serviço
- ✅ O serviço Qdrant está rodando (verde)

---

## 🐛 Problemas Comuns

### Problema 1: URL Incorreta

**Sintoma:** Erro 404 mesmo com API Key configurada

**Solução:**
- Verifique se `QDRANT_URL` é a URL completa do cluster
- Deve começar com `https://`
- Exemplo correto: `https://abc123-def456.us-east-1-0.aws.cloud.qdrant.io`
- Exemplo incorreto: `abc123-def456.us-east-1-0.aws.cloud.qdrant.io` (sem https://)

### Problema 2: API Key Incorreta

**Sintoma:** Erro 401 ou 403

**Solução:**
- Verifique se `QDRANT_API_KEY` está correta
- Não deve ter espaços extras
- Deve ser a chave do seu cluster Qdrant Cloud

### Problema 3: Variáveis Não Configuradas

**Sintoma:** Usando host:port ao invés de URL

**Solução:**
- Adicione `QDRANT_URL` e `QDRANT_API_KEY` no Railway
- Railway fará redeploy automático

---

## ✅ Após Corrigir

1. **Railway fará redeploy automático**
2. **Verifique os logs** - deve mostrar:
   ```
   INFO:rag.vector_store:Conectando ao Qdrant Cloud: https://seu-cluster.qdrant.io
   INFO:rag.vector_store:Usando autenticação com API Key
   ```

3. **Se ainda aparecer 404**, verifique:
   - A URL está correta?
   - A API Key está correta?
   - O cluster Qdrant está acessível?

---

## 🧪 Testar Conexão

Após corrigir, teste:

```powershell
$url = "https://web-production-42847.up.railway.app"
Invoke-WebRequest -Uri "$url/api/health"
```

Deve retornar 200 OK.

---

**Verifique as variáveis acima e corrija se necessário! 🔧**

