# Plano de Contingência e Refatoração — Gilded Rose

## Estratégia

1. **Caracterizar primeiro** — Criar testes que capturem o comportamento atual
2. **Refatorar em pequenos passos** — Uma mudança por vez, rodando testes após cada uma
3. **Nunca alterar Item ou Items** — Essas classes são proibidas pela especificação

## Ordem das Mudanças

| Ordem | O que fazer | Branch |
|-------|-------------|--------|
| 1 | Criar testes de caracterização | test/unitario |
| 2 | Aplicar SRP — extrair strategies | refactor/srp |
| 3 | Aplicar OCP — factory pattern | refactor/ocp |
| 4 | Clean Architecture — camadas | refactor/arch |
| 5 | Implementar Conjured | feat/conjured |
| 6 | Documentação final | docs/final |

## Riscos

| Risco | Probabilidade | Mitigação |
|-------|--------------|-----------|
| Quebrar regra de negócio existente | Média | Testes de caracterização antes |
| Alterar Item indevidamente | Baixa | Code review obrigatório |
| Esquecer caso de borda | Média | Testes para quality=0, quality=50, sell_in=0 |
| Perder comportamento do Conjured | Baixa | Testes dedicados |

## Critérios de Validação

- [ ] Todos os testes existentes passam após cada refatoração
- [ ] Comportamento do sistema original preservado
- [ ] Conjured implementado corretamente
- [ ] Cobertura de testes >= 90% das regras de negócio
