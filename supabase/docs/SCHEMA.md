# SCHEMA.md - Citara Marketing Database

**Projeto:** Citara Marketing
**Database:** Supabase PostgreSQL
**Project Ref:** `fotizvfbsyllvycswwuh`
**Região:** South America (São Paulo)
**Data:** 2026-02-22
**Autor:** @data-engineer (Dara)

---

## Status do Database

| Estado | Descrição |
|--------|-----------|
| **Provisionado** | ✅ Sim |
| **Tabelas Criadas** | ❌ Não (schema vazio) |
| **Migrations** | ❌ Nenhuma |
| **RLS Policies** | ⚠️ Padrão (sem políticas customizadas) |
| **Functions** | ❌ Nenhuma |

---

## Estrutura Atual

### Schema: `public`

O schema `public` está **vazio** - nenhuma tabela foi criada ainda.

### Roles Configuradas

| Role | Descrição | Permissões Padrão |
|------|-----------|-------------------|
| `postgres` | Superusuário | ALL |
| `anon` | Acesso anônimo (público) | USAGE on schema |
| `authenticated` | Usuários autenticados | USAGE on schema |
| `service_role` | Role de serviço (backend) | USAGE on schema |

### Grants Padrão

```sql
-- Sequences
GRANT ALL ON SEQUENCES TO postgres, anon, authenticated, service_role;

-- Functions
GRANT ALL ON FUNCTIONS TO postgres, anon, authenticated, service_role;

-- Tables
GRANT ALL ON TABLES TO postgres, anon, authenticated, service_role;
```

---

## Débitos Identificados (Database)

| ID | Débito | Severidade | Esforço | Impacto |
|----|--------|------------|---------|---------|
| **DB-001** | Schema vazio - nenhuma tabela criada | Crítico | Alto | O sistema não persiste dados |
| **DB-002** | Sem migrations versionadas | Alto | Médio | Impossível rastrear evolução |
| **DB-003** | RLS policies genéricas (todas permissões) | Crítico | Alto | Risco de segurança |
| **DB-004** | Sem índices (não há tabelas) | N/A | - | - |
| **DB-005** | Sem constraints ou validations | N/A | - | - |

---

## Recomendações

### Imediatas (Crítico)

1. **Criar estrutura de tabelas**
   - Definir entidades principais (Clientes, Projetos, Conteúdos, etc.)
   - Criar migrations versionadas

2. **Configurar RLS Policies adequadas**
   - Remover grants genéricos `GRANT ALL`
   - Implementar políticas por role

3. **Documentar modelo de dados**
   - ERD (Entity Relationship Diagram)
   - Dicionário de dados

### Curto Prazo

1. **Criar índices** para performance
2. **Implementar triggers** para auditoria
3. **Configurar backups** automatizados

---

## Próximos Passos

1. **Definir modelo de dados** com @architect
2. **Criar migrations** usando Supabase CLI
3. **Implementar RLS** policies específicas
4. **Documentar schema** em SCHEMA.md

---

*Fim da FASE 2 - Análise de Database*

— Dara, arquiteta de dados 🗄️
