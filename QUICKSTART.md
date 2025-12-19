# Quick Start - Product Camp 2025 RAG

## ⚡ Início Rápido (5 minutos)

> 💡 **Primeira vez?** Leia o `START_HERE.md` primeiro!

### Pré-requisitos
- ✅ Python 3.9+ instalado
- ✅ Node.js 18+ instalado
- ✅ Docker instalado e rodando
- ✅ OpenAI API Key (obter em: https://platform.openai.com/api-keys)

### 1. Iniciar Qdrant
```bash
docker-compose up -d
```

Verificar se está rodando:
```bash
docker ps
# Deve mostrar container qdrant
```

### 2. Configurar Backend

**Windows PowerShell:**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows CMD:**
```cmd
cd backend
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Criar arquivo `.env` no diretório `backend/`:**

**Windows PowerShell:**
```powershell
@"
OPENAI_API_KEY=sua_chave_aqui
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=development
LOG_LEVEL=INFO
"@ | Out-File -FilePath .env -Encoding utf8
```

**Windows CMD / Linux / Mac:**
Crie manualmente o arquivo `backend/.env` com:
```
OPENAI_API_KEY=sua_chave_aqui
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=development
LOG_LEVEL=INFO
```

### 3. Adicionar PDFs

Copie seus PDFs das palestras para o diretório `data/pdfs/`

**Windows:**
```powershell
# Criar diretório se não existir
New-Item -ItemType Directory -Force -Path data\pdfs

# Copiar PDFs (ajuste o caminho)
Copy-Item C:\caminho\para\palestras\*.pdf data\pdfs\
```

**Linux/Mac:**
```bash
# Criar diretório se não existir
mkdir -p data/pdfs

# Copiar PDFs
cp /caminho/para/palestras/*.pdf data/pdfs/
```

### 4. Processar PDFs (Ingestão)

**Certifique-se de estar no diretório backend com venv ativado:**
```bash
cd backend
# Ativar venv novamente se necessário
# Windows: .\venv\Scripts\Activate.ps1
# Linux/Mac: source venv/bin/activate

python run_ingestion.py
```

Você verá logs do processamento. Aguarde até ver:
```
Ingestão concluída! Total de chunks: X
```

### 5. Configurar Frontend

**Abrir novo terminal:**
```bash
cd frontend
npm install
```

**Criar `.env.local` (opcional, padrão já funciona):**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 6. Iniciar Servidores

**Terminal 1 - Backend:**
```bash
cd backend
# Ativar venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# ou: venv\Scripts\activate.bat  # Windows CMD
# ou: source venv/bin/activate  # Linux/Mac

uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 7. Acessar e Testar

1. **Frontend**: http://localhost:3000
2. **API Docs**: http://localhost:8000/docs
3. **Health Check**: http://localhost:8000/api/health
4. **Qdrant Dashboard**: http://localhost:6333/dashboard

Faça uma pergunta de teste no frontend!

## ✅ Checklist de Verificação

- [ ] Docker instalado e rodando
- [ ] Qdrant rodando (verificar com `docker ps`)
- [ ] Python 3.9+ instalado
- [ ] Node.js 18+ instalado
- [ ] OpenAI API Key configurada no `.env`
- [ ] PDFs copiados para `data/pdfs/`
- [ ] Ingestão executada com sucesso (vê "Ingestão concluída")
- [ ] Backend rodando (porta 8000 - verificar logs)
- [ ] Frontend rodando (porta 3000 - verificar logs)
- [ ] Teste de pergunta funcionando

## 🆘 Problemas?

### "Docker não encontrado"
- Instale Docker Desktop: https://www.docker.com/products/docker-desktop
- Inicie o Docker Desktop antes de executar `docker-compose up -d`

### "Python não encontrado"
- Windows: Instale do site oficial ou Microsoft Store
- Verifique: `python --version` deve mostrar 3.9+

### "OpenAI API Key inválida"
- Verifique se copiou a chave completa (começa com `sk-`)
- Verifique se tem créditos na conta OpenAI
- Teste a chave em: https://platform.openai.com/api-keys

### "Erro ao conectar ao Qdrant"
- Verifique se Qdrant está rodando: `docker ps`
- Verifique porta 6333: `curl http://localhost:6333/health`

### "Frontend não conecta ao backend"
- Verifique se backend está rodando na porta 8000
- Verifique `NEXT_PUBLIC_API_URL` no `.env.local`
- Verifique CORS no backend (já configurado para localhost:3000)

## 🎯 Próximos Passos

- ✅ **Testado localmente?** Veja `DEPLOY.md` para fazer deploy em produção
- 📖 **Quer entender melhor?** Leia `README.md` e `ARCHITECTURE.md`
- 💡 **Quer otimizar?** Veja `TIPS.md`

## 🎉 Pronto para Usar!

Agora você pode fazer perguntas sobre as palestras do Product Camp 2025!

**Exemplos de perguntas:**
- "Quais são os principais temas abordados nas palestras?"
- "Quem são os palestrantes do evento?"
- "Quais frameworks foram mencionados?"

