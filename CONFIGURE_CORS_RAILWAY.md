# 🔧 Configurar CORS no Railway

## ⚠️ IMPORTANTE: Ação Necessária

O código já foi atualizado para incluir a URL do Vercel, mas você **AINDA PRECISA** configurar a variável `CORS_ORIGINS` no Railway para garantir que funcione.

## 📋 Passo a Passo

### 1. Acesse o Railway Dashboard

1. Acesse: https://railway.app
2. Faça login na sua conta
3. Selecione o projeto do backend

### 2. Configure a Variável CORS_ORIGINS

1. No projeto, clique no serviço **Backend**
2. Vá na aba **Variables** (ou **Settings** → **Variables**)
3. Procure por `CORS_ORIGINS` na lista
4. Se não existir, clique em **+ New Variable**
5. Configure:
   - **Name**: `CORS_ORIGINS`
   - **Value**: 
     ```
     https://rag-pcamp2025.vercel.app,http://localhost:3000,http://localhost:3001
     ```
6. Clique em **Add** ou **Save**

### 3. Redeploy

Após adicionar a variável:

1. O Railway fará **redeploy automático** (pode levar 1-2 minutos)
2. Ou clique em **Deployments** → **Redeploy** no último deploy

### 4. Verificar

Após o redeploy:

1. Aguarde 1-2 minutos para o deploy completar
2. Acesse: https://rag-pcamp2025.vercel.app
3. Abra o Console do navegador (F12)
4. Recarregue a página
5. Verifique se não há mais erros de CORS
6. As palestras devem aparecer no filtro

## 🔍 Verificar se Funcionou

### No Console do Navegador:

**Antes (erro):**
```
Access to XMLHttpRequest ... blocked by CORS policy
```

**Depois (sucesso):**
```
Palestras carregadas: Array(10)
```

### Teste Direto da API:

Abra no navegador:
```
https://pcamp2025.up.railway.app/api/palestras
```

Deve retornar um JSON com as palestras.

## 📝 Nota sobre Múltiplos Domínios Vercel

Se você tiver preview deployments do Vercel, adicione também:

```
https://rag-pcamp2025.vercel.app,https://rag-pcamp2025-git-*.vercel.app,http://localhost:3000
```

**OU** use apenas o domínio principal (o código já inclui o principal por padrão).

## 🐛 Se Ainda Não Funcionar

1. Verifique se a variável foi salva corretamente no Railway
2. Verifique se o redeploy foi concluído
3. Verifique os logs do Railway para erros
4. Limpe o cache do navegador (Ctrl+Shift+R)
5. Teste em modo anônimo/privado

## ✅ Checklist

- [ ] Variável `CORS_ORIGINS` configurada no Railway
- [ ] Valor inclui `https://rag-pcamp2025.vercel.app`
- [ ] Redeploy concluído
- [ ] Sem erros de CORS no console
- [ ] Palestras aparecem no filtro

