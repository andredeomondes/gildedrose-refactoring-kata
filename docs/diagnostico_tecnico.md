# Diagnóstico Técnico — Gilded Rose

## Problemas Identificados no Código Legado

### 1. God Class / Falta de SRP
O método `update_quality` centraliza todas as regras de negócio em um único lugar, violando o **Princípio da Responsabilidade Única (SRP)**.

### 2. Condicionais Aninhadas Complexas
Múltiplos `if` aninhados dificultam a leitura e manutenção do código.

### 3. Nomes pouco claros
Uso de variáveis como `i` e strings mágicas espalhadas.

### 4. Baixa testabilidade
Lógica acoplada impossibilita testar regras isoladamente.

### 5. Violação do OCP
Para adicionar um novo tipo de item (ex: Conjured), é necessário modificar o método existente.

### 6. Duplicação de código
Regras de limite de qualidade (max 50) repetidas em múltiplos lugares.

_(Preencher com análise detalhada da equipe)_
