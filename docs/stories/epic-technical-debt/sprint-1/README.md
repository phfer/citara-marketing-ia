# Sprint 1: Security Foundation

**Epic:** EPIC-DEBT-001
**Duração:** 1 semana
**Horas:** 22h
**Investimento:** R$ 3.300
**Focus:** Resolver débitos P0 (Críticos)

## Stories

| Story | Título | Horas | Status |
|-------|--------|-------|--------|
| [1.1](./story-1.1-configure-rls.md) | Configure RLS Policies | 6h | Pending |
| [1.2](./story-1.2-create-schema.md) | Create Database Schema | 16h | Pending |

## Objetivos

- [ ] Remover grants genéricos (`GRANT ALL`)
- [ ] Implementar RLS policies específicas
- [ ] Criar tabelas core do sistema
- [ ] Estabelecer base para persistência de dados

## Dependências

- STORY-1.2 depende de STORY-1.1 (RLS primeiro)
- Sprint 2 depende deste sprint

## Critérios de Sucesso

- [ ] Zero vulnerabilidades CRITICAL de segurança
- [ ] RLS habilitado em todas as tabelas
- [ ] Todas tabelas core criadas
- [ ] Migration versionada aplicada
