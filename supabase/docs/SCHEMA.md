# SCHEMA.md - Citara Marketing Database

**Projeto:** Citara Marketing
**Database:** Supabase PostgreSQL
**Project Ref:** `fotizvfbsyllvycswwuh`
**Região:** South America (São Paulo)
**Data:** 2026-02-22
**Autor:** @data-engineer (Dara)
**Versão:** 3.0 (Schema Criado)

---

## Status do Database

| Estado | Descrição |
|--------|-----------|
| **Provisionado** | ✅ Sim |
| **Tabelas Criadas** | ✅ 4 tabelas core |
| **Migrations** | ✅ 3 migrations aplicadas |
| **RLS Policies** | ✅ Ativo com policies específicas |
| **Functions** | ✅ 1 function (updated_at trigger) |
| **Triggers** | ✅ 4 triggers (auto updated_at) |

---

## Migrations Aplicadas

| ID | Arquivo | Descrição | Data |
|----|---------|-----------|------|
| 001 | `001_revoke_generic_grants.sql` | Revoga GRANT ALL genérico | 2026-02-22 |
| 002 | `002_enable_rls.sql` | Configura framework RLS | 2026-02-22 |
| 003 | `003_create_core_tables.sql` | Criar tabelas core + RLS policies | 2026-02-22 |

---

## Estrutura do Database

### Tabelas Criadas

| Tabela | Descrição | Registros |
|--------|-----------|-----------|
| `clientes` | Clientes da agência | 0 |
| `projetos` | Projetos por cliente | 0 |
| `conteudos` | Conteúdos de marketing | 0 |
| `usuarios` | Usuários do sistema | 0 |

### Schema: `public`

```
clientes (1) -----> (N) projetos (1) -----> (N) conteudos
   ^
   |
   └── (N) usuarios (gerencia)
```

---

## Detalhes das Tabelas

### 1. clientes

| Coluna | Tipo | Constraints |
|--------|------|-------------|
| id | BIGSERIAL | PK |
| nome | TEXT | NOT NULL, UNIQUE |
| ticket_mensal | DECIMAL(10,2) | - |
| status | TEXT | DEFAULT 'ativo' CHECK IN ('ativo','inativo','pausado') |
| created_at | TIMESTAMPTZ | DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | DEFAULT NOW() |

**RLS Policies:**
- `clientes_select_authenticated`: Authenticated pode ler
- `clientes_all_admin`: Admin pode tudo

---

### 2. projetos

| Coluna | Tipo | Constraints |
|--------|------|-------------|
| id | BIGSERIAL | PK |
| cliente_id | BIGINT | FK → clientes(id) ON DELETE CASCADE, NOT NULL |
| nome | TEXT | NOT NULL |
| tipo | TEXT | - |
| status | TEXT | DEFAULT 'pendente' CHECK IN ('pendente','em_andamento','concluido','cancelado') |
| created_at | TIMESTAMPTZ | DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | DEFAULT NOW() |

**RLS Policies:**
- `projetos_select_authenticated`: Authenticated pode ler
- `projetos_all_admin`: Admin pode tudo

---

### 3. conteudos

| Coluna | Tipo | Constraints |
|--------|------|-------------|
| id | BIGSERIAL | PK |
| projeto_id | BIGINT | FK → projetos(id) ON DELETE CASCADE, NOT NULL |
| tipo | TEXT | NOT NULL |
| plataforma | TEXT | - |
| status | TEXT | DEFAULT 'rascunho' CHECK IN ('rascunho','revisao','aprovado','publicado') |
| url | TEXT | - |
| titulo | TEXT | - |
| descricao | TEXT | - |
| created_at | TIMESTAMPTZ | DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | DEFAULT NOW() |
| publicado_at | TIMESTAMPTZ | - |

**RLS Policies:**
- `conteudos_select_authenticated`: Authenticated pode ler
- `conteudos_all_admin`: Admin pode tudo

