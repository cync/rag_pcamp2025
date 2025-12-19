# ✅ Solução Simples: Railway Deploy

## 🎯 Configuração no Railway Dashboard

A **forma mais simples e confiável** é configurar manualmente no Railway:

### Passo a Passo:

1. **Acesse seu projeto no Railway**
2. **Clique no serviço Backend**
3. **Vá em Settings**
4. **Configure:**

   - **Root Directory**: `backend`
   - **Build Command**: (deixe **VAZIO**)
   - **Start Command**: 
     ```
     gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT
     ```

5. **Salve**

### Por que isso funciona?

- Railway detecta automaticamente Python pelo `requirements.txt` em `backend/`
- Nixpacks instala tudo automaticamente
- Não precisa de Dockerfile ou configurações complexas
- **É a forma mais confiável!**

---

## 🔄 Alternativa: Se ainda não funcionar

### Opção A: Usar Dockerfile com contexto correto

No Railway Dashboard:
1. **Settings** → **Root Directory**: (deixe **VAZIO** - raiz do projeto)
2. **Settings** → **Dockerfile Path**: `backend/Dockerfile`
3. **Settings** → **Build Context**: `.` (raiz)

### Opção B: Mover Dockerfile para raiz

Se preferir, podemos mover o Dockerfile para a raiz do projeto.

---

## ✅ Verificar

Após configurar, o Railway fará deploy automaticamente.

Teste:
```bash
curl https://seu-app.railway.app/api/health
```

---

**A configuração manual no Dashboard (Root Directory = `backend`) é a mais simples e funciona!** ✅

