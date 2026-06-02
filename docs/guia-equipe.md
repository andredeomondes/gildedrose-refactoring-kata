# Guia da Equipe - Projeto Gilded Rose

## O Projeto

Gilded Rose - sistema legado de estoque de uma pousada que precisa ser refatorado aplicando SOLID, Clean Architecture, testes pytest, e adicionando suporte a itens Conjurados.

Repositorio: https://github.com/andredeomondes/gildedrose-refactoring-kata.git

---

## Tarefas de cada um

### ANDRE DEOMONDES - Arquiteto / Lider

O que fazer:
1. Preencher `docs/plano_contingencia.md` com riscos e estrategia
2. Refatorar codigo aplicando SRP (branch `refactor/srp`)
3. Refatorar codigo aplicando OCP (branch `refactor/ocp`)
4. Refatorar codigo para Clean Architecture (branch `refactor/arch`)

Passo a passo:
```bash
git checkout docs/inicial
# editar docs/plano_contingencia.md, depois:
git add docs/plano_contingencia.md
git commit -m "docs: plano de contingencia e estrategia de refatoracao. -- docs/inicial"
git push origin docs/inicial

# depois do merge, criar proximas branches:
git checkout main
git pull origin main
git checkout -b refactor/srp
# codificar strategies...
git add -A
git commit -m "refactor: extracao das regras de qualidade para classes Strategy. -- refactor/srp"
git push origin refactor/srp
# continuar nas branches refactor/ocp e refactor/arch
```

Commits que Andre faz:
| Commit | Branch |
|--------|--------|
| `docs: plano de contingencia e estrategia de refatoracao. -- docs/inicial` | docs/inicial |
| `refactor: extracao das regras de qualidade para classes Strategy. -- refactor/srp` | refactor/srp |
| `refactor: finalizacao da separacao de responsabilidades (SRP). -- refactor/srp` | refactor/srp |
| `refactor: criacao da fabrica de strategies para suportar OCP. -- refactor/ocp` | refactor/ocp |
| `arch: estruturacao das camadas domain/application/infra. -- refactor/arch` | refactor/arch |
| `arch: implementacao do fluxo completo com injecao de dependencias. -- refactor/arch` | refactor/arch |

---

### LUCCA SILVANI - Qualidade / Testes

O que fazer:
1. Criar testes de caracterizacao no codigo original (branch `test/unitario`)
2. Preencher `docs/evidencias_testes.md` com logs e resultados (branch `docs/final`)

Passo a passo:
```bash
git checkout main
git pull origin main
git checkout -b test/unitario
# criar/editar testes em tests/test_gilded_rose.py
git add -A
git commit -m "test: importacao do codigo legado original (Item + GildedRose). -- test/unitario"
# continuar...
git push origin test/unitario
```

Commits que Lucca faz:
| Commit | Branch |
|--------|--------|
| `test: importacao do codigo legado original (Item + GildedRose). -- test/unitario` | test/unitario |
| `test: testes de caracterizacao para todos os tipos de item. -- test/unitario` | test/unitario |
| `test: execucao inicial e registro de evidencias do comportamento original. -- test/unitario` | test/unitario |
| `docs: evidencias de execucao com logs e cobertura de testes. -- docs/final` | docs/final |

---

### RYAN LUIGI - Documentacao

O que fazer:
1. Preencher `docs/diagnostico_tecnico.md` com analise de code smells
2. Preencher `docs/requisitos.md` com RFs e RNFs
3. Escrever `README.md` final com instrucoes (branch `docs/final`)

Passo a passo:
```bash
git checkout main
git pull origin main
git checkout -b docs/inicial
# editar docs/diagnostico_tecnico.md
git add docs/diagnostico_tecnico.md
git commit -m "docs: diagnostico tecnico com code smells e problemas de design. -- docs/inicial"
# editar docs/requisitos.md
git add docs/requisitos.md
git commit -m "docs: documento de requisitos funcionais e nao funcionais. -- docs/inicial"
git push origin docs/inicial
```

Commits que Ryan faz:
| Commit | Branch |
|--------|--------|
| `docs: analise inicial e compreensao do sistema legado Gilded Rose. -- docs/inicial` | docs/inicial |
| `docs: diagnostico tecnico com code smells e problemas de design. -- docs/inicial` | docs/inicial |
| `docs: documento de requisitos funcionais e nao funcionais. -- docs/inicial` | docs/inicial |
| `docs: README tecnico com instrucoes e estrutura. -- docs/final` | docs/final |

---

### IGOR LIMA - Implementacao / Apresentacao

O que fazer:
1. Implementar regra dos itens Conjurados (branch `feat/conjured`)
2. Criar testes para Conjured
3. Preparar slides da apresentacao (branch `docs/final`)

Passo a passo:
```bash
git checkout main
git pull origin main
git checkout -b feat/conjured
# implementar ConjuredStrategy em src/
git add -A
git commit -m "feat: implementacao da regra de itens Conjurados com degradacao dobrada. -- feat/conjured"
# adicionar testes
git add tests/
git commit -m "feat: testes especificos para itens Conjurados e casos de borda. -- feat/conjured"
git push origin feat/conjured
```

Commits que Igor faz:
| Commit | Branch |
|--------|--------|
| `feat: implementacao da regra de itens Conjurados com degradacao dobrada. -- feat/conjured` | feat/conjured |
| `feat: testes especificos para itens Conjurados e casos de borda. -- feat/conjured` | feat/conjured |
| `docs: apresentacao final com slides. -- docs/final` | docs/final |

---

## Ordem correta dos merges

1. `docs/inicial` faz merge no `main` (primeiro)
2. `test/unitario` faz merge no `main` (segundo)
3. `refactor/srp` faz merge no `main`
4. `refactor/ocp` faz merge no `main`
5. `refactor/arch` faz merge no `main`
6. `feat/conjured` faz merge no `main`
7. `docs/final` faz merge no `main` (ultimo)

Cada merge so pode acontecer quando a branch anterior ja foi mesclada.

---

## Fluxo de Trabalho

```bash
# clonar repositorio
git clone https://github.com/andredeomondes/gildedrose-refactoring-kata.git
cd gildedrose-refactoring-kata

# criar ambiente virtual (uma vez so)
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install -r requirements.txt

# antes de comecar uma tarefa nova
git checkout main
git pull origin main
git checkout -b <sua-branch>

# depois de fazer as alteracoes
git add -A
git commit -m "tipo: descricao. -- <sua-branch>"
git push origin <sua-branch>

# quando terminar a branch, criar Pull Request no GitHub
```

## Regras

- Nao alterar classe Item (penalidade -2,0)
- Nao alterar propriedade Items na GildedRose (penalidade -2,0)
- Rodar `pytest -v` antes de todo commit
- Commits em portugues, no formato do professor
- Cada branch faz merge em `main` na ordem definida acima
