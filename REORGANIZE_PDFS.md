# 📁 Reorganizar PDFs: Dia 1 (4 PDFs) e Dia 2 (6 PDFs)

## 📋 Lista de PDFs Disponíveis

1. `10_00 - Meli - Landing page Fashion.pptx.pdf`
2. `10_00 - Vibra Energia.pptx.pdf`
3. `10_55 - Stone.pptx.pdf`
4. `11_10 - Sem parar .pptx.pdf`
5. `13_35 Globoplay .pptx.pdf`
6. `13_50 - BrazeAI Decisioning Impulsionando Receita - Product Camp.pptx.pdf`
7. `14_30 - Mercado Livre.pptx.pdf`
8. `16_10 - Recargapay - De Wallet a Plataforma de Investimentos.pdf`
9. `17_05 - Amplitude .pptx.pdf`
10. `Palestra  Minders Menos atrito, mais dados como reestruturamos a criac~ao de conta em uma Fintech.pdf`

---

## 🎯 Como Reorganizar

### Opção 1: Script com Parâmetros

Execute o script informando quais PDFs vão para Dia 1:

```powershell
# Exemplo: PDFs 1, 2, 3, 4 para Dia 1
.\reorganize_pdfs_param.ps1 "1,2,3,4"

# Ou outros números, por exemplo: 1, 3, 5, 7
.\reorganize_pdfs_param.ps1 "1,3,5,7"
```

### Opção 2: Manual

1. **Limpar diretórios atuais:**
   ```powershell
   Remove-Item "data\pdfs\dia1\*" -Force
   Remove-Item "data\pdfs\dia2\*" -Force
   ```

2. **Copiar manualmente:**
   ```powershell
   # Exemplo: Copiar PDFs 1, 2, 3, 4 para Dia 1
   Copy-Item "data\pdfs\temp\10_00 - Meli*.pdf" "data\pdfs\dia1\" -Force
   Copy-Item "data\pdfs\temp\10_00 - Vibra*.pdf" "data\pdfs\dia1\" -Force
   # ... etc
   ```

---

## 💡 Sugestão de Organização

Baseado nos horários, uma possível organização:

### Dia 1 (4 PDFs - Manhã):
- 1. 10_00 - Meli
- 2. 10_00 - Vibra Energia
- 3. 10_55 - Stone
- 4. 11_10 - Sem parar

### Dia 2 (6 PDFs - Restantes):
- 5. 13_35 - Globoplay
- 6. 13_50 - BrazeAI
- 7. 14_30 - Mercado Livre
- 8. 16_10 - Recargapay
- 9. 17_05 - Amplitude
- 10. Palestra Minders

---

## 🚀 Executar

**Qual organização você prefere?**

Informe quais 4 PDFs devem ir para Dia 1, e eu executo o script!

Exemplo: "Dia 1: 1,2,3,4" ou "Dia 1: 1,3,5,7"

