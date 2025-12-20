# Product Camp 2025 - Frontend RAG

Frontend moderno e minimalista para consultas RAG sobre as palestras do Product Camp 2025.

## 🚀 Tecnologias

- **Next.js 14** - Framework React
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **Axios** - Cliente HTTP

## 📋 Funcionalidades

- ✅ Chat interface moderna e responsiva
- ✅ Filtro por palestra/PDF específico
- ✅ Exibição de fontes citadas
- ✅ Perguntas sugeridas
- ✅ Design minimalista e performático
- ✅ Totalmente responsivo

## 🛠️ Desenvolvimento Local

### Pré-requisitos

- Node.js 18+ 
- npm ou yarn

### Instalação

```bash
# Instalar dependências
npm install

# Executar em desenvolvimento
npm run dev
```

Acesse: http://localhost:3000

### Variáveis de Ambiente

Crie um arquivo `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Para produção, use a URL do Railway:
```env
NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app
```

## 📦 Build

```bash
# Build para produção
npm run build

# Executar build de produção
npm start
```

## 🚢 Deploy no Vercel

Veja o guia completo em: [DEPLOY_VERCEL.md](../DEPLOY_VERCEL.md)

### Quick Deploy

1. Conecte o repositório no Vercel
2. Configure:
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
3. Adicione variável de ambiente:
   - `NEXT_PUBLIC_API_URL=https://pcamp2025.up.railway.app`
4. Deploy!

## 🎨 Estrutura

```
frontend/
├── app/              # Next.js App Router
│   ├── layout.tsx    # Layout principal
│   ├── page.tsx      # Página inicial
│   └── globals.css   # Estilos globais
├── components/       # Componentes React
│   ├── ChatInterface.tsx
│   ├── ChatMessage.tsx
│   ├── ChatInput.tsx
│   ├── PalestraFilter.tsx
│   ├── SourcesList.tsx
│   └── SuggestedQuestions.tsx
├── services/         # Serviços API
│   └── chatService.ts
└── types/            # TypeScript types
    └── chat.ts
```

## 🔧 Configuração

### API Endpoints

O frontend consome:
- `POST /api/chat` - Enviar pergunta
- `GET /api/palestras` - Listar palestras disponíveis
- `GET /api/health` - Health check

### Filtros

O sistema suporta filtros por:
- `titulo_palestra` - Filtrar por palestra específica
- `palestrante` - Filtrar por palestrante
- `tema` - Filtrar por tema
- `dia` - Filtrar por dia (dia1, dia2)

## 📱 Responsividade

O design é totalmente responsivo:
- **Mobile**: Layout otimizado para telas pequenas
- **Tablet**: Layout adaptado
- **Desktop**: Layout completo

## ⚡ Performance

- Lazy loading de componentes
- Otimização de imagens
- Code splitting automático
- CSS otimizado com Tailwind

## 🐛 Troubleshooting

### Erro de CORS
- Verifique se `CORS_ORIGINS` no backend inclui a URL do frontend

### API não responde
- Verifique se `NEXT_PUBLIC_API_URL` está configurada corretamente
- Verifique se o backend está rodando

### Build falha
- Verifique se todas as dependências estão instaladas
- Limpe o cache: `rm -rf .next node_modules && npm install`

