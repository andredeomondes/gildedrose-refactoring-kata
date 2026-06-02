# Documento de Requisitos — Gilded Rose

## Requisitos Funcionais

| Código | Descrição |
|--------|-----------|
| RF01 | Itens comuns devem diminuir quality em 1 e sell_in em 1 a cada dia |
| RF02 | Após a data de venda (sell_in < 0), itens comuns degradam quality 2x mais rápido |
| RF03 | A quality de um item nunca pode ser negativa |
| RF04 | Aged Brie aumenta quality em 1 a cada dia |
| RF05 | Aged Brie aumenta quality em 2 após a data de venda |
| RF06 | A quality nunca pode exceder 50 |
| RF07 | Sulfuras é lendário: não altera sell_in nem quality (quality = 80) |
| RF08 | Backstage Passes aumenta quality em 1 quando sell_in > 10 |
| RF09 | Backstage Passes aumenta quality em 2 quando sell_in <= 10 |
| RF10 | Backstage Passes aumenta quality em 3 quando sell_in <= 5 |
| RF11 | Backstage Passes quality = 0 após a data de venda |
| RF12 | Itens Conjurados degradam quality 2x mais rápido que itens comuns |

## Requisitos Não Funcionais

| Código | Descrição |
|--------|-----------|
| RNF01 | O sistema deve preservar o comportamento existente após refatoração |
| RNF02 | O código deve ser organizado em camadas (Clean Architecture) |
| RNF03 | O código deve seguir princípios SOLID |
| RNF04 | Deve ser possível testar cada regra de negócio isoladamente |
| RNF05 | Novos tipos de item devem ser adicionados sem modificar código existente (OCP) |
| RNF06 | A classe Item não pode ser alterada |
