# ✅ Fix: Procfile causando erro "cd not found"

## 🔴 Problema Encontrado

O `Procfile` tinha:
```
web: cd backend && gunicorn ...
```

Isso causava erro porque o Railway tentava executar `cd` dentro do container.

## ✅ Solução Aplicada

1. **Corrigido Procfile**: Removido `cd backend` (não é necessário)
2. **Melhorado Dockerfile CMD**: Usar formato JSON com shell para suportar variável PORT

---

## 📝 Mudanças

### Procfile (corrigido):
```
web: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
```

### Dockerfile CMD (melhorado):
```dockerfile
CMD ["sh", "-c", "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000}"]
```

---

## ⚠️ Importante: No Railway Dashboard

**Verifique as configurações:**

1. **Settings** → **Start Command**: (deixe **VAZIO**)
   - O Dockerfile já tem o CMD correto
   - Não precisa de Start Command adicional

2. **Settings** → **Root Directory**: (deixe **VAZIO** - raiz)

3. **Settings** → **Dockerfile Path**: `Dockerfile`

---

## ✅ Por que isso funciona?

- O Dockerfile já copia tudo para `/app`
- O WORKDIR já está em `/app`
- Não precisa de `cd` - tudo já está no lugar certo
- O Procfile agora também está correto (caso Railway use ele)

---

**Agora deve funcionar! O problema era o Procfile com `cd`.** ✅

