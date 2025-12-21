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

# Copiar PDFs para o container
# Railway usa o diretório raiz como contexto, então copiamos de lá
COPY data/ ./data/

# Expor porta (Railway usa variável PORT dinamicamente)
EXPOSE 8000

# Comando para produção
# Railway injeta PORT como variável de ambiente dinamicamente
# Usar shell para expandir variável PORT do Railway
# Bind em 0.0.0.0 para aceitar conexões de qualquer IP (produção)
# --timeout 600: 10 minutos para processamento longo (ingestão de PDFs)
CMD ["sh", "-c", "gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${PORT:-8000} --timeout 600"]

