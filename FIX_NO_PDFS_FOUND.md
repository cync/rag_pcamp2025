# 🔧 Corrigir: Nenhum PDF Encontrado

## 🔴 Problema Identificado

Os logs mostram:
```
Encontrados 0 arquivos PDF
Nenhum PDF encontrado no diretório!
```

Isso significa que os **PDFs não estão acessíveis** no container do Railway.

---

## ✅ Soluções

### Opção 1: PDFs no Git (Recomendado se PDFs são pequenos)

Se os PDFs estão no diretório `data/pdfs/` localmente:

1. **Verifique se estão no Git:**
   ```powershell
   git status
   git ls-files data/pdfs/
   ```

2. **Se não estiverem, adicione:**
   ```powershell
   git add data/pdfs/
   git commit -m "Add PDFs for processing"
   git push
   ```

3. **Railway fará deploy automático** e os PDFs estarão disponíveis

**⚠️ Limitação**: Git não é ideal para arquivos grandes (>100MB). Use Volume se os PDFs forem grandes.

---

### Opção 2: Via Volume no Railway (Recomendado para PDFs grandes)

1. **No Railway Dashboard:**
   - Abra seu projeto → Serviço Backend
   - Vá em **Settings** → **Volumes**
   - Clique em **+ New Volume**
   - Crie um volume (ex: `pdfs-volume`)

2. **Montar o Volume:**
   - No volume criado, configure o **Mount Path**: `/app/data/pdfs`
   - Isso fará o volume aparecer em `/app/data/pdfs` no container

3. **Upload dos PDFs:**
   - Use Railway CLI para fazer upload:
     ```powershell
     railway run bash
     # Dentro do container, você pode fazer upload via curl ou wget
     ```

   **Ou** use um serviço de storage (S3, etc.) e baixe no container durante o build.

---

### Opção 3: Via Railway CLI (Upload Manual)

1. **Instalar Railway CLI** (se ainda não tem):
   ```powershell
   npm install -g @railway/cli
   ```

2. **Login e Link:**
   ```powershell
   railway login
   railway link
   ```

3. **Upload PDFs:**
   ```powershell
   # Copiar PDFs para o container
   railway run bash
   # Dentro do container:
   mkdir -p /app/data/pdfs/dia1
   mkdir -p /app/data/pdfs/dia2
   # Use scp ou outro método para copiar os PDFs
   ```

---

### Opção 4: Modificar Build para Baixar PDFs

Se os PDFs estão em um storage externo (S3, Google Drive, etc.):

1. **Adicione código no Dockerfile** para baixar durante o build:
   ```dockerfile
   # Adicionar antes do CMD
   RUN mkdir -p /app/data/pdfs/dia1 /app/data/pdfs/dia2
   # Adicionar comandos para baixar PDFs (curl, wget, etc.)
   ```

2. **Ou adicione no código Python** para baixar na inicialização

---

## 🔍 Verificar Onde os PDFs Devem Estar

O código procura PDFs em:
- `data/pdfs/dia1/` (4 PDFs)
- `data/pdfs/dia2/` (6 PDFs)

No container Railway, o caminho completo é:
- `/app/data/pdfs/dia1/`
- `/app/data/pdfs/dia2/`

---

## ✅ Após Adicionar PDFs

1. **Se usou Git**: Railway fará deploy automático
2. **Se usou Volume**: Reinicie o serviço ou execute ingestão novamente
3. **Execute processamento novamente:**
   ```powershell
   .\process_net.ps1
   ```

---

## 📝 Checklist

- [ ] PDFs estão no Git? (verifique com `git ls-files data/pdfs/`)
- [ ] PDFs estão em um Volume no Railway?
- [ ] PDFs podem ser baixados durante o build?
- [ ] Caminho correto: `/app/data/pdfs/dia1/` e `/app/data/pdfs/dia2/`

---

**Escolha uma das opções acima e adicione os PDFs ao Railway! 📄**

