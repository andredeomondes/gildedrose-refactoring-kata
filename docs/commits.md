# Gilded Rose - Plano de Commits

## Padrao (baseado nos commits do professor)

```
<tipo>: <descricao> — <tipo/nome-da-branch>
```

## Branch: docs/inicial - Documentacao Inicial

Responsavel: Ryan (commits 1-3) e Andre (commit 4)

| # | Commit | Quem |
|---|--------|------|
| 1 | `docs: analise inicial e compreensao do sistema legado Gilded Rose. — docs/inicial` | Ryan |
| 2 | `docs: diagnostico tecnico com code smells e problemas de design. — docs/inicial` | Ryan |
| 3 | `docs: documento de requisitos funcionais e nao funcionais. — docs/inicial` | Ryan |
| 4 | `docs: plano de contingencia e estrategia de refatoracao. — docs/inicial` | Andre |

## Branch: test/unitario - Testes de Caracterizacao

Responsavel: Lucca

| # | Commit | Quem |
|---|--------|------|
| 1 | `test: importacao do codigo legado original (Item + GildedRose). — test/unitario` | Lucca |
| 2 | `test: testes de caracterizacao para todos os tipos de item. — test/unitario` | Lucca |
| 3 | `test: execucao inicial e registro de evidencias do comportamento original. — test/unitario` | Lucca |

## Branch: refactor/srp - SRP (Strategy Pattern)

Responsavel: Andre

| # | Commit | Quem |
|---|--------|------|
| 1 | `refactor: extracao das regras de qualidade para classes Strategy. — refactor/srp` | Andre |
| 2 | `refactor: finalizacao da separacao de responsabilidades (SRP). — refactor/srp` | Andre |

## Branch: refactor/ocp - OCP (Factory Pattern)

Responsavel: Andre

| # | Commit | Quem |
|---|--------|------|
| 1 | `refactor: criacao da fabrica de strategies para suportar OCP. — refactor/ocp` | Andre |

## Branch: refactor/arch - Clean Architecture

Responsavel: Andre

| # | Commit | Quem |
|---|--------|------|
| 1 | `arch: estruturacao das camadas domain/application/infra. — refactor/arch` | Andre |
| 2 | `arch: implementacao do fluxo completo com injecao de dependencias. — refactor/arch` | Andre |

## Branch: feat/conjured - Itens Conjurados

Responsavel: Igor

| # | Commit | Quem |
|---|--------|------|
| 1 | `feat: implementacao da regra de itens Conjurados com degradacao dobrada. — feat/conjured` | Igor |
| 2 | `feat: testes especificos para itens Conjurados e casos de borda. — feat/conjured` | Igor |

## Branch: docs/final - Documentacao Final

Responsavel: Lucca (commit 1), Ryan (commit 2), Igor (commit 3)

| # | Commit | Quem |
|---|--------|------|
| 1 | `docs: evidencias de execucao com logs e cobertura de testes. — docs/final` | Lucca |
| 2 | `docs: README tecnico com instrucoes e estrutura. — docs/final` | Ryan |
| 3 | `docs: apresentacao final com slides. — docs/final` | Igor |
