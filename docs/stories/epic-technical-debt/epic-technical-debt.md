# Epic: Resolução de Débitos Técnicos - Citara Marketing IA

**Epic ID:** EPIC-DEBT-001
**Prioridade:** P0 (Crítica)
**Sprint:** 1-4 (4 semanas)
**Budget Aprovado:** R$ 6.300 (P0+P1) | R$ 16.200 (completo)

---

## Objetivo do Epic

Resolver todos os débitos técnicos críticos e altos do projeto Citara Marketing IA, estabelecendo uma fundação sólida para desenvolvimento sustentável.

---

## Escopo

### In Scope (P0 + P1)

| ID | Débito | Horas | Sprint |
|----|--------|-------|--------|
| DB-003 | RLS policies genéricas | 6h | 1 |
| DB-001 | Schema vazio | 16h | 1 |
| DB-002 | Migrations | 4h | 2 |
| S-004 | CI/CD | 8h | 2 |
| S-005 | Testes | 8h | 2 |

**Subtotal:** 42h | R$ 6.300

### Out of Scope (P2 + P3)

Débitos médios e baixos serão tratados em epics futuros:
- EPIC-DEBT-002: Enhancement (P2)
- EPIC-UX-001: Dashboard & Interface (P3)

---

## Critérios de Sucesso

- [ ] Todos débitos P0 resolvidos
- [ ] Todos débitos P1 resolvidos
- [ ] Quality score ≥ 70%
- [ ] Zero security CRITICAL issues
- [ ] CI/CD operacional
- [ ] Test coverage ≥ 70%

---

## Timeline

| Sprint | Duração | Focus | Story |
|--------|---------|-------|-------|
| **Sprint 1** | 1 semana | Security Foundation | story-1.1, story-1.2 |
| **Sprint 2** | 1 semana | Dev Infrastructure | story-2.1, story-2.2, story-2.3 |

---

## Stories

### Sprint 1: Security Foundation

#### story-1.1: Configure RLS Policies

**ID:** STORY-1.1
**Título:** Implementar Row Level Security no Supabase
**Débito:** DB-003
**Estimativa:** 6 horas
**Prioridade:** P0

**Acceptance Criteria:**
- [ ] Revoke `GRANT ALL` de roles genéricas
- [ ] Habilitar RLS em todas as tabelas
- [ ] Criar policies mínimas (SELECT authenticated)
- [ ] Criar policies admin (INSERT/UPDATE/DELETE)
- [ ] Testar acesso via diferentes roles
- [ ] Documentar policies em SCHEMA.md

**Definition of Done:**
- RLS ativo em todas as tabelas
- Policies documentadas
- Testes de acesso passando

---

#### story-1.2: Create Database Schema

**ID:** STORY-1.2
**Título:** Criar estrutura de tabelas core
**Débito:** DB-001
**Estimativa:** 16 horas
**Prioridade:** P0
**Depends:** STORY-1.1

**Acceptance Criteria:**
- [ ] Criar tabela `clientes`
- [ ] Criar tabela `projetos`
- [ ] Criar tabela `conteudos`
- [ ] Criar tabela `usuarios`
- [ ] Adicionar constraints (PK, FK, Unique)
- [ ] Criar migration versionada
- [ ] Testar inserts/queries
- [ ] Atualizar ERD

**Definition of Done:**
- Todas tabelas criadas
- Migration aplicada com sucesso
- ERD atualizado

---

### Sprint 2: Development Infrastructure

#### story-2.1: Implement Migrations

**ID:** STORY-2.1
**Título:** Configurar estrutura de migrations versionadas
**Débito:** DB-002
**Estimativa:** 4 horas
**Prioridade:** P1
**Depends:** STORY-1.2

**Acceptance Criteria:**
- [ ] Criar estrutura de migrations
- [ ] Migrations existentes versionadas
- [ ] Testar rollback
- [ ] Documentar processo

**Definition of Done:**
- Migrations versionadas
- Rollback testado

---

#### story-2.2: Configure CI/CD

**ID:** STORY-2.2
**Título:** Implementar GitHub Actions para CI/CD
**Débito:** S-004
**Estimativa:** 8 horas
**Prioridade:** P1

**Acceptance Criteria:**
- [ ] Criar workflow de lint
- [ ] Criar workflow de testes
- [ ] Criar workflow de typecheck
- [ ] Configurar branch protection
- [ ] PR auto-approve em checks pass

**Definition of Done:**
- PRs validados automaticamente
- Branches protegidos

---

#### story-2.3: Implement Tests

**ID:** STORY-2.3
**Título:** Criar suíte de testes automatizados
**Débito:** S-005
**Estimativa:** 8 horas
**Prioridade:** P1
**Depends:** STORY-2.2

**Acceptance Criteria:**
- [ ] Configurar Jest/Vitest
- [ ] Criar testes unitários (core)
- [ ] Criar testes de integração (DB)
- [ ] Coverage ≥ 70%
- [ ] Testes rodam no CI

**Definition of Done:**
- Test coverage ≥ 70%
- CI roda testes automaticamente

---

## Orçamento

| Sprint | Horas | Custo (R$150/h) |
|--------|-------|-----------------|
| Sprint 1 | 22h | R$ 3.300 |
| Sprint 2 | 20h | R$ 3.000 |
| **TOTAL** | **42h** | **R$ 6.300** |

---

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Schema mal definido | Revisar com @data-engineer |
| RLS bloqueia ops | Testar antes de deploy |
| CI/CD complexo | Usar templates do AIOS |

---

## Links

- [Technical Debt Assessment](../prd/technical-debt-assessment.md)
- [Executive Report](../reports/TECHNICAL-DEBT-REPORT.md)
- [QA Review](../reviews/qa-review.md)

---

*Epic criado em: 2026-02-22*
*PM: @pm (Bob)*
*Architect: @architect (Aria)*
