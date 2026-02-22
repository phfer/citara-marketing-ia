# STORY-2.2: Configure CI/CD

**Epic:** EPIC-DEBT-001
**Sprint:** 2
**Story ID:** STORY-2.2
**Status:** Draft
**Estimativa:** 8 horas
**Priority:** P1 (Alta)
**Débito:** S-004

---

## Descrição

Implementar GitHub Actions para CI/CD automatizado, garantindo qualidade de código e deploy seguro.

---

## Problema

Deploy e validação de código são manuais, causando:
- Risco de código quebrado em produção
- Processo lento e sujeito a erros
- Falha de padronização

---

## Solução

Criar workflows GitHub Actions para:
- Lint (ESLint)
- Type check (TypeScript)
- Testes (Jest/Vitest)
- Branch protection

---

## Acceptance Criteria

- [ ] Workflow `.github/workflows/ci.yml` criado
- [ ] Lint executa automaticamente em PR
- [ ] Type check executa automaticamente em PR
- [ ] Testes executam automaticamente em PR
- [ ] Branch `main` protegido (requer checks pass)
- [ ] PR só pode ser mergeado com checks OK
- [ ] Tempo total de CI < 5 minutos

---

## Tasks

- [ ] **TASK-2.2.1:** Criar workflow base (1h)
- [ ] **TASK-2.2.2:** Configurar job de lint (1h)
- [ ] **TASK-2.2.3:** Configurar job de typecheck (1h)
- [ ] **TASK-2.2.4:** Configurar job de testes (2h)
- [ ] **TASK-2.2.5:** Configurar branch protection (1h)
- [ ] **TASK-2.2.6:** Testar PR completo (2h)

---

## Definition of Done

- [ ] CI funcional em PRs
- [ ] Main branch protegida
- [ ] Todos checks < 5min

---

## Workflow Template

```yaml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint

  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run typecheck

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

---

## File List

- `.github/workflows/ci.yml` (novo)
- `.github/workflows/cd.yml` (opcional)
- `docs/ci-cd.md` (novo)
