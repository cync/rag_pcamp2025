# Deploy do Frontend no Vercel

## Pré-requisitos

1. Conta no Vercel (https://vercel.com)
2. Repositório Git configurado (GitHub, GitLab ou Bitbucket)
3. Backend já deployado no Railway

## Passo a Passo

### 1. Configurar Variáveis de Ambiente

No Vercel Dashboard:

1. Acesse seu projeto
2. Vá em **Settings** → **Environment Variables**
3. Adicione:
   ```
   NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app
   ```

### 2. Deploy via Vercel Dashboard

1. Acesse https://vercel.com/new
2. Conecte seu repositório Git
3. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
   - **Install Command**: `npm install`
4. Clique em **Deploy**

### 3. Deploy via CLI (Alternativa)

```bash
# Instalar Vercel CLI
npm i -g vercel

# Fazer login
vercel login

# Navegar para o diretório frontend
cd frontend

# Deploy
vercel

# Deploy em produção
vercel --prod
```

### 4. Configuração Automática

O arquivo `vercel.json` na raiz já está configurado para:
- Build do frontend
- Rewrites para API (proxying)
- Variáveis de ambiente

### 5. Verificar Deploy

Após o deploy:
1. Acesse a URL fornecida pelo Vercel
2. Teste a interface
3. Verifique se as chamadas à API estão funcionando

## Troubleshooting

### Erro: "API URL not found"
- Verifique se `NEXT_PUBLIC_API_URL` está configurada no Vercel
- Verifique se o backend está rodando no Railway

### Erro: "CORS"
- Verifique se `CORS_ORIGINS` no Railway inclui a URL do Vercel
- Adicione: `https://seu-projeto.vercel.app`

### Build Fails
- Verifique os logs no Vercel Dashboard
- Certifique-se de que todas as dependências estão no `package.json`

## Estrutura de Deploy

```
Frontend (Vercel)
  ↓
  API Calls
  ↓
Backend (Railway)
  ↓
  Qdrant Cloud
```

## URLs de Exemplo

- Frontend: `https://pcamp2025-rag.vercel.app`
- Backend: `https://pcamp2025.up.railway.app`
- API: `https://pcamp2025.up.railway.app/api`

