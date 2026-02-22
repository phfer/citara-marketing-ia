# EPIC-DEBT-001: Resolução de Débitos Técnicos

**Tipo:** Epic
**Status:** Ready
**Prioridade:** P0 (Crítica)
**Epic Owner:** @pm (Bob)
**Sprint:** 1-2 (4 semanas)
**Budget:** R$ 6.300 (P0+P1) | R$ 16.200 (completo)

---

## Contexto

O Brownfield Discovery identificou **14 débitos técnicos** no projeto Citara Marketing IA. Os débitos críticos (P0) e altos (P1) precisam ser resolvidos antes da entrada em produção para garantir segurança e estabilidade.

**Referência:** [TECHNICAL-DEBT-REPORT.md](../../../reports/TECHNICAL-DEBT-REPORT.md)

---

## Objetivo do Epic

Resolver todos os débitos técnicos **P0 e P1**, estabelecendo uma fundação sólida para desenvolvimento sustentável.

### Metas

- [ ] Zero vulnerabilidades CRITICAL de segurança
- [ ] Database funcional com schema implementado
- [ ] CI/CD automatizado operacional
- [ ] Test coverage ≥ 70%
- [ ] Quality score ≥ 70%

---

## Escopo

### IN Scope (P0 + P1)

| ID | Débito | Área | Horas |
|----|--------|------|-------|
| DB-003 | RLS policies genéricas | DB | 6h |
| DB-001 | Schema vazio | DB | 16h |
| DB-002 | Migrations | DB | 4h |
| S-004 | CI/CD | Sistema | 8h |
| S-005 | Testes | Sistema | 8h |

**Total:** 42 horas | R$ 6.300

### OUT Scope (P2 + P3)

Débitos médios e baixos serão tratados em epics futuros:
- EPIC-DEBT-002: Enhancement (P2)
- EPIC-UX-001: Dashboard & Interface (P3)

---

## Stories

### Sprint 1: Security Foundation (22h)

| Story ID | Título | Pontos | Status |
|----------|--------|--------|--------|
| STORY-1.1 | Configure RLS Policies | 3 | Pending |
| STORY-1.2 | Create Database Schema | 8 | Pending |

### Sprint 2: Development Infrastructure (20h)

| Story ID | Título | Pontos | Status |
|----------|--------|--------|--------|
| STORY-2.1 | Implement Migrations | 2 | Pending |
| STORY-2.2 | Configure CI/CD | 5 | Pending |
| STORY-2.3 | Implement Tests | 5 | Pending |

---

## Critérios de Sucesso do Epic

- [ ] Todas stories P0 completadas
- [ ] Todas stories P1 completadas
- [ ] Quality score ≥ 70%
- [ ] Zero security CRITICAL issues
- [ ] CI/CD operacional (PR checks < 5min)
- [ ] Test coverage ≥ 70%
- [ ] Migration rollback testado
- [ ] Documentação atualizada

---

## Timeline

| Sprint | Duração | Focus | Stories |
|--------|---------|-------|---------|
| **Sprint 1** | 1 semana | Security Foundation | 2 stories |
| **Sprint 2** | 1 semana | Dev Infrastructure | 3 stories |
| **Total** | **2 semanas** | **P0+P1** | **5 stories** |

---

## Orçamento

| Categoria | Horas | Custo (R$150/h) |
|-----------|-------|-----------------|
| P0 - Críticos | 22h | R$ 3.300 |
| P1 - Altos | 20h | R$ 3.000 |
| **TOTAL** | **42h** | **R$ 6.300** |

---

## Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Schema mal definido | Média | Alto | Revisar com @data-engineer antes |
| RLS bloqueia ops | Baixa | Alto | Testar antes de deploy |
| CI/CD complexo | Média | Médio | Usar templates do AIOS |

---

## Dependências

### Externas
- Supabase CLI autenticado
- GitHub repo configurado
- Node.js 18+ instalado

### Internas
- STORY-1.2 depende de STORY-1.1
- STORY-2.1 depende de STORY-1.2
- STORY-2.3 depende de STORY-2.2

---

## Stakeholders

| Role | Nome | Responsabilidade |
|------|------|-------------------|
| Epic Owner | @pm (Bob) | Priorização, bloqueios |
| Architect | @architect (Aria) | Design técnico |
| Data Engineer | @data-engineer (Dara) | Database decisions |
| QA | @qa (Quinn) | Quality gates |

---

## Links

- [Assessment Técnico](../../../prd/technical-debt-assessment.md)
- [Executive Report](../../../reports/TECHNICAL-DEBT-REPORT.md)
- [Database Review](../../../reviews/db-specialist-review.md)
- [QA Review](../../../reviews/qa-review.md)

---

## Histórico

| Data | Alteração | Autor |
|------|-----------|-------|
| 22/02/2026 | Epic criado | @pm (Bob) |

---

*Última atualização: 2026-02-22*
