# 🔧 Fix: Erro Nixpacks no Railway

## Problema
Nixpacks está saindo com erro durante o build no Railway.

## Soluções

### Solução 1: Usar Root Directory (Recomendado)

No Railway Dashboard:

1. **Settings** → **Root Directory**: `backend`
2. **Settings** → **Build Command**: (deixe vazio)
3. **Settings** → **Start Command**: 
   ```
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
   ```

Isso faz o Railway trabalhar diretamente no diretório `backend`, onde está o `requirements.txt`.

### Solução 2: Remover .nixpacks.toml

Se a Solução 1 não funcionar:

1. Delete o arquivo `.nixpacks.toml` da raiz
2. Configure no Railway Dashboard:
   - **Root Directory**: `backend`
   - **Start Command**: `gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT`

### Solução 3: Usar Dockerfile

Se ainda não funcionar, use o Dockerfile:

1. No Railway, vá em **Settings**
2. **Build Command**: (deixe vazio)
3. Railway detectará automaticamente o `Dockerfile` em `backend/Dockerfile`

Mas primeiro, precisamos mover o Dockerfile ou ajustar o caminho.

### Solução 4: Configuração Manual no Railway

1. **Settings** → **Root Directory**: `backend`
2. **Settings** → **Build Command**: 
   ```
   pip install --upgrade pip && pip install -r requirements.txt
   ```
3. **Settings** → **Start Command**: 
   ```
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
   ```

## Verificar Logs

No Railway Dashboard:
1. Vá em **Deployments**
2. Clique no deployment mais recente
3. Veja os **Logs** para entender o erro específico

## Arquivos Atualizados

- ✅ `.nixpacks.toml` - Corrigido
- ✅ `railway.json` - Atualizado
- ✅ `backend/runtime.txt` - Adicionado

## Próximos Passos

1. Faça commit das mudanças:
   ```bash
   git add .
   git commit -m "Fix Railway nixpacks configuration"
   git push
   ```

2. No Railway, tente a **Solução 1** primeiro (Root Directory = `backend`)

3. Se não funcionar, tente as outras soluções na ordem

