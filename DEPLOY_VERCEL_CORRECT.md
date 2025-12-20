# ✅ Configuração Correta do Vercel

## Problema

O Vercel não aceita `rootDirectory` no `vercel.json`. Essa propriedade deve ser configurada no **Dashboard do Vercel**.

## Solução

### Opção 1: Configurar no Dashboard (RECOMENDADO)

1. Acesse o projeto no Vercel Dashboard
2. Vá em **Settings** → **General**
3. Em **Root Directory**, configure:
   - Selecione **Root Directory**
   - Digite: `frontend`
   - Salve

4. O `vercel.json` deve ter apenas:
   ```json
   {
     "buildCommand": "npm install && npm run build",
     "outputDirectory": ".next",
     "framework": "nextjs"
   }
   ```

### Opção 2: Usar comandos com `cd` (ATUAL)

O `vercel.json` atual usa comandos com `cd frontend`:

```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/.next",
  "framework": "nextjs"
}
```

**Mas isso pode falhar se o diretório não existir no momento do build.**

## Solução Definitiva

### Configure no Dashboard do Vercel:

1. **Settings** → **General**
2. **Root Directory**: `frontend`
3. Salve

### Simplifique o `vercel.json`:

```json
{
  "buildCommand": "npm install && npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://pcamp2025.up.railway.app/api/:path*"
    }
  ]
}
```

## Variáveis de Ambiente

No Vercel Dashboard → **Settings** → **Environment Variables**:

```
NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app
```

## Após Configurar

1. Faça um novo deploy (Redeploy)
2. O build deve funcionar corretamente

