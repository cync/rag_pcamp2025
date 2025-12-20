# ✅ Configuração Railway para Produção

## 🔧 Configuração Corrigida

O Dockerfile foi atualizado para usar a variável `PORT` do Railway dinamicamente e bindar em `0.0.0.0` para produção.

---

## ✅ Mudanças Aplicadas

### Dockerfile Atualizado:

```dockerfile
# Bind em 0.0.0.0 para aceitar conexões de qualquer IP (produção)
# Usa variável PORT do Railway dinamicamente
CMD ["sh", "-c", "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000}"]
```

**O que mudou:**
- ✅ Agora usa `${PORT}` do Railway (dinâmico)
- ✅ Bind em `0.0.0.0` (aceita conexões de qualquer IP)
- ✅ Fallback para `8000` se PORT não estiver definido

---

## 🔍 Verificar Configuração no Railway

### 1. Settings do Serviço Backend

No Railway Dashboard → Backend → **Settings**, verifique:

- **Root Directory**: (deixe **VAZIO** - raiz do projeto)
- **Dockerfile Path**: `Dockerfile` (ou deixe padrão)
- **Start Command**: (deixe **VAZIO** - Dockerfile já tem CMD)
- **Build Command**: (deixe **VAZIO**)

### 2. Variável PORT

O Railway **injeta automaticamente** a variável `PORT`. Você **não precisa** configurá-la manualmente.

### 3. Network Configuration

O Railway configura automaticamente:
- ✅ Porta dinâmica via variável `PORT`
- ✅ Roteamento para o container
- ✅ IP público para acesso externo

---

## 🚀 Após Atualizar

1. **Commit e Push:**
   ```bash
   git add Dockerfile
   git commit -m "Fix Railway production config - use PORT variable and bind to 0.0.0.0"
   git push
   ```

2. **Railway fará deploy automático**

3. **Aguarde o deploy completar**

4. **Teste:**
   ```powershell
   $url = "https://pcamp2025.up.railway.app"
   Invoke-WebRequest -Uri "$url/api/health"
   ```

---

## ✅ O que está correto agora

- ✅ Bind em `0.0.0.0` (todas as interfaces de rede)
- ✅ Usa variável `PORT` do Railway dinamicamente
- ✅ Configurado para produção
- ✅ Aceita conexões de qualquer IP

---

**A configuração está correta para produção! 🚀**

