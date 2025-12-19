# Dicas e Boas Práticas

## 📄 Preparação dos PDFs

### Formato de Nome Recomendado

Para melhor organização, nomeie os PDFs assim:
```
Titulo_Palestra_Palestrante_Tipo_Tema.pdf
```

**Exemplos:**
- `Estrategia_Produto_Joao_Silva_keynote_estrategia.pdf`
- `Metricas_Produto_Maria_Santos_workshop_metricas.pdf`
- `Design_Thinking_Carlos_Oliveira_palestra_design.pdf`

### Estrutura dos PDFs

- **Slides bem formatados**: Facilita a extração de texto
- **Texto legível**: Evite PDFs apenas com imagens
- **Títulos claros**: Ajuda na identificação de seções

## 🔧 Otimizações

### Ajustar Tamanho dos Chunks

No arquivo `backend/ingestion/chunking.py`:
- Aumentar `max_size` para chunks maiores
- Ajustar `overlap` para mais contexto entre chunks

### Ajustar Busca

No arquivo `backend/rag/vector_store.py`:
- Aumentar `top_k` para mais resultados
- Ajustar `score_threshold` para filtrar relevância

### Escolher Modelo LLM

No arquivo `backend/rag/rag_engine.py`:
- `gpt-4-turbo-preview`: Melhor qualidade, mais caro
- `gpt-3.5-turbo`: Mais rápido e econômico

## 🎨 Personalização do Frontend

### Cores

Edite `frontend/tailwind.config.js` para mudar o tema:
```javascript
colors: {
  primary: {
    // Suas cores aqui
  }
}
```

### Perguntas Sugeridas

Edite `frontend/components/SuggestedQuestions.tsx`:
```typescript
const SUGGESTED_QUESTIONS = [
  'Sua pergunta aqui',
  // ...
]
```

## 📊 Monitoramento

### Verificar Qdrant

Acesse: http://localhost:6333/dashboard

### Ver Logs

**Backend:**
```bash
# Logs aparecem no terminal onde o uvicorn está rodando
```

**Frontend:**
```bash
# Logs no console do navegador (F12)
```

## 🐛 Troubleshooting Comum

### "Collection não encontrada"
- Execute o pipeline de ingestão primeiro
- Verifique se o Qdrant está rodando

### "Erro ao gerar embedding"
- Verifique OPENAI_API_KEY
- Verifique créditos da conta OpenAI

### "Respostas genéricas"
- Aumente `top_k` na busca
- Verifique se os PDFs foram processados corretamente
- Ajuste o `score_threshold`

### "Frontend não conecta"
- Verifique se backend está na porta 8000
- Verifique CORS no backend
- Verifique `NEXT_PUBLIC_API_URL` no frontend

## 🚀 Performance

### Para Muitos PDFs

- Processe em lotes
- Use processamento assíncrono
- Considere sharding no Qdrant

### Para Muitos Usuários

- Implemente cache de respostas
- Use rate limiting
- Considere CDN para frontend

## 🔒 Segurança

- Nunca commite `.env` files
- Use variáveis de ambiente em produção
- Configure CORS adequadamente
- Implemente autenticação se necessário

## 📈 Melhorias Futuras

- Histórico de conversas
- Favoritar perguntas
- Exportar conversas
- Busca avançada com múltiplos filtros
- Análise de sentimento
- Sugestões inteligentes de perguntas

