FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar APENAS requirements primeiro (para cache de layers)
# Isso permite que o Docker reutilize a camada de instalação de dependências
# se o requirements.txt não mudar, economizando muito tempo!
COPY backend/requirements.txt ./requirements.txt

# Instalar dependências Python
# Esta camada será reutilizada se requirements.txt não mudar
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código do backend (esta camada muda com frequência)
# Por isso colocamos DEPOIS da instalação de dependências
COPY backend/ ./

# Expor porta (Railway usa variável PORT)
EXPOSE 8000

# Comando para produção - usar variável PORT do Railway
# Usar formato JSON para evitar problemas com shell
CMD ["sh", "-c", "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000}"]

