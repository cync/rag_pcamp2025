# 🚀 Guia Completo de Deploy

## 📋 Índice

1. [Desenvolvimento Local](#desenvolvimento-local)
2. [Deploy em Produção](#deploy-em-produção)
   - [Opção 1: VPS/Cloud (Recomendado)](#opção-1-vpscloud-recomendado)
   - [Opção 2: Docker Compose](#opção-2-docker-compose)
   - [Opção 3: Serviços Gerenciados](#opção-3-serviços-gerenciados)

---

## 🏠 Desenvolvimento Local

### Passo 1: Verificar Pré-requisitos

```bash
# Verificar Python (3.9+)
python --version

# Verificar Node.js (18+)
node --version

# Verificar Docker (para Qdrant)
docker --version
```

### Passo 2: Clonar/Preparar Projeto

```bash
# Se ainda não tem o projeto, navegue até a pasta
cd PCAMP2025_RAG
```

### Passo 3: Iniciar Qdrant

```bash
# Iniciar Qdrant com Docker
docker-compose up -d

# Verificar se está rodando
docker ps
# Deve ver o container qdrant rodando
```

### Passo 4: Configurar Backend

```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Criar arquivo .env
# Windows PowerShell:
New-Item -Path .env -ItemType File
# Linux/Mac:
touch .env
```

**Editar `.env` com:**
```env
OPENAI_API_KEY=sk-sua-chave-openai-aqui
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=development
LOG_LEVEL=INFO
```

> 💡 **Obter OpenAI API Key**: https://platform.openai.com/api-keys

### Passo 5: Adicionar PDFs

```bash
# Criar diretório se não existir
mkdir -p ..\data\pdfs

# Copiar seus PDFs para data/pdfs/
# Exemplo:
# copy C:\caminho\para\palestras\*.pdf ..\data\pdfs\
```

### Passo 6: Processar PDFs (Ingestão)

```bash
# Ainda no diretório backend
python run_ingestion.py
```

Você deve ver logs como:
```
Iniciando pipeline de ingestão de PDFs
Encontrados X arquivos PDF
Processando: data/pdfs/palestra1.pdf
  → Y chunks criados
✓ Processado com sucesso
```

### Passo 7: Configurar Frontend

```bash
cd ..\frontend

# Instalar dependências
npm install

# Criar arquivo .env.local (opcional, padrão já funciona)
# Windows PowerShell:
New-Item -Path .env.local -ItemType File
# Linux/Mac:
touch .env.local
```

**Editar `.env.local` (opcional):**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Passo 8: Iniciar Servidores

**Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\Activate.ps1  # ou activate.bat no CMD
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Passo 9: Testar

1. Acesse: http://localhost:3000
2. Faça uma pergunta de teste
3. Verifique se recebe resposta com fontes

**Verificações:**
- Backend: http://localhost:8000/api/health
- API Docs: http://localhost:8000/docs
- Qdrant: http://localhost:6333/dashboard

---

## 🌐 Deploy em Produção

### Opção 1: VPS/Cloud (Recomendado)

#### Serviços Recomendados:
- **DigitalOcean**: https://www.digitalocean.com
- **Linode**: https://www.linode.com
- **AWS EC2**: https://aws.amazon.com/ec2
- **Google Cloud**: https://cloud.google.com
- **Azure**: https://azure.microsoft.com

#### Passo a Passo:

**1. Provisionar Servidor**
- Ubuntu 22.04 LTS
- Mínimo: 2GB RAM, 2 vCPU
- Recomendado: 4GB RAM, 4 vCPU

**2. Conectar ao Servidor**
```bash
ssh root@seu-servidor-ip
```

**3. Instalar Dependências**
```bash
# Atualizar sistema
apt update && apt upgrade -y

# Instalar Python
apt install python3.9 python3.9-venv python3-pip -y

# Instalar Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Instalar Nginx (para reverse proxy)
apt install nginx -y
```

**4. Clonar/Upload Projeto**
```bash
# Opção A: Git
git clone seu-repositorio.git
cd PCAMP2025_RAG

# Opção B: Upload via SCP
# No seu computador local:
scp -r PCAMP2025_RAG root@seu-servidor-ip:/opt/
ssh root@seu-servidor-ip
cd /opt/PCAMP2025_RAG
```

**5. Configurar Qdrant**
```bash
# Criar docker-compose para produção
cat > docker-compose.prod.yml << EOF
version: '3.8'
services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "127.0.0.1:6333:6333"
      - "127.0.0.1:6334:6334"
    volumes:
      - qdrant_storage:/qdrant/storage
    restart: always
volumes:
  qdrant_storage:
EOF

# Iniciar Qdrant
docker-compose -f docker-compose.prod.yml up -d
```

**6. Configurar Backend**
```bash
cd backend

# Criar ambiente virtual
python3.9 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
pip install gunicorn  # Servidor de produção

# Criar .env
nano .env
```

**`.env` de produção:**
```env
OPENAI_API_KEY=sua-chave-openai
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=product_camp_2025
ENVIRONMENT=production
LOG_LEVEL=INFO
```

**7. Processar PDFs**
```bash
# Upload PDFs para data/pdfs/
# Depois executar:
python run_ingestion.py
```

**8. Criar Systemd Service para Backend**
```bash
sudo nano /etc/systemd/system/pcamp-rag-api.service
```

**Conteúdo:**
```ini
[Unit]
Description=Product Camp 2025 RAG API
After=network.target

[Service]
User=root
WorkingDirectory=/opt/PCAMP2025_RAG/backend
Environment="PATH=/opt/PCAMP2025_RAG/backend/venv/bin"
ExecStart=/opt/PCAMP2025_RAG/backend/venv/bin/gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

**Ativar serviço:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable pcamp-rag-api
sudo systemctl start pcamp-rag-api
sudo systemctl status pcamp-rag-api
```

**9. Build Frontend**
```bash
cd /opt/PCAMP2025_RAG/frontend

# Instalar dependências
npm install

# Build para produção
npm run build

# Instalar PM2 (gerenciador de processos)
npm install -g pm2

# Iniciar com PM2
pm2 start npm --name "pcamp-rag-frontend" -- start
pm2 save
pm2 startup
```

**10. Configurar Nginx**
```bash
sudo nano /etc/nginx/sites-available/pcamp-rag
```

**Configuração:**
```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Ativar site:**
```bash
sudo ln -s /etc/nginx/sites-available/pcamp-rag /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**11. Configurar SSL (Let's Encrypt)**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d seu-dominio.com
```

**12. Configurar Firewall**
```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

---

### Opção 2: Docker Compose (Tudo em Containers)

Criar `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "127.0.0.1:6333:6333"
    volumes:
      - qdrant_storage:/qdrant/storage
    restart: always

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "127.0.0.1:8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - QDRANT_HOST=qdrant
      - QDRANT_PORT=6333
    depends_on:
      - qdrant
    restart: always
    volumes:
      - ./data:/app/data

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "127.0.0.1:3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    depends_on:
      - backend
    restart: always

volumes:
  qdrant_storage:
```

**Dockerfiles necessários** (criar depois se escolher esta opção)

---

### Opção 3: Serviços Gerenciados

#### Backend: Railway / Render / Fly.io
- Upload código
- Configurar variáveis de ambiente
- Deploy automático

#### Frontend: Vercel / Netlify
- Conectar repositório Git
- Build automático
- Deploy instantâneo

#### Qdrant: Qdrant Cloud
- Serviço gerenciado
- https://cloud.qdrant.io

---

## ✅ Checklist de Deploy

### Antes do Deploy
- [ ] Testado localmente
- [ ] PDFs processados
- [ ] Variáveis de ambiente configuradas
- [ ] Domínio configurado (se aplicável)
- [ ] SSL configurado
- [ ] Firewall configurado

### Após Deploy
- [ ] Backend respondendo: `curl https://seu-dominio.com/api/health`
- [ ] Frontend acessível
- [ ] Qdrant funcionando
- [ ] Teste de pergunta funcionando
- [ ] Logs sendo gerados
- [ ] Monitoramento configurado

---

## 🔧 Comandos Úteis

### Verificar Status
```bash
# Backend
sudo systemctl status pcamp-rag-api
sudo journalctl -u pcamp-rag-api -f

# Frontend
pm2 status
pm2 logs pcamp-rag-frontend

# Qdrant
docker ps
docker logs qdrant
```

### Reiniciar Serviços
```bash
# Backend
sudo systemctl restart pcamp-rag-api

# Frontend
pm2 restart pcamp-rag-frontend

# Qdrant
docker-compose restart qdrant
```

### Atualizar Código
```bash
# Pull novo código
git pull

# Backend
cd backend
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart pcamp-rag-api

# Frontend
cd frontend
npm install
npm run build
pm2 restart pcamp-rag-frontend
```

---

## 🆘 Troubleshooting

### Backend não inicia
```bash
# Ver logs
sudo journalctl -u pcamp-rag-api -n 50

# Verificar porta
sudo netstat -tulpn | grep 8000

# Testar manualmente
cd backend
source venv/bin/activate
python -m uvicorn main:app
```

### Frontend não conecta ao backend
- Verificar `NEXT_PUBLIC_API_URL`
- Verificar CORS no backend
- Verificar firewall

### Qdrant não conecta
```bash
# Verificar container
docker ps
docker logs qdrant

# Testar conexão
curl http://localhost:6333/health
```

---

## 📊 Monitoramento Recomendado

- **Uptime**: UptimeRobot / Pingdom
- **Logs**: CloudWatch / Papertrail
- **Métricas**: Prometheus + Grafana
- **Alertas**: Email / Slack

---

**Pronto para deploy! 🚀**

