# Pipeline de Ingestão

Este módulo é responsável por processar os PDFs das palestras e armazená-los no Qdrant.

## Como Usar

1. Coloque os PDFs no diretório `data/pdfs/`

2. Execute o pipeline:
   ```bash
   cd backend
   python -m ingestion.ingestion_pipeline
   ```

## O que o Pipeline Faz

1. **Lê todos os PDFs** do diretório `data/pdfs/`
2. **Extrai texto** de cada página usando `pdfplumber`
3. **Divide em chunks** semânticos (preferencialmente por slide)
4. **Gera embeddings** usando OpenAI text-embedding-ada-002
5. **Armazena no Qdrant** com metadados completos

## Metadados Armazenados

Cada chunk armazena:
- `titulo_palestra`: Título da palestra
- `palestrante`: Nome do palestrante
- `tipo`: Tipo (keynote, workshop, palestra)
- `tema`: Tema/trilha (opcional)
- `pagina_ou_slide`: Número da página ou slide
- `fonte`: "Product Camp 2025"
- `text`: Texto do chunk

## Formato de Nome dos PDFs

Para melhor organização, nomeie os PDFs assim:
```
Titulo_Palestra_Palestrante_Tipo_Tema.pdf
```

Exemplo:
```
Estrategia_Produto_Joao_Silva_keynote_estrategia.pdf
```

Se não seguir esse formato, o sistema tentará inferir ou usará valores padrão.

## Troubleshooting

- **Erro ao conectar ao Qdrant**: Verifique se o Qdrant está rodando
- **Erro ao gerar embeddings**: Verifique se OPENAI_API_KEY está configurada
- **PDFs não processados**: Verifique se os arquivos estão em `data/pdfs/` e são PDFs válidos

