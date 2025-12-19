# 📁 Organizar e Processar PDFs

## 📂 Estrutura de Diretórios

Os PDFs devem ser organizados em:
```
data/pdfs/
  ├── dia1/     # PDFs do Dia 1
  └── dia2/     # PDFs do Dia 2
```

---

## 🚀 Passo a Passo

### 1. Organizar PDFs Localmente

#### Opção A: Manual (Recomendado)

1. **Criar diretórios** (já criados automaticamente):
   ```powershell
   data\pdfs\dia1\
   data\pdfs\dia2\
   ```

2. **Copiar PDFs do Dia 1**:
   ```powershell
   Copy-Item "C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001\*.pdf" "data\pdfs\dia1\" -Filter "*dia1*"
   # Ou copie manualmente os PDFs do Dia 1
   ```

3. **Copiar PDFs do Dia 2**:
   ```powershell
   Copy-Item "C:\Users\Felipe\Downloads\Apresentações Product Camp-20251219T151033Z-3-001\*.pdf" "data\pdfs\dia2\" -Filter "*dia2*"
   # Ou copie manualmente os PDFs do Dia 2
   ```

#### Opção B: Usar Script

```powershell
.\organize_pdfs.ps1
```

O script listará os PDFs encontrados para você organizar.

---

### 2. Processar PDFs

#### Processar Dia 1:
```bash
cd backend
python process_pdfs.py dia1
```

#### Processar Dia 2:
```bash
cd backend
python process_pdfs.py dia2
```

#### Processar Todos:
```bash
cd backend
python process_pdfs.py all
```

---

### 3. Processar no Railway (Produção)

Após organizar localmente, você precisa fazer upload para o Railway:

#### Opção A: Via Railway CLI

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link ao projeto
railway link

# Upload PDFs (criar volume primeiro no Railway)
# Ou usar git para commit dos PDFs (não recomendado - arquivos grandes)
```

#### Opção B: Via Volume no Railway

1. No Railway, adicione **Volume** ao serviço backend
2. Upload PDFs para o volume
3. Execute ingestão via CLI:
   ```bash
   railway run python backend/process_pdfs.py dia1
   railway run python backend/process_pdfs.py dia2
   ```

#### Opção C: Via Endpoint de Ingestão

Se configurou `INGESTION_API_KEY` e os PDFs estão acessíveis:
```bash
curl -X POST https://seu-app.railway.app/api/ingest \
  -H "X-API-Key: sua-chave-secreta"
```

---

## 📝 Metadados Automáticos

O sistema detecta automaticamente:
- **Dia**: "Dia 1" ou "Dia 2" (baseado no diretório)
- **Título**: Do nome do arquivo
- **Palestrante**: Do nome do arquivo (se seguir formato)
- **Tipo**: keynote, workshop, palestra
- **Tema**: Do nome do arquivo (se disponível)

---

## ✅ Verificar

Após processar, você pode:

1. **Verificar no Qdrant** (se tiver acesso)
2. **Testar API**:
   ```bash
   curl -X POST https://seu-app.railway.app/api/chat \
     -H "Content-Type: application/json" \
     -d '{"question": "Quais palestras foram no Dia 1?", "filters": null}'
   ```

---

## 🎯 Formato Recomendado de Nome

Para melhor organização, nomeie os PDFs assim:
```
Titulo_Palestra_Palestrante_Tipo_Tema.pdf
```

Exemplo:
```
Estrategia_Produto_Joao_Silva_keynote_estrategia.pdf
```

Mas o sistema funciona com qualquer nome!

---

**Organize os PDFs e processe! 🚀**

