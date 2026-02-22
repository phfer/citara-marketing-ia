# DB-AUDIT.md - Security & Performance Audit

**Projeto:** Citara Marketing
**Database:** Supabase PostgreSQL
**Data:** 2026-02-22
**Autor:** @data-engineer (Dara)
**Tipo:** Security Audit + Performance Review

---

## Executive Summary

| Aspecto | Status | Score | Notas |
|---------|--------|-------|-------|
| **Segurança** | 🔴 CRÍTICO | 1/5 | Schema vazio + grants genéricos |
| **Performance** | ⚪ N/A | - | Sem tabelas para analisar |
| **Manutenibilidade** | 🟡 MÉDIO | 3/5 | Sem migrations/versionamento |
| **Compliance** | 🟡 MÉDIO | 3/5 | RLS padrão aplicado |

**Score Geral:** 2/5 - **Requer Atenção Imediata**

---

## 1. Security Audit

### 1.1 Authentication & Authorization

| Item | Status | Risco | Recomendação |
|------|--------|-------|--------------|
| Row Level Security | ⚠️ Padrão | Alto | Implementar policies específicas |
| Role-based access | ⚠️ Genérico | Alto | Customizar por função |
| Anonymous access | ✅ Configurado | Médio | Revisar necessidade |
| Service role | ✅ Configurado | Baixo | OK |

**CRÍTICO - Grants Genéricos:**
```sql
-- ⚠️ RISCO: Permissões excessivas
GRANT ALL ON TABLES TO anon;
GRANT ALL ON TABLES TO authenticated;
GRANT ALL ON TABLES TO service_role;
```

**Recomendação:**
```sql
-- ✅ MELHOR: Princípio do menor privilégio
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM anon, authenticated, service_role;

-- Depois conceder apenas o necessário
GRANT SELECT ON TABLE clientes TO authenticated;
GRANT SELECT, INSERT ON TABLE conteudos TO authenticated;
```

### 1.2 RLS Policies (Row Level Security)

| Tabela | RLS Ativo | Policies | Status |
|--------|-----------|----------|--------|
| (nenhuma) | - | - | ⚠️ Schema vazio |

**Recomendação:** Habilitar RLS em TODAS as tabelas após criação.

### 1.3 Secrets Management

| Item | Status | Observação |
|--------|--------|------------|
| `.env` gitignored | ✅ | Correto |
| Hardcoded secrets | ❌ | Verificar código |
| Rotation policy | ❌ | Não implementada |

---

## 2. Performance Audit

### 2.1 Índices

**Status:** N/A - Schema vazio

**Recomendações futuras:**
- Criar índices em foreign keys
- Índices em colunas de busca/filtro
- Considerar índices parciais para dados grandes

### 2.2 Queries

**Status:** N/A - Sem tabelas, sem queries

### 2.3 Connection Pooling

| Item | Status | Observação |
|--------|--------|------------|
| PgBouncer | ❓ | Verificar config Supabase |
| Pool size | ❓ | Configurar por load esperado |

---

## 3. Data Integrity

### 3.1 Constraints

**Status:** N/A - Schema vazio

**Recomendações futuras:**
```sql
-- Primary keys em TODAS as tabelas
id SERIAL PRIMARY KEY

-- Foreign keys com ON DELETE
cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE

-- Unique constraints onde aplicável
email VARCHAR(255) UNIQUE NOT NULL

-- Check constraints para validação
valor DECIMAL(10,2) CHECK (valor >= 0)
```

### 3.2 Normalization

**Status:** N/A - Sem tabelas para analisar

**Recomendação:** Seguir pelo menos 3NF (Third Normal Form).

### 3.3 Data Types

| Categoria | Tipo Recomendado | Observação |
|-----------|------------------|------------|
| IDs | `BIGSERIAL` | Auto-incremento 64-bit |
| Moedas | `DECIMAL(10,2)` | Precisão financeira |
| Timestamps | `TIMESTAMPTZ` | Com timezone |
| JSON | `JSONB` | Binário, mais rápido |
| Emails | `VARCHAR(255)` | Com validação app-level |

---

## 4. Backup & Recovery

| Item | Status | Observação |
|--------|--------|------------|
| Automated backups | ✅ Supabase | Verificar retention |
| Point-in-time recovery | ✅ Supabase | Até 30 dias |
| Disaster recovery tested | ❌ | Nunca testado |

---

## 5. Monitoring & Observability

| Item | Status | Observação |
|--------|--------|------------|
| Query logging | ❓ | Verificar Supabase dashboard |
| Performance metrics | ❓ | Configurar alertas |
| Slow query log | ❓ | Habilitar threshold |

---

## 6. Débitos Priorizados

| Prioridade | ID | Débito | Esforço | Impacto |
|------------|----|--------|---------|---------|
| **P0** | DB-003 | Remover grants genéricos `GRANT ALL` | 2h | Crítico |
| **P0** | DB-001 | Criar estrutura de tabelas | 8h | Crítico |
| **P1** | DB-002 | Implementar migrations | 4h | Alto |
| **P1** | DB-006 | Configurar RLS policies | 4h | Alto |
| **P2** | DB-007 | Testar disaster recovery | 2h | Médio |
| **P2** | DB-008 | Documentar modelo ERD | 2h | Médio |

---

## 7. Checklist de Segurança

- [ ] Remover `GRANT ALL` genérico
- [ ] Habilitar RLS em todas as tabelas
- [ ] Implementar políticas por role
- [ ] Adicionar constraints (PK, FK, Unique, Check)
- [ ] Configurar índices apropriados
- [ ] Versionar migrations
- [ ] Testar restore de backup
- [ ] Documentar modelo de dados

---

## 8. Perguntas para @architect

1. **Qual a entidade principal do sistema?** (Clientes, Projetos, Conteúdos?)
2. **Como será o controle de acesso?** (Multi-tenant? Single-tenant?)
3. **Qual o volume esperado de dados?** (Para planejar particionamento)
4. **Há necessidade de busca full-text?** (Para considerar PostgreSQL FTS)
5. **Relatórios/Analytics serão no DB ou app?** (Para considerar materialized views)

---

*Fim do DB-AUDIT*

— Dara, arquiteta de dados 🗄️
