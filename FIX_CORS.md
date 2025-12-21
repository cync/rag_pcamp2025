# 🔧 Correção de CORS

## Problema

O frontend no Vercel não consegue acessar o backend no Railway devido a erro de CORS:

```
Access to XMLHttpRequest at 'https://pcamp2025.up.railway.app/api/palestras' 
from origin 'https://rag-pcamp2025.vercel.app' 
has been blocked by CORS policy
```

## Solução

### 1. Atualizar Variável de Ambiente no Railway

No Railway Dashboard:

1. Acesse: https://railway.app
2. Vá em seu projeto → Backend → Variables
3. Encontre ou adicione: `CORS_ORIGINS`
4. Configure o valor:
   ```
   https://rag-pcamp2025.vercel.app,http://localhost:3000,http://localhost:3001
   ```
5. Salve

### 2. Verificar Código

O código já foi atualizado para:
- Aceitar múltiplas origens separadas por vírgula
- Incluir a URL do Vercel por padrão
- Logar as origens configuradas

### 3. Redeploy

Após atualizar a variável:
- O Railway fará redeploy automaticamente
- Ou clique em "Redeploy" no dashboard

## Verificação

Após o redeploy, teste:

1. Abra o console do navegador (F12)
2. Recarregue a página do Vercel
3. Verifique se não há mais erros de CORS
4. As palestras devem aparecer no filtro

## URLs

- Frontend: `https://rag-pcamp2025.vercel.app`
- Backend: `https://pcamp2025.up.railway.app`

## Nota

Se você tiver múltiplos domínios do Vercel (preview, production), adicione todos:

```
https://rag-pcamp2025.vercel.app,https://rag-pcamp2025-git-main-*.vercel.app,http://localhost:3000
```