---

### 4. usuarios

| Coluna | Tipo | Constraints |
|--------|------|-------------|
| id | BIGSERIAL | PK |
| nome | TEXT | NOT NULL |
| email | TEXT | NOT NULL, UNIQUE |
| role | TEXT | DEFAULT 'usuario' CHECK IN ('admin','usuario') |
| ativo | BOOLEAN | DEFAULT true |
| created_at | TIMESTAMPTZ | DEFAULT NOW() |
| updated_at | TIMESTAMPTZ | DEFAULT NOW() |
| last_login | TIMESTAMPTZ | - |

**RLS Policies:**
- `usuarios_select_self`: Usuário vê apenas seus dados (email match)
- `usuarios_all_admin`: Admin pode tudo

---

## Security

### Roles Configuradas

| Role | Descrição | Permissões |
|------|-----------|-------------|
| `postgres` | Superusuário | ALL |
| `anon` | Acesso anônimo | USAGE |
| `authenticated` | Usuários autenticados | USAGE + SELECT (via RLS) |
| `service_role` | Role de serviço | USAGE + ALL |

### RLS Policies Ativas

| Tabela | Policy | Role | Comando |
|--------|--------|------|---------|
| clientes | select_authenticated | authenticated | SELECT |
| clientes | all_admin | authenticated | ALL (se role=admin) |
| projetos | select_authenticated | authenticated | SELECT |
| projetos | all_admin | authenticated | ALL (se role=admin) |
| conteudos | select_authenticated | authenticated | SELECT |
| conteudos | all_admin | authenticated | ALL (se role=admin) |
| usuarios | select_self | authenticated | SELECT (se email=jwt.email) |
| usuarios | all_admin | authenticated | ALL (se role=admin) |

---

## Índices Criados

| Tabela | Índice | Colunas |
|--------|--------|--------|
| clientes | idx_clientes_status | status |
| projetos | idx_projetos_cliente_id | cliente_id |
| projetos | idx_projetos_status | status |
| conteudos | idx_conteudos_projeto_id | projeto_id |
| conteudos | idx_conteudos_status | status |
| conteudos | idx_conteudos_plataforma | plataforma |
| usuarios | idx_usuarios_email | email |
| usuarios | idx_usuarios_role | role |

---

## Triggers

| Trigger | Tabela | Função |
|---------|--------|--------|
| update_clientes_updated_at | clientes | update_updated_at_column() |
| update_projetos_updated_at | projetos | update_updated_at_column() |
| update_conteudos_updated_at | conteudos | update_updated_at_column() |
| update_usuarios_updated_at | usuarios | update_updated_at_column() |

**Função:** `update_updated_at_column()` - Atualiza `updated_at` automaticamente antes de UPDATE.

---

## Functions

| Function | Propósito |
|----------|-----------|
| `update_updated_at_column()` | Trigger para auto updated_at |

---

## Débitos Resolvidos

| ID | Débito | Status |
|----|--------|--------|
| **DB-001** | Schema vazio - nenhuma tabela criada | ✅ RESOLVIDO |
| **DB-002** | Sem migrations versionadas | ✅ RESOLVIDO |
| **DB-003** | RLS policies genéricas | ✅ RESOLVIDO |
| **DB-006** | Configurar RLS policies específicas | ✅ RESOLVIDO |

---

## Próximos Passos

1. **Popular tabelas** com dados iniciais (seeds)
2. **Criar tabelas secundárias** (tags, categorias, etc.)
3. **Implementar índices otimizados** (baseado em queries reais)
4. **Configurar audit logging**

---

## Links

- [ERD - Diagrama Completo](../../../database/ERD.md)
- [DB-AUDIT - Security Audit](./DB-AUDIT.md)

---

*SCHEMA.md v3.0 - Schema Criado e Operacional*

— Dara, arquiteta de dados 🗄️
