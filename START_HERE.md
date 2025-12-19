# 🎯 POR ONDE COMEÇAR?

## Você está aqui! 👋

Este é o guia definitivo para começar a usar o sistema RAG do Product Camp 2025.

---

## 🚀 Roteiro Rápido

### Para Desenvolvimento Local (Testar Agora)

1. **Leia**: `QUICKSTART.md` ⚡ (5 minutos)
2. **Siga**: Passo a passo do `QUICKSTART.md`
3. **Teste**: Faça uma pergunta no sistema

### Para Deploy em Produção

1. **Leia**: `DEPLOY.md` 📖 (guia completo)
2. **Escolha**: Opção de deploy (VPS, Docker, etc)
3. **Siga**: Instruções detalhadas

---

## 📚 Documentação Disponível

| Arquivo | Quando Usar |
|---------|-------------|
| **QUICKSTART.md** | ⚡ Quer testar AGORA (5 min) |
| **DEPLOY.md** | 🌐 Quer fazer deploy em produção |
| **SETUP.md** | 🔧 Setup detalhado passo a passo |
| **README.md** | 📖 Documentação completa |
| **ARCHITECTURE.md** | 🏗️ Entender arquitetura |
| **EXAMPLES.md** | 💡 Ver exemplos de uso |
| **TIPS.md** | 💎 Dicas e otimizações |

---

## ⚡ Início Rápido (Copy & Paste)

### Windows PowerShell

```powershell
# 1. Iniciar Qdrant
docker-compose up -d

# 2. Configurar Backend
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Criar .env (edite depois com sua OpenAI API Key)
@"
OPENAI_API_KEY=sua_chave_aqui
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
"@ | Out-File -FilePath .env -Encoding utf8

# 3. Adicionar PDFs (copie seus PDFs para data/pdfs/)

# 4. Processar PDFs
python run_ingestion.py

# 5. Iniciar Backend (Terminal 1)
uvicorn main:app --reload

# 6. Configurar Frontend (Terminal 2)
cd ..\frontend
npm install
npm run dev
```

### Linux/Mac

```bash
# 1. Iniciar Qdrant
docker-compose up -d

# 2. Configurar Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Criar .env (edite depois com sua OpenAI API Key)
cat > .env << EOF
OPENAI_API_KEY=sua_chave_aqui
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
EOF

# 3. Adicionar PDFs (copie seus PDFs para data/pdfs/)

# 4. Processar PDFs
python run_ingestion.py

# 5. Iniciar Backend (Terminal 1)
uvicorn main:app --reload

# 6. Configurar Frontend (Terminal 2)
cd ../frontend
npm install
npm run dev
```

---

## ✅ Checklist Inicial

Antes de começar, você precisa:

- [ ] **Python 3.9+** instalado
- [ ] **Node.js 18+** instalado  
- [ ] **Docker** instalado (para Qdrant)
- [ ] **OpenAI API Key** (obter em: https://platform.openai.com/api-keys)
- [ ] **PDFs das palestras** para processar

---

## 🆘 Problemas Comuns

### "Docker não encontrado"
- Instale Docker Desktop: https://www.docker.com/products/docker-desktop

### "Python não encontrado"
- Windows: Instale do site oficial ou use Microsoft Store
- Linux: `sudo apt install python3.9 python3.9-venv`
- Mac: `brew install python3`

### "Node não encontrado"
- Instale do site: https://nodejs.org
- Ou use: `brew install node` (Mac)

### "OpenAI API Key inválida"
- Verifique se copiou a chave completa
- Verifique se tem créditos na conta OpenAI
- A chave deve começar com `sk-`

---

## 🎯 Próximos Passos

1. ✅ **Agora**: Siga o `QUICKSTART.md`
2. 📖 **Depois**: Leia `README.md` para entender melhor
3. 🚀 **Quando pronto**: Veja `DEPLOY.md` para produção

---

## 💡 Dica Pro

Se você só quer **testar rapidamente** sem processar PDFs reais:

1. Crie um PDF de teste com algumas páginas de texto
2. Coloque em `data/pdfs/`
3. Execute a ingestão
4. Teste o sistema!

---

**Boa sorte! 🚀**

Se tiver dúvidas, consulte os outros arquivos de documentação.

