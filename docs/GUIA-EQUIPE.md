# Guia da Equipe — Projeto Gilded Rose

## 📋 O Projeto

**Gilded Rose** — sistema legado de estoque de uma pousada que precisa ser refatorado aplicando **SOLID**, **Clean Architecture**, **testes pytest**, e adicionando suporte a **itens Conjurados**.

## 👥 Time e Tarefas

| Membro | Função | Entregáveis | Peso |
|--------|--------|-------------|------|
| **ANDRE DEOMONDES** | Arquiteto / Líder | Plano de contingência + Código refatorado (SOLID + Arch) | 2,0 |
| **LUCCA SILVANI** | Qualidade / Testes | Testes automatizados + Evidências de execução | 1,5 |
| **RYAN LUIGI** | Documentação | Diagnóstico técnico + Documento de requisitos + README | 3,0 |
| **IGOR LIMA** | Implementação / Apresentação | Implementação Conjured + Apresentação final | 3,5 |

## 🔄 Git Flow — Branches e Commits

### Padrão do Professor (usar igual)

```
<tipo: descrição do que foi feito> — <tipo/nome-da-branch>
```

### Branch: `docs/inicial` — Documentação Inicial

**Criação:** `git checkout -b docs/inicial`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `docs: análise inicial e compreensão do sistema legado Gilded Rose. — docs/inicial` | Ryan |
| 2 | `docs: diagnóstico técnico com code smells e problemas de design. — docs/inicial` | Ryan |
| 3 | `docs: documento de requisitos funcionais e não funcionais. — docs/inicial` | Ryan |
| 4 | `docs: plano de contingência e estratégia de refatoração. — docs/inicial` | André |

**Merge:** `main` ← `docs/inicial`

### Branch: `test/unitario` — Testes de Caracterização

**Criação:** `git checkout -b test/unitario`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `test: importação do código legado original (Item + GildedRose). — test/unitario` | Lucca |
| 2 | `test: testes de caracterização para todos os tipos de item. — test/unitario` | Lucca |
| 3 | `test: execução inicial e registro de evidências do comportamento original. — test/unitario` | Lucca |

**Merge:** `main` ← `test/unitario`

### Branch: `refactor/srp` — SRP (Strategy Pattern)

**Criação:** `git checkout -b refactor/srp main`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `refactor: extração das regras de qualidade para classes Strategy. — refactor/srp` | André |
| 2 | `refactor: finalização da separação de responsabilidades (SRP). — refactor/srp` | André |

**Merge:** `main` ← `refactor/srp`

### Branch: `refactor/ocp` — OCP (Factory Pattern)

**Criação:** `git checkout -b refactor/ocp main`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `refactor: criação da fábrica de strategies para suportar OCP. — refactor/ocp` | André |

**Merge:** `main` ← `refactor/ocp`

### Branch: `refactor/arch` — Clean Architecture

**Criação:** `git checkout -b refactor/arch main`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `arch: estruturação das camadas domain/application/infra. — refactor/arch` | André |
| 2 | `arch: implementação do fluxo completo com injeção de dependências. — refactor/arch` | André |

**Merge:** `main` ← `refactor/arch`

### Branch: `feat/conjured` — Itens Conjurados

**Criação:** `git checkout -b feat/conjured main`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `feat: implementação da regra de itens Conjurados com degradação dobrada. — feat/conjured` | Igor |
| 2 | `feat: testes específicos para itens Conjurados e casos de borda. — feat/conjured` | Igor |

**Merge:** `main` ← `feat/conjured`

### Branch: `docs/final` — Documentação Final

**Criação:** `git checkout -b docs/final main`

| # | Commit | Responsável |
|---|--------|-------------|
| 1 | `docs: evidências de execução com logs e cobertura de testes. — docs/final` | Lucca |
| 2 | `docs: README técnico com instruções e estrutura. — docs/final` | Ryan |
| 3 | `docs: apresentação final com slides. — docs/final` | Igor |

**Merge:** `main` ← `docs/final`

## 📁 Estrutura Final do Projeto

```
gilded-rose/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── item.py                    ← NÃO ALTERAR
│   ├── gilded_rose.py             ← código original (NÃO ALTERAR Items)
│   ├── main.py                    ← ponto de entrada
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── strategies/
│   │       ├── __init__.py
│   │       ├── base.py            ← QualityStrategy (ABC)
│   │       ├── normal.py
│   │       ├── aged_brie.py
│   │       ├── sulfuras.py
│   │       ├── backstage_pass.py
│   │       └── conjured.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── gilded_rose.py
│   │   └── factory.py
│   └── infra/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_gilded_rose.py
├── docs/
│   ├── GUIA-EQUIPE.md
│   ├── equipe.md
│   ├── commits.md
│   ├── trabalho.md
│   ├── diagnostico_tecnico.md
│   ├── requisitos.md
│   ├── plano_contingencia.md
│   └── evidencias_testes.md
└── apresentacao/
    └── slides.pdf
```

## 🚫 Regras de Ouro

| Regra | Penalidade |
|-------|-----------|
| NÃO alterar classe `Item` | **-2,0** |
| NÃO alterar `Items` na `GildedRose` | **-2,0** |
| NÃO entregar diagnóstico | **-3,0** |
| NÃO entregar plano de contingência | **-3,0** |
| NÃO entregar testes automatizados | **-3,0** |
| Código não executar | Nota máxima **5,0** |
| Conjured incorreto | **-2,0** |

## 🧪 Comandos Úteis

```bash
git checkout -b <nome-da-branch>   # criar branch nova
git add .                          # preparar arquivos
git commit -m "msg"                # commitar
git push origin <branch>           # subir pro GitHub

pytest -v                          # rodar testes
pytest --cov=src tests/            # cobertura
```

## 🚀 Para Começar

```bash
git clone <url-do-repositorio> gilded-rose
cd gilded-rose
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
pytest -v
```
