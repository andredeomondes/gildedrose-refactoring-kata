# Gilded Rose - Modernizacao de Sistema Legado

Refatoracao do sistema Gilded Rose aplicando SOLID, Clean Architecture, testes automatizados e adicionando suporte a itens Conjurados.

## Primeiros Passos

### 1. Clonar o repositorio

```bash
git clone https://github.com/andredeomondes/gildedrose-refactoring-kata.git
cd gildedrose-refactoring-kata
```

### 2. Criar e ativar ambiente virtual

No Windows (PowerShell, CMD, Git Bash):
```bash
python -m venv venv
.\venv\Scripts\Activate
```

No Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal mostra `(venv)` no inicio da linha.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

```bash
python -m src.main
```

### 5. Rodar os testes

```bash
pytest -v
```

Para ver cobertura dos testes:
```bash
pip install pytest-cov
pytest --cov=src tests/
```

### 6. Sair do ambiente virtual

```bash
deactivate
```

## Estrutura do Projeto

```
gilded-rose/
├── README.md
├── requirements.txt
├── .gitignore
├── src/               -> codigo-fonte
│   ├── item.py        -> classe Item (NAO ALTERAR)
│   ├── gilded_rose.py -> classe GildedRose original
│   ├── main.py        -> ponto de entrada
│   ├── domain/        -> regras de negocio
│   ├── application/   -> orquestracao
│   └── infra/         -> entry point
├── tests/             -> testes automatizados (pytest)
├── docs/              -> documentacao do projeto
└── apresentacao/      -> slides
```

## Documentacao

- `docs/guia-equipe.md` - guia completo da equipe com tarefas e git flow
- `docs/trabalho.md` - especificacao do trabalho pelo professor
- `docs/commits.md` - plano de todos os commits do projeto
- `docs/diagnostico_tecnico.md` - analise de code smells
- `docs/requisitos.md` - requisitos funcionais e nao funcionais
- `docs/plano_contingencia.md` - riscos e estrategia de refatoracao
- `docs/evidencias_testes.md` - logs e resultados dos testes

## Equipe

- Andre Deomondes
- Lucca Silvani
- Ryan Luigi
- Igor Lima
