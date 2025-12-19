# 📁 Instruções para Organizar PDFs

## ✅ PDFs Copiados

10 PDFs foram copiados para: `data\pdfs\temp`

## 📋 Lista de PDFs Encontrados:

1. `10_00 - Meli - Landing page Fashion.pptx.pdf`
2. `11_10 - Sem parar .pptx.pdf`
3. `13_50 - BrazeAI Decisioning Impulsionando Receita - Product Camp.pptx.pdf`
4. `Palestra  Minders Menos atrito, mais dados como reestruturamos a criac~ao de conta em uma Fintech.pdf`
5. `10_00 - Vibra Energia.pptx.pdf`
6. `10_55 - Stone.pptx.pdf`
7. `13_35 Globoplay .pptx.pdf`
8. `14_30 - Mercado Livre.pptx.pdf`
9. `16_10 - Recargapay - De Wallet a Plataforma de Investimentos.pdf`
10. `17_05 - Amplitude .pptx.pdf`

---

## 🎯 Organizar por Horário

Baseado nos horários nos nomes, podemos organizar:

### Dia 1 (manhã/tarde):
- 10_00 - Meli
- 10_00 - Vibra Energia  
- 10_55 - Stone
- 11_10 - Sem parar
- 13_35 - Globoplay
- 13_50 - BrazeAI
- 14_30 - Mercado Livre

### Dia 2 (tarde):
- 16_10 - Recargapay
- 17_05 - Amplitude
- Palestra Minders (sem horário - precisa identificar)

---

## 🚀 Comandos para Organizar

### Opção 1: Automático (baseado em horário)

```powershell
# Dia 1 (horários até 14:30)
Get-ChildItem "data\pdfs\temp" | Where-Object { 
    $_.Name -match "10_00|10_55|11_10|13_35|13_50|14_30" 
} | Copy-Item -Destination "data\pdfs\dia1\" -Force

# Dia 2 (horários 16:10 e 17:05)
Get-ChildItem "data\pdfs\temp" | Where-Object { 
    $_.Name -match "16_10|17_05" 
} | Copy-Item -Destination "data\pdfs\dia2\" -Force

# Minders (sem horário - copiar manualmente ou para dia1)
Copy-Item "data\pdfs\temp\*Minders*" -Destination "data\pdfs\dia1\" -Force
```

### Opção 2: Manual

1. Abra o Explorer
2. Vá para: `data\pdfs\temp`
3. Copie os PDFs do Dia 1 para: `data\pdfs\dia1\`
4. Copie os PDFs do Dia 2 para: `data\pdfs\dia2\`

---

## ✅ Após Organizar

Processe os PDFs:

```bash
cd backend
python process_pdfs.py dia1
python process_pdfs.py dia2
```

---

**Organize os PDFs e depois processe!** 🚀

