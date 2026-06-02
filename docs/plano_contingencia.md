# Plano de Contingência e Refatoração — Gilded Rose

## 1. Estratégia de Refatoração Segura

A equipe seguirá 4 princípios para modificar o sistema sem quebrar o comportamento existente:

1. **Testes primeiro** — Criar testes de caracterização ANTES de qualquer refatoração para capturar o comportamento atual do sistema
2. **Refatoração incremental** — Uma mudança por vez, sempre rodando `pytest -v` após cada alteração
3. **Nunca alterar o que é proibido** — Classes `Item` e propriedade `Items` da `GildedRose` permanecem intactas
4. **Commits atômicos** — Cada commit representa uma transformação completa e verificável

## 2. Partes do Código

### Podem ser alteradas
- Método `update_quality` na classe `GildedRose` (refatoração completa)
- Criação de novos arquivos: strategies, factory, camadas, testes
- `main.py` (ponto de entrada)

### Não podem ser alteradas (penalidade -2,0 cada)
- Classe `Item` em `src/item.py`
- Propriedade `self.items` na classe `GildedRose`

## 3. Riscos e Mitigações

| Risco | Impacto | Probabilidade | Mitigação |
|-------|---------|---------------|-----------|
| Quebrar regra do Aged Brie (quality aumentar errado) | Regra de negócio incorreta | Média | Teste dedicado que verifica incremento exato antes da refatoração |
| Quality ultrapassar 50 no Backstage Pass | Violação de limite | Média | Teste de borda com quality=49 em sell_in <= 5 |
| Item comum degradar errado após sell_in | Comportamento inconsistente | Média | Teste com sell_in=0 e quality=10 verificando degradação dupla |
| Conjured degradar igual item normal | Funcionalidade nova incorreta | Alta | Teste comparando Conjured vs Normal lado a lado |
| Alterar Sulfuras sem querer | Mudar quality 80 lendária | Baixa | Teste que verifica imutabilidade + code review obrigatório |
| Perder teste existente após merge | Falso positivo | Média | CI rodando `pytest` antes de todo merge no `main` |
| Esquecer caso de borda (quality negativa) | Violação de regra | Média | Testes parametrizados cobrindo 0, 50, valores negativos |

## 4. Ordem das Mudanças

| Etapa | Branch | Mudança | Validação |
|-------|--------|---------|-----------|
| 1 | `test/unitario` | Criar testes de caracterização para todos os itens | `pytest -v` — 100% dos cenários atuais capturados |
| 2 | `refactor/srp` | Extrair regras de qualidade para Strategy classes separadas | `pytest -v` — mesmos resultados do código original |
| 3 | `refactor/ocp` | Criar Factory para adicionar novos tipos sem modificar código existente | `pytest -v` + adicionar item novo sem editar update_quality |
| 4 | `refactor/arch` | Separar em camadas domain/application/infra | `pytest -v` — comportamento inalterado |
| 5 | `feat/conjured` | Implementar Conjured com degradação 2x mais rápida | `pytest -v` — testes específicos + regressão dos existentes |
| 6 | `docs/final` | Evidências, README e apresentação | Documentação revisada e testes finais |

## 5. Plano de Rollback

Se em qualquer etapa os testes falharem:

```bash
git checkout -- .           # descarta mudanças não commitadas
git stash                   # ou guarda temporariamente
git checkout <branch-anterior>  # volta pra branch estável
```

Se o merge quebrou o `main`:

```bash
git revert <hash-do-commit>  # desfaz o merge mantendo histórico
```

## 6. Critérios de Validação (checklist)

- [ ] `pytest -v` — todos os testes passam (0 falhas, 0 erros)
- [ ] Testes de caracterização originais continuam passando após refatoração
- [ ] Conjured perde quality 2x mais rápido que item normal
- [ ] Quality nunca < 0 (testado com valores extremos)
- [ ] Quality nunca > 50 (exceto Sulfuras = 80)
- [ ] Sulfuras não altera sell_in nem quality
- [ ] Código refatorado não contém a classe Item alterada
- [ ] Nenhum arquivo `src/item.py` foi modificado (verificar com `git diff`)
