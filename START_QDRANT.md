# 🐳 Iniciar Qdrant - Instruções

## ⚠️ Qdrant não está rodando

O processamento precisa do Qdrant rodando. Você tem duas opções:

---

## Opção 1: Docker Desktop (Recomendado)

### 1. Instalar Docker Desktop

Se não tiver instalado:
- Download: https://www.docker.com/products/docker-desktop
- Instale e reinicie o computador
- Inicie o Docker Desktop

### 2. Iniciar Qdrant

```powershell
docker-compose up -d
```

### 3. Verificar

```powershell
docker ps
```

Deve mostrar o container qdrant rodando.

---

## Opção 2: Processar no Railway (Sem Docker Local)

Se não quiser instalar Docker localmente, você pode:

1. **Processar diretamente no Railway** após fazer upload dos PDFs
2. **Usar Qdrant Cloud** (serviço gerenciado)

---

## Opção 3: Instalação Manual do Qdrant

Siga as instruções em:
https://qdrant.tech/documentation/guides/installation/

---

## ✅ Após Qdrant Rodando

Execute novamente:

```powershell
cd backend
.\venv\Scripts\python.exe run_ingestion_dia.py dia1
.\venv\Scripts\python.exe run_ingestion_dia.py dia2
```

---

**Instale o Docker Desktop e inicie o Qdrant para processar os PDFs! 🐳**

