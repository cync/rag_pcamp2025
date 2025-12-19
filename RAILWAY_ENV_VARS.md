# ✅ Configurar Variáveis de Ambiente no Railway

## 🎉 Progresso!

O container está iniciando! Agora só falta configurar as variáveis de ambiente.

---

## 🔧 Passo a Passo no Railway Dashboard

### 1. Acessar Variáveis de Ambiente

1. **Acesse seu projeto no Railway**
2. **Clique no serviço Backend**
3. **Vá na aba "Variables"** (ou "Variables & Secrets")

### 2. Adicionar Variáveis

Clique em **"+ New Variable"** e adicione cada uma:

#### Variáveis Obrigatórias:

```
OPENAI_API_KEY=sk-sua-chave-openai-aqui
```

> 💡 **Obter chave**: https://platform.openai.com/api-keys

#### Variáveis do Qdrant:

```
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
```

> ⚠️ **Importante**: Se você adicionou Qdrant como serviço no Railway, o `QDRANT_HOST` deve ser o nome do serviço (geralmente `qdrant`)

#### Variáveis Opcionais:

```
ENVIRONMENT=production
LOG_LEVEL=INFO
CORS_ORIGINS=https://seu-app.vercel.app
INGESTION_API_KEY=uma-chave-secreta-aleatoria
```

---

## 🔗 Conectar Qdrant

### Se você ainda não adicionou Qdrant:

1. No projeto Railway, clique em **"+ New"**
2. **Add Database** → **Qdrant**
3. Railway criará automaticamente
4. O nome do serviço será usado como `QDRANT_HOST`

### Verificar nome do serviço Qdrant:

1. No projeto Railway, veja a lista de serviços
2. O nome do serviço Qdrant (geralmente `qdrant`) é o que você usa em `QDRANT_HOST`

---

## ✅ Após Adicionar Variáveis

1. **Salve** as variáveis
2. **Railway fará redeploy automaticamente**
3. Aguarde o deploy completar
4. Teste: `curl https://seu-app.railway.app/api/health`

---

## 🧪 Verificar se Funcionou

```bash
curl https://seu-app.railway.app/api/health
```

Deve retornar:
```json
{"status":"healthy","service":"Product Camp 2025 RAG API"}
```

---

## 📝 Checklist de Variáveis

- [ ] `OPENAI_API_KEY` - Sua chave da OpenAI
- [ ] `QDRANT_HOST` - Nome do serviço Qdrant (geralmente `qdrant`)
- [ ] `QDRANT_PORT` - `6333`
- [ ] `QDRANT_COLLECTION_NAME` - `product_camp_2025`
- [ ] `ENVIRONMENT` - `production` (opcional)
- [ ] `LOG_LEVEL` - `INFO` (opcional)
- [ ] `CORS_ORIGINS` - URL do Vercel (quando tiver)
- [ ] `INGESTION_API_KEY` - Chave secreta aleatória (opcional)

---

## 🆘 Troubleshooting

### "OPENAI_API_KEY não encontrada"
- Verifique se adicionou a variável no Railway
- Verifique se não tem espaços extras
- Verifique se a chave começa com `sk-`

### "Qdrant não conecta"
- Verifique se o serviço Qdrant está rodando
- Verifique se `QDRANT_HOST` está correto (nome do serviço)
- Verifique se `QDRANT_PORT` está como `6333`

---

**Adicione as variáveis e o deploy deve funcionar!** ✅

