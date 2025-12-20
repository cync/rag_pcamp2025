# 🔧 Correção dos Erros de Deploy no Vercel

## Problema

Todos os deploys estão falhando com status "Error". O problema mais comum é que o **Root Directory** não está configurado no Dashboard do Vercel.

## ✅ Solução Passo a Passo

### 1. Configurar Root Directory no Dashboard

**IMPORTANTE:** O `rootDirectory` NÃO pode estar no `vercel.json`. Deve ser configurado no Dashboard.

1. Acesse: https://vercel.com/dashboard
2. Selecione seu projeto
3. Vá em **Settings** → **General**
4. Role até a seção **Root Directory**
5. Clique em **Edit**
6. Selecione **Root Directory**
7. Digite: `frontend`
8. Clique em **Save**

### 2. Verificar Variáveis de Ambiente

1. No mesmo projeto, vá em **Settings** → **Environment Variables**
2. Adicione (se não existir):
   ```
   NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app
   ```
3. Selecione os ambientes: **Production**, **Preview**, **Development**
4. Clique em **Save**

### 3. Verificar Build Settings

1. Vá em **Settings** → **General**
2. Verifique **Build & Development Settings**:
   - **Framework Preset**: Next.js (deve ser detectado automaticamente)
   - **Build Command**: `npm run build` (ou deixe vazio para usar o padrão)
   - **Output Directory**: `.next` (ou deixe vazio para usar o padrão)
   - **Install Command**: `npm install` (ou deixe vazio para usar o padrão)

### 4. Fazer Novo Deploy

Após configurar o Root Directory:

1. Vá em **Deployments**
2. Clique no menu (três pontos) do último deploy
3. Selecione **Redeploy**
4. Ou faça um novo commit e push (o Vercel detectará automaticamente)

## 🔍 Verificar Logs de Erro

Se ainda falhar após configurar o Root Directory:

1. Clique no deploy que falhou
2. Vá na aba **Build Logs**
3. Procure por erros como:
   - `No such file or directory: frontend`
   - `Cannot find module`
   - `TypeScript errors`
   - `Build failed`

## 📋 Checklist

- [ ] Root Directory configurado como `frontend` no Dashboard
- [ ] Variável `NEXT_PUBLIC_API_URL` configurada
- [ ] Build Command: `npm run build` (ou vazio)
- [ ] Output Directory: `.next` (ou vazio)
- [ ] Framework: Next.js detectado
- [ ] Novo deploy iniciado após configurações

## 🐛 Erros Comuns

### Erro: "No such file or directory"
- **Causa**: Root Directory não configurado
- **Solução**: Configure `frontend` no Dashboard

### Erro: "Cannot find module '@/...'"
- **Causa**: Problema com path aliases do TypeScript
- **Solução**: Verifique se `tsconfig.json` tem `"@/*": ["./*"]`

### Erro: "TypeScript errors"
- **Causa**: Erros de tipo no código
- **Solução**: Execute `npm run build` localmente para ver os erros

### Erro: "Build failed"
- **Causa**: Erro durante o build
- **Solução**: Veja os logs completos no Vercel

## 🚀 Teste Local

Antes de fazer deploy, teste localmente:

```bash
cd frontend
npm install
npm run build
```

Se o build local funcionar, o deploy no Vercel também deve funcionar (após configurar o Root Directory).

## 📝 Nota Importante

O `vercel.json` atual está correto e NÃO deve ter `rootDirectory`. A configuração do Root Directory deve ser feita **apenas no Dashboard do Vercel**.

