# SCHEMA.md - Citara Marketing Database

**Projeto:** Citara Marketing
**Database:** Supabase PostgreSQL
**Project Ref:** `fotizvfbsyllvycswwuh`
**Região:** South America (São Paulo)
**Data:** 2026-02-22
**Autor:** @data-engineer (Dara)
**Versão:** 2.0 (RLS Configured)

---

## Status do Database

| Estado | Descrição |
|--------|-----------|
| **Provisionado** | ✅ Sim |
| **Tabelas Criadas** | ❌ Não (próxima story) |
| **Migrations** | ✅ 2 migrations aplicadas |
| **RLS Policies** | ✅ Framework configurado |
| **Functions** | ❌ Nenhuma |

---

## Migrations Aplicadas

| ID | Arquivo | Descrição | Data |
|----|---------|-----------|------|
| 001 | `001_revoke_generic_grants.sql` | Revoga GRANT ALL genérico | 2026-02-22 |
| 002 | `002_enable_rls.sql` | Configura framework RLS | 2026-02-22 |

---

## Estrutura Atual

### Schema: `public`

O schema `public` está **vazio** - tabelas serão criadas na STORY-1.2.

### Roles Configuradas

| Role | Descrição | Permissões Atuais |
|------|-----------|---------------------|
| `postgres` | Superusuário | ALL (completo) |
| `anon` | Acesso anônimo (público) | USAGE on schema |
| `authenticated` | Usuários autenticados | USAGE on schema |
| `service_role` | Role de serviço (backend) | USAGE + ALL (admin) |

### Security (DB-003: RESOLVIDO ✅)

**Antes:**
```sql
-- ❌ RISCO: Permissões excessivas
GRANT ALL ON TABLES TO anon;
GRANT ALL ON TABLES TO authenticated;
```

**Depois (Migration 001):**
```sql
-- ✅ SEGURO: Permissões mínimas
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM anon;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM authenticated;
GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;
```

---

## RLS Policies Framework

As policies estão definidas na migration `002_enable_rls.sql` e serão aplicadas durante a criação das tabelas (STORY-1.2).

### Padrão de Policies

| Tipo | Descrição | Role |
|------|-----------|------|
| `*_select_authenticated` | Leitura para autenticados | `authenticated` |
| `*_all_admin` | Escrita completa | `admin` (via JWT) |
| `*_select_anon` | Leitura pública (se aplicável) | `anon` |
| `*_select_self` | Leitura própria apenas | `authenticated` |

### Policies por Tabela (serão aplicadas em STORY-1.2)

#### clientes
```sql
ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "clientes_select_authenticated" ON clientes
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "clientes_all_admin" ON clientes
  FOR ALL TO authenticated
  USING (auth.jwt() ->> 'role' = 'admin')
  WITH CHECK (auth.jwt() ->> 'role' = 'admin');
```

#### projetos
```sql
ALTER TABLE projetos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "projetos_select_authenticated" ON projetos
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "projetos_all_admin" ON projetos
  FOR ALL TO authenticated
  USING (auth.jwt() ->> 'role' = 'admin')
  WITH CHECK (auth.jwt() ->> 'role' = 'admin');
```

#### conteudos
```sql
ALTER TABLE conteudos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "conteudos_select_authenticated" ON conteudos
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "conteudos_all_admin" ON conteudos
  FOR ALL TO authenticated
  USING (auth.jwt() ->> 'role' = 'admin')
  WITH CHECK (auth.jwt() ->> 'role' = 'admin');
```

#### usuarios
```sql
ALTER TABLE usuarios ENABLE ROW LEVEL SECURITY;

CREATE POLICY "usuarios_select_self" ON usuarios
  FOR SELECT TO authenticated
  USING (auth.uid() = id);

CREATE POLICY "usuarios_all_admin" ON usuarios
  FOR ALL TO authenticated
  USING (auth.jwt() ->> 'role' = 'admin')
  WITH CHECK (auth.jwt() ->> 'role' = 'admin');
```

---

## Débitos Identificados (Database)

| ID | Débito | Severidade | Status |
|----|--------|------------|--------|
| **DB-001** | Schema vazio - nenhuma tabela criada | Crítico | Pendente |
| **DB-002** | Sem migrations versionadas | Alto | ✅ RESOLVIDO |
| **DB-003** | RLS policies genéricas | Crítico | ✅ RESOLVIDO |
| **DB-006** | Configurar RLS policies específicas | Alto | Em progresso |
| **DB-007** | Testar disaster recovery | Médio | Pendente |
| **DB-008** | Documentar modelo ERD | Médio | Pendente |

---

## Próximos Passos

1. **STORY-1.2:** Criar tabelas com RLS habilitado
2. **STORY-2.1:** Validar migrations e rollback
3. **DB-008:** Criar ERD documentado

---

*SCHEMA.md v2.0 - RLS Framework Configurado*

— Dara, arquiteta de dados 🗄️
