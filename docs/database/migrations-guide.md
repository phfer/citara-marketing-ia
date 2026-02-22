# Database Migrations Guide - Citara Marketing IA

**Projeto:** Citara Marketing IA
**Versão:** 1.0
**Data:** 2026-02-22

---

## Visão Geral

Este guia documenta como trabalhar com migrations do database Supabase no projeto Citara Marketing IA.

---

## Estrutura de Migrations

```
supabase/
├── migrations/               # Arquivos SQL versionados
│   ├── README.md            # Documentação
│   ├── 001_*.sql            # Revoke grants
│   ├── 002_*.sql            # Enable RLS
│   ├── 003_*.sql            # Create tables
│   └── ...
├── tests/                   # Testes de database
└── docs/                    # Documentação
```

---

## Fluxo de Trabalho

### 1. Planejar a Mudança

Antes de criar uma migration, responda:

- [ ] Qual mudança é necessária?
- [ ] Impacto em dados existentes?
- [ ] Requer rollback manual?
- [ ] Depende de outra migration?

### 2. Criar a Migration

```bash
# Criar nova migration
supabase migration short descricao

# Exemplo
supabase migration short add_status_column
# Cria: supabase/migrations/TIMESTAMP_add_status_column.sql
```

### 3. Escrever SQL

```sql
-- Migration: 004_add_status_column.sql
-- Description: Adiciona coluna status
-- Author: @dev (Dex)
-- Date: 2026-02-22

-- Adicionar coluna (IF NOT EXISTS previne erro)
ALTER TABLE clientes
ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'ativo';

-- Adicionar constraint
ALTER TABLE clientes
ADD CONSTRAINT clientes_status_check
CHECK (status IN ('ativo', 'inativo', 'pausado'));

-- Adicionar índice
CREATE INDEX IF NOT EXISTS idx_clientes_status
ON clientes(status);
```

### 4. Testar Localmente

```bash
# Reset database local (apaga e recria)
supabase db reset --local

# Verificar se funcionou
supabase db remote tables
```

### 5. Aplicar no Remoto

```bash
# Push migration para remoto
supabase db push

# Confirmar
supabase db remote commits
```

---

## Padrões SQL

### Adicionar Coluna

```sql
ALTER TABLE nome_tabela
ADD COLUMN IF NOT EXISTS nome_coluna tipo_campos DEFAULT valor;
```

### Criar Tabela

```sql
CREATE TABLE IF NOT EXISTS nome_tabela (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

COMMENT ON TABLE nome_tabela IS 'Descrição da tabela';
```

### Modificar Coluna

```sql
ALTER TABLE nome_tabela
ALTER COLUMN nome_coluna TYPE novo_tipo;
```

### Adicionar Foreign Key

```sql
ALTER TABLE nome_tabela
ADD CONSTRAINT fk_nome_coluna
FOREIGN KEY (coluna_id) REFERENCES outra_tabela(id)
ON DELETE CASCADE;
```

### Criar Índice

```sql
CREATE INDEX IF NOT EXISTS idx_nome_tabela_coluna
ON nome_tabela(coluna);
```

### Habilitar RLS

```sql
ALTER TABLE nome_tabela ENABLE ROW LEVEL SECURITY;
```

### Criar Policy RLS

```sql
CREATE POLICY "nome_policy" ON nome_tabela
FOR SELECT TO authenticated
USING (true);
```

---

## Tipos de Migrations

### DDL (Data Definition Language)

- CREATE TABLE
- ALTER TABLE
- DROP TABLE
- ADD CONSTRAINT
- CREATE INDEX

### DML (Data Manipulation Language)

- INSERT (seeds)
- UPDATE
- DELETE

⚠️ **CUIDADO:** DML em migrations pode ser perigoso se a migration falhar midway!

---

## Rollback

### Estratégias

1. **Migration Reversa:** Criar migration `revert_XXX_*.sql`
2. **Database Reset:** Último recurso (apaga tudo)

### Comando Rollback

```bash
# Reset local
supabase db reset --local

# Reset remoto (CUIDADO!)
supabase db reset --linked
```

---

## Checklist Antes de Commit

- [ ] Migration segue convenção de nome (XXX_descricao.sql)
- [ ] SQL é idempotente (IF NOT EXISTS, IF EXISTS)
- [ ] Comentários no topo (Descrição, Autor, Data)
- [ ] Testado localmente
- [ ] Rollback documentado (se aplicável)
- [ ] README.md atualizado (se necessário)

---

## Referências Rápidas

| Comando | Descrição |
|---------|-----------|
| `supabase migration new` | Criar nova migration |
| `supabase db push` | Aplicar migrations no remoto |
| `supabase db remote commits` | Ver migrations aplicadas |
| `supabase db reset --local` | Resetar database local |
| `supabase migration list` | Listar migrations locais |

---

## Migrations Atuais

| ID | Arquivo | Status |
|----|---------|--------|
| 001 | revoke_generic_grants.sql | ✅ Aplicada |
| 002 | enable_rls.sql | ✅ Aplicada |
| 003 | create_core_tables.sql | ✅ Aplicada |

---

*Guia de Migrations - Citara Marketing IA*
