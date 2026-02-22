# STORY-2.3: Implement Tests

**Epic:** EPIC-DEBT-001
**Sprint:** 2
**Story ID:** STORY-2.3
**Status:** Draft
**Estimativa:** 8 horas
**Priority:** P1 (Alta)
**Débito:** S-005
**Depends:** STORY-2.2

---

## Descrição

Criar suíte de testes automatizados (unit + integration) com coverage mínimo de 70%.

---

## Problema

Sem testes automatizados, o projeto está sujeito a:
- Regressões não detectadas
- Refatorações arriscadas
- Falta de confiança em changes

---

## Solução

Implementar testes usando Vitest (ou Jest):
- Testes unitários para funções core
- Testes de integração para database
- Coverage ≥ 70%
- Integração com CI (STORY-2.2)

---

## Acceptance Criteria

- [ ] Vitest/Jest configurado
- [ ] Testes unitários criados (core functions)
- [ ] Testes de integração criados (DB)
- [ ] Coverage ≥ 70%
- [ ] Testes rodam no CI (< 3min)
- [ ] `npm test` executa todos testes

---

## Tasks

- [ ] **TASK-2.3.1:** Configurar Vitest (1h)
- [ ] **TASK-2.3.2:** Criar testes unitários core (2h)
- [ ] **TASK-2.3.3:** Criar testes integração DB (3h)
- [ ] **TASK-2.3.4:** Configurar coverage (1h)
- [ ] **TASK-2.3.5:** Integrar com CI (1h)

---

## Definition of Done

- [ ] Coverage ≥ 70%
- [ ] Todos testes passando
- [ ] Integração com CI OK

---

## File List

- `vitest.config.ts` (novo)
- `tests/unit/*.test.ts` (novos)
- `tests/integration/*.test.ts` (novos)
- `package.json` (scripts atualizados)
