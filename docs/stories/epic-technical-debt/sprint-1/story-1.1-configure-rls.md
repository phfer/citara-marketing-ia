# STORY-1.1: Configure RLS Policies

**Epic:** EPIC-DEBT-001
**Sprint:** 1
**Story ID:** STORY-1.1
**Status:** Draft
**Estimativa:** 6 horas
**Priority:** P0 (Crítica)
**Débito:** DB-003

---

## Descrição

Implementar Row Level Security (RLS) no Supabase para proteger dados sensíveis. Atualmente, o database utiliza permissões genéricas (`GRANT ALL`) que representam um risco de segurança crítico.

## Problema

```sql
-- ⚠️ RISCO ATUAL
GRANT ALL ON TABLES TO anon;
GRANT ALL ON TABLES TO authenticated;
```

Isso permite que usuários anônimos e autenticados tenham acesso irrestrito, incluindo DELETE e DROP.

## Solução

1. Remover grants genéricos
2. Habilitar RLS em todas as tabelas
3. Criar policies específicas por role
4. Testar acessos

---

## Acceptance Criteria

### Given
- Supabase project conectado
- Schema `public` existe

### When
- RLS é configurado nas tabelas

### Then
- [ ] `GRANT ALL` foi revogado de `anon` e `authenticated`
- [ ] RLS está habilitado em todas as tabelas
- [ ] Policy `SELECT` existe para `authenticated`
- [ ] Policy `INSERT/UPDATE/DELETE` existe para `admin`
- [ ] Testes de acesso passam (authenticated pode ler, admin pode escrever)
- [ ] Documento SCHEMA.md atualizado com policies

---

## Scope

### IN
- Revoke de grants genéricos
- Habilitar RLS nas tabelas existentes
- Criar policies mínimas
- Testes de acesso
- Documentação

### OUT
- Policies complexas (por usuário, por tenant)
- Audit logging
- Performance tuning

---

## Tasks

- [ ] **TASK-1.1.1:** Revoke `GRANT ALL` (30min)
- [ ] **TASK-1.1.2:** Habilitar RLS nas tabelas (1h)
- [ ] **TASK-1.1.3:** Criar policies SELECT (1h)
- [ ] **TASK-1.1.4:** Criar policies INSERT/UPDATE/DELETE (1h)
- [ ] **TASK-1.1.5:** Testar acessos via Supabase JS (2h)
- [ ] **TASK-1.1.6:** Atualizar SCHEMA.md (30min)

---

## Definition of Done

- [ ] Todos AC atendidos
- [ ] Code review aprovado
- [ ] Testes passando
- [ ] Documentação atualizada
- [ ] Zero CRITICAL security issues

---

## Dependencies

- **Requires:** Supabase CLI autenticado
- **Blocks:** STORY-1.2 (Create Schema)

---

## Notes

**Ordem é crítica:**
1. Primeiro revoke GRANT ALL
2. Depois habilite RLS
3. Crie policies antes de habilitar

**Se fizer na ordem errada, pode perder acesso!**

---

## File List

- `supabase/migrations/xxx_enable_rls.sql`
- `supabase/tests/rls.test.ts`
- `supabase/docs/SCHEMA.md` (atualizado)
