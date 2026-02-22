# Supabase Migrations - Citara Marketing IA

**Projeto:** Citara Marketing IA
**Database:** Supabase PostgreSQL
**Versão:** 1.0

---

## Visão Geral

Este diretório contém as migrations do database Supabase do projeto Citara Marketing IA. Migrations são arquivos SQL que versionam e controlam as mudanças no schema do database.

---

## Estrutura

```
supabase/migrations/
├── README.md (este arquivo)
├── 001_revoke_generic_grants.sql
├── 002_enable_rls.sql
├── 003_create_core_tables.sql
└── TIMESTAMP_descrição.sql (futuras)
```

---

## Convenções de Nomenclatura

### Nome de Arquivo

**Formato:** `XXX_descrição_curta.sql`

- `XXX` = Número sequencial de 3 dígitos (001, 002, 003...)
- `descrição_curta` = snake_case descrevendo a mudança
- `.sql` = extensão SQL padrão

**Exemplos:**
- `001_revoke_generic_grants.sql`
- `002_enable_rls.sql`
- `003_create_core_tables.sql`
- `004_add_tags_table.sql`
- `005_insert_seed_data.sql`

### Orden de Execução

As migrations são executadas **em ordem numérica crescente**:
1. 001_*
2. 002_*
3. 003_*
...

---

## Comandos Supabase CLI

### Criar Nova Migration

```bash
# Criar nova migration
supabase migration new nome_da_migration

# Exemplo: supabase migration new add_tags_table
# Cria arquivo: 20240222120000_add_tags_table.sql
```

### Aplicar Migrations

```bash
# Aplicar migrations locais ao database remoto
supabase db push

# Ver status das migrations
supabase db remote commits

# Listar migrations locais não aplicadas
supabase migration list
```

### Rollback

```bash
# Resetar database local (CUIDADO: apaga todos dados)
supabase db reset --local

# Resetar database remoto (CUIDADO: apaga todos dados)
supabase db reset --linked
```

---

## Boas Práticas

### 1. Sempre Criar Migration Nova

```bash
# ❌ ERRADO: Editar migration existente
# Isso quebra o histórico para quem já clonou

# ✅ CORRETO: Criar nova migration
supabase migration new fix_clientes_table
```

### 2. Migrations Devem Ser Idempotentes

```sql
-- ✅ CORRETO: Pode rodar múltiplas vezes
CREATE TABLE IF NOT EXISTS clientes (...);

-- ❌ ERRADO: Falha na segunda execução
CREATE TABLE clientes (...);
```

### 3. Sempre Testar Localmente Primeiro

```bash
# 1. Testar local
supabase db reset --local

# 2. Verificar se tudo funciona
supabase db reset --local --debug

# 3. Depois aplicar no remoto
supabase db push
```

### 4. Descrever Mudanças no Topo do Arquivo

```sql
-- Migration: 004_add_tags_table.sql
-- Description: Adiciona tabela de tags para conteúdos
-- Author: @dev (Dex)
-- Date: 2026-02-22
-- Depends: 003_create_core_tables.sql

-- ... código SQL
```

### 5. Usar IF EXISTS e IF NOT EXISTS

```sql
-- DROP
DROP TABLE IF EXISTS nome_tabela;

-- CREATE
CREATE TABLE IF NOT EXISTS nome_tabela (...);

-- ALTER
ALTER TABLE IF EXISTS nome_tabela ADD COLUMN IF NOT EXISTS nome_coluna TEXT;
```

---

## Histórico de Migrations

| ID | Arquivo | Descrição | Data | Autor |
|----|---------|-----------|------|-------|
| 001 | `001_revoke_generic_grants.sql` | Revoga GRANT ALL genérico | 2026-02-22 | @dev |
| 002 | `002_enable_rls.sql` | Configura framework RLS | 2026-02-22 | @dev |
| 003 | `003_create_core_tables.sql` | Criar tabelas core | 2026-02-22 | @dev |

---

## Rollback Strategy

### Como Fazer Rollback

**Opção 1: Criar migration reversa**

```bash
# Criar migration que desfaz a mudança
supabase migration new revert_003_core_tables

# Adicionar DROP TABLEs
DROP TABLE IF EXISTS conteudos CASCADE;
DROP TABLE IF EXISTS projetos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;
```

**Opção 2: Reset database (último recurso)**

```bash
# CUIDADO: Isso apaga TODOS os dados
supabase db reset --linked
```

### Melhor Prática: Criar Migration Forward/Backward

```sql
-- 004_add_status_column.sql

-- Forward (adiciona coluna)
ALTER TABLE clientes ADD COLUMN IF NOT EXISTS status TEXT DEFAULT 'ativo';

-- Backward (remove coluna) - PARA ROLLBACK
-- ALTER TABLE clientes DROP COLUMN IF EXISTS status;
```

---

## Verificações

### Ver Status das Migrations

```bash
# Ver migrations aplicadas no remoto
supabase db remote commits

# Ver migrations locais
ls -la supabase/migrations/

# Ver schema atual
supabase db remote tables
```

### Ver Tabelas e Estrutura

```bash
# Listar todas as tabelas
psql $DATABASE_URL -c "\dt"

# Ver estrutura de uma tabela
psql $DATABASE_URL -c "\d clientes"
```

---

## Troubleshooting

### Erro: Migration já aplicada

```
Error: Migration already applied
```

**Solução:** A migration já foi aplicada. Continue para a próxima.

### Erro: Conflict com migration remota

```
Error: Remote migration conflicts with local
```

**Solução:** Alinhar com o remoto:
```bash
supabase db remote commit
```

### Erro: Permissão negada

```
Error: permission denied for table
```

**Solução:** Verificar se `service_role` está sendo usado para operações administrativas.

---

## Links Úteis

- [Supabase CLI Docs](https://supabase.com/docs/reference/cli)
- [Supabase Migrations Guide](https://supabase.com/docs/guides/cli/local-development)
- [PostgreSQL Migration Best Practices](https://wiki.postgresql.org/wiki/SQL/Migration)

---

*Última atualização: 2026-02-22*
*Autor: @dev (Dex)*
