# STORY-1.2: Create Database Schema

**Epic:** EPIC-DEBT-001
**Sprint:** 1
**Story ID:** STORY-1.2
**Status:** Draft
**Estimativa:** 16 horas
**Priority:** P0 (Crítica)
**Débito:** DB-001
**Depends:** STORY-1.1

---

## Descrição

Criar a estrutura de tabelas core do sistema Citara Marketing IA. O database está vazio e precisa de entidades fundamentais para operação: clientes, projetos, conteúdos e usuários.

---

## Problema

Database Supabase provisionado mas **sem tabelas criadas**, impossibilitando persistência de dados.

---

## Solução

Criar 4 tabelas core com relacionamentos, constraints e migrations versionadas.

### Tabelas

```sql
-- 1. Clientes
clientes (id, nome, ticket_mensal, status, created_at)

-- 2. Projetos
projetos (id, cliente_id, nome, tipo, status, created_at)

-- 3. Conteúdos
conteudos (id, projeto_id, tipo, plataforma, status, url, created_at)

-- 4. Usuários
usuarios (id, nome, email, role, created_at)
```

---

## Acceptance Criteria

### Given
- RLS habilitado (STORY-1.1 completo)
- Supabase CLI conectado

### When
- Migration de schema é executada

### Then
- [ ] Tabela `clientes` criada com PK
- [ ] Tabela `projetos` criada com FK para clientes
- [ ] Tabela `conteudos` criada com FK para projetos
- [ ] Tabela `usuarios` criada
- [ ] Constraints NOT NULL aplicados
- [ ] Migration file versionada criada
- [ ] `supabase db push` executado com sucesso
- [ ] ERD atualizado em docs

---

## Scope

### IN
- 4 tabelas core
- Primary keys (BIGSERIAL)
- Foreign keys com ON DELETE CASCADE
- NOT NULL constraints
- Timestamps (TIMESTAMPTZ)
- Migrations versionadas
- ERD documentado

### OUT
- Tabelas de histórico/audit
- Tabelas de analytics
- Indexes (próxima story)
- Tabelas de many-to-many
- Triggers

---

## Tasks

- [ ] **TASK-1.2.1:** Criar migration file (1h)
- [ ] **TASK-1.2.2:** Escrever SQL tabela clientes (2h)
- [ ] **TASK-1.2.3:** Escrever SQL tabela projetos (2h)
- [ ] **TASK-1.2.4:** Escrever SQL tabela conteudos (2h)
- [ ] **TASK-1.2.5:** Escrever SQL tabela usuarios (2h)
- [ ] **TASK-1.2.6:** Adicionar constraints (2h)
- [ ] **TASK-1.2.7:** Testar migration local (2h)
- [ ] **TASK-1.2.8:** Push para Supabase remoto (1h)
- [ ] **TASK-1.2.9:** Criar ERD em Mermaid (2h)

---

## Definition of Done

- [ ] Todos AC atendidos
- [ ] Migration aplicada em dev e prod
- [ ] Inserts de teste funcionam
- [ ] ERD documentado
- [ ] Zero erros de schema

---

## Dependencies

- **Requires:** STORY-1.1 (RLS configured)
- **Blocks:** STORY-2.1 (Migrations)

---

## File List

- `supabase/migrations/xxx_create_core_tables.sql`
- `supabase/tests/schema.test.ts`
- `docs/database/ERD.md` (novo)
- `supabase/docs/SCHEMA.md` (atualizado)

---

## SQL Template

```sql
-- Migration: 001_create_core_tables.sql

-- Clientes
CREATE TABLE clientes (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    ticket_mensal DECIMAL(10,2),
    status TEXT DEFAULT 'ativo' CHECK (status IN ('ativo', 'inativo', 'pausado')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Projetos
CREATE TABLE projetos (
    id BIGSERIAL PRIMARY KEY,
    cliente_id BIGINT NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
    nome TEXT NOT NULL,
    tipo TEXT,
    status TEXT DEFAULT 'pendente' CHECK (status IN ('pendente', 'em_andamento', 'concluido')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Conteúdos
CREATE TABLE conteudos (
    id BIGSERIAL PRIMARY KEY,
    projeto_id BIGINT NOT NULL REFERENCES projetos(id) ON DELETE CASCADE,
    tipo TEXT NOT NULL,
    plataforma TEXT,
    status TEXT DEFAULT 'rascunho' CHECK (status IN ('rascunho', 'revisao', 'publicado')),
    url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Usuários
CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT DEFAULT 'usuario' CHECK (role IN ('admin', 'usuario')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Habilitar RLS (já feito na STORY-1.1)
ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;
ALTER TABLE projetos ENABLE ROW LEVEL SECURITY;
ALTER TABLE conteudos ENABLE ROW LEVEL SECURITY;
ALTER TABLE usuarios ENABLE ROW LEVEL SECURITY;

-- Policies mínimas (STORY-1.1)
-- ... (ver STORY-1.1)
```
