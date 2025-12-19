FROM node:18-alpine AS builder

WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./

# Instalar dependências
RUN npm ci

# Copiar código
COPY . .

# Build da aplicação
RUN npm run build

# Produção
FROM node:18-alpine

WORKDIR /app

# Copiar apenas arquivos necessários
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

# Expor porta
EXPOSE 3000

# Iniciar aplicação
CMD ["npm", "start"]

