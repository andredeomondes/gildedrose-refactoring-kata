# Gilded Rose — Especificação do Trabalho

---

## Historia do Sistema

Voce foi contratado pela **pousada Gilded Rose**. Somos uma pequena pousada que tambem compra e vende mercadorias. Infelizmente nossos produtos perdem qualidade conforme a data de venda se aproxima.

Temos um sistema legado (criado pelo **Leeroy** — um rapaz sem nocao) que atualiza automaticamente o estoque. Seu trabalho: **refatorar o sistema e adicionar uma nova categoria de itens (Conjurados)**.

### Regras de Negocio

| Item | Comportamento |
|------|---------------|
| **Item comum** | `quality` diminui 1 por dia. Apos `sell_in` passar, diminui **2 por dia**. `quality` nunca negativa |
| **Aged Brie** | `quality` **aumenta** 1 por dia. Apos `sell_in` passar, aumenta **2 por dia**. Max 50 |
| **Sulfuras** | Item lendario. `quality` = 80 (fixo). `sell_in` nao altera |
| **Backstage Passes** | `quality` aumenta: +1 (>10 dias), +2 (<=10 dias), +3 (<=5 dias). **Zera** apos `sell_in` |
| **Conjured** (NOVO) | Degrada **2x mais rapido** que item comum |

### Restricoes (NAO PODE ALTERAR)

- Classe `Item` — pertence ao **Goblin** (penalidade **-2,0**)
- Propriedade `Items` na classe `GildedRose` (penalidade **-2,0**)

---

## Objetivos

O objetivo **nao e so fazer funcionar** — e demonstrar:

- Analise e compreensao de sistema legado
- Planejamento de refatoracao segura
- Aplicacao de **Clean Code, SOLID, modularizacao**
- Uso de **Arquitetura Limpa** (ou hexagonal)
- Testes automatizados (**pytest**)
- Documentacao tecnica (inspirada em MPS.BR)
- evidencias objetivas de funcionamento

---

## Passo a Passo (10 etapas)

| # | Etapa | O que fazer |
|---|-------|-------------|
| 1 | **Ler e compreender** o problema | Entender as regras de cada item |
| 2 | **Executar o sistema original** | Rodar e registrar comportamento ANTES |
| 3 | **Diagnostico tecnico** | Identificar code smells, problemas de design |
| 4 | **Documentar requisitos** | Transformar narrativa em RFs e RNFs |
| 5 | **Plano de contingencia** | Definir riscos, ordem, validacao |
| 6 | **Criar testes de caracterizacao** | Capturar comportamento atual (rede de seguranca) |
| 7 | **Refatoracao incremental** | SRP -> OCP -> Clean Architecture |
| 8 | **Implementar Conjured** | Degradacao 2x mais rapida |
| 9 | **Testes finais e evidencias** | Prints, logs, cobertura |
| 10 | **Preparar entrega** | README, docs finais, apresentacao |

---

## Entregaveis Obrigatorios (8 itens)

### 1. Diagnostico Tecnico (`docs/diagnostico_tecnico.md`) — 1,0 pt
- Identificar code smells, duplicacoes, condicionais complexas
- Explicar por que dificultam manutencao
- Citar trechos do codigo

### 2. Documento de Requisitos (`docs/requisitos.md`) — 1,0 pt
- RFs numerados (RF01, RF02...) para cada regra
- RNFs numerados (RNF01, RNF02...) para atributos de qualidade

### 3. Plano de Contingencia (`docs/plano_contingencia.md`) — 1,0 pt
- Estrategia de refatoracao segura
- Partes que podem vs NAO podem ser alteradas
- Riscos + mitigacoes
- Como os testes reduzem riscos

### 4. Codigo Refatorado (`src/`) — 1,0 pt
- SOLID + Clean Architecture (ou hexagonal)
- NAO alterar `Item` nem `Items`
- Reduzir complexidade, facilitar novas regras
- Conjured implementado corretamente

### 5. Testes Automatizados (`tests/`) — 1,0 pt
- **pytest** obrigatorio
- Cobrir: comum, Aged Brie, Sulfuras, Backstage, Conjured + bordas

### 6. evidencias de Execucao (`docs/evidencias_testes.md`) — 0,5 pt
- Prints/logs antes/depois
- Relatorio de cobertura (se possivel)

### 7. README Tecnico (`README.md`) — 1,0 pt
- Como instalar, executar, testar
- Estrutura de pastas
- Decisoes de refatoracao

### 8. Apresentacao (5-7 min) — 3,0 pt
- Problemas encontrados, estrategia, melhorias, resultados
- Foco na **justificativa tecnica**

---

## Estrutura Recomendada

```
gilded-rose/
├── README.md
├── src/               -> codigo refatorado
├── tests/             -> testes automatizados
├── docs/              -> documentacao
│   ├── guia-equipe.md
│   ├── diagnostico_tecnico.md
│   ├── requisitos.md
│   ├── plano_contingencia.md
│   ├── evidencias_testes.md
│   ├── equipe.md
│   └── commits.md
└── apresentacao/
    └── slides.pdf
```

---

## Barema de Avaliacao (10,0 pts)

| Criterio | Peso | O que espera |
|----------|------|-------------|
| Diagnostico tecnico | **1,0** | Code smells identificados e relacionados ao codigo |
| Documentacao de requisitos | **1,0** | RFs e RNFs numerados e rastreaveis |
| Plano de contingencia | **1,0** | Estrategia, riscos e acoes preventivas |
| Codigo refatorado | **1,0** | Legibilidade, separacao, sem alterar Item/Items |
| Implementacao Conjured | **0,5** | Degradacao dobrada, limites respeitados, com testes |
| Testes automatizados | **1,0** | pytest cobrindo todos os itens + bordas |
| evidencias de execucao | **0,5** | Prints/logs organizados |
| README + organizacao | **1,0** | Instrucoes claras, estrutura documentada |
| Apresentacao e defesa | **3,0** | 5-7 min, comunicacao objetiva |

---

## Penalidades

| Problema | Penalidade |
|----------|-----------|
| Ausencia do Diagnostico Tecnico | **-3,0** |
| Ausencia do Plano de Contingencia | **-3,0** |
| Ausencia de Testes Automatizados | **-3,0** |
| Codigo nao executa | Nota maxima **5,0** |
| Alterar classe `Item` indevidamente | **-2,0** |
| Nao implementar `Conjured` corretamente | **-2,0** |

---

## Dependencia entre Entregaveis

As etapas sao **cumulativas**. Se a equipe pular uma etapa inicial, as seguintes ficam comprometidas. A ausencia de qualquer entregavel obrigatorio gera penalidade.

---

## Dicas Finais

- Prefiram **refatoracoes pequenas e progressivas**
- Criem **testes ANTES** de mudar o codigo
- Nao copiem solucao pronta — o professor avalia o **dominio da equipe**
- Expliquem as decisoes tecnicas mesmo quando parecer simples
- Valorizem clareza, organizacao e preservacao de comportamento
