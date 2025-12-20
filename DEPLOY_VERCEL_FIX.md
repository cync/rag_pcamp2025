# 🔧 Correção do Deploy Vercel

## Problema

O Vercel estava tentando executar `cd frontend && npm install`, mas o diretório não era encontrado durante o build.

## Solução

Atualizei o `vercel.json` para usar `rootDirectory: "frontend"` em vez de comandos com `cd`.

### Configuração Corrigida

```json
{
  "buildCommand": "npm install && npm run build",
  "outputDirectory": ".next",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "rootDirectory": "frontend"
}
```

## Próximos Passos

1. **Commit e Push das alterações:**
   ```bash
   git add vercel.json
   git commit -m "Fix Vercel configuration"
   git push
   ```

2. **No Vercel Dashboard:**
   - O Vercel detectará automaticamente o `vercel.json`
   - Ou configure manualmente:
     - **Root Directory**: `frontend`
     - **Build Command**: `npm run build`
     - **Output Directory**: `.next`
     - **Install Command**: `npm install`

3. **Variáveis de Ambiente:**
   No Vercel Dashboard → Settings → Environment Variables:
   ```
   NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app
   ```

4. **Redeploy:**
   - O Vercel fará deploy automaticamente após o push
   - Ou clique em "Redeploy" no dashboard

## Verificação

Após o deploy, verifique:
- ✅ Build completa sem erros
- ✅ Site acessível
- ✅ API calls funcionando
- ✅ Filtro de palestras carregando

## Nota

O `rootDirectory` faz com que o Vercel execute todos os comandos dentro do diretório `frontend`, então não precisa usar `cd frontend` nos comandos.

