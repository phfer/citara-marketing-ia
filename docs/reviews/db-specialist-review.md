# Database Specialist Review

**Projeto:** Citara Marketing IA
**Data:** 2026-02-22
**Revisor:** @data-engineer (Dara)
**Documento Base:** `docs/prd/technical-debt-DRAFT.md`

---

## Veredito: ✅ APROVADO COM AJUSTES

Os débitos de Database identificados no DRAFT estão **corretos e prioritários**.

---

## 1. Débitos Validados

| ID | Débito | Status | Ajuste | Horas | Prioridade |
|----|--------|--------|--------|-------|------------|
| **DB-001** | Schema vazio | ✅ Confirmado | - | 16h | **P0** |
| **DB-002** | Sem migrations | ✅ Confirmado | Reduzir esforço | 4h | P1 |
| **DB-003** | RLS genéricas | ✅ Confirmado | - | 6h | **P0** |
| **DB-006** | RLS policies | ✅ Confirmado | Parte do DB-001 | 0h | P1 |
| **DB-007** | DR não testado | ✅ Confirmado | - | 2h | P2 |
| **DB-008** | Sem ERD | ✅ Confirmado | - | 3h | P2 |

**Ajustes:**
- DB-006 foi absorvido pelo DB-001 (fazer junto)
- DB-002: Supabase CLI já tem migrations, esforço menor

---

## 2. Débitos Adicionais

| ID | Débito | Severidade | Horas | Prioridade |
|----|--------|------------|-------|------------|
| **DB-009** | Sem connection pooling configurado | Médio | 1h | P2 |
| **DB-010** | Falta definir tipo de dados para moeda BRL | Baixo | 1h | P3 |

---

## 3. Respostas ao Architect

### P1: Qual estrutura mínima de tabelas para MVP?

**Resposta:** Para um sistema de gestão de agência com clientes:

```sql
-- Core entities
clientes (id, nome, ticket_mensal, status, created_at)
projetos (id, cliente_id, nome, tipo, status, created_at)
conteudos (id, projeto_id, tipo, plataforma, status, url, created_at)
usuarios (id, nome, email, role, created_at)

-- Metadata
tags (id, nome, cor)
tags_relacionadas (conteudo_id, tag_id)
```

### P2: Qual ferramenta de migrations?

**Resposta:** **Supabase CLI** (já instalado).
```bash
supabase migration new nome_da_migration
supabase db push
```

### P3: Grants genéricos são realmente críticos?

**Resposta:** **SIM**. O padrão `GRANT ALL` no Supabase é perigoso porque:
- Permite `DELETE` em `anon` role
- Permite `DROP TABLE` em `service_role`
- Viola princípio do menor privilégio

**Ação imediata:** Revoke e aplicar políticas específicas.

### P4: Quantas policies RLS para MVP?

**Resposta:** Mínimo de **8 policies**:
- `clientes`: SELECT (authenticated), INSERT/UPDATE (admin)
- `projetos`: SELECT (authenticated), INSERT/UPDATE/DELETE (admin)
- `conteudos`: SELECT (authenticated), INSERT/UPDATE/DELETE (admin)
- `usuarios`: SELECT (self), INSERT/UPDATE (self)

---

## 4. Estimativas Atualizadas

| Débito | Horas Originais | Horas Revisadas | Justificativa |
|--------|----------------|-----------------|---------------|
| DB-001 | 16h | 16h | Mantida |
| DB-002 | 8h | 4h | CLI já tem suporte |
| DB-003 | 6h | 6h | Mantida |
| DB-006 | 4h | 0h | Absorvido pelo DB-001 |
| DB-007 | 2h | 2h | Mantida |
| DB-008 | 4h | 3h | Documentação simples |
| DB-009 | - | 1h | Novo |
| DB-010 | - | 1h | Novo |
| **TOTAL** | **40h** | **33h** | **-7h** |

---

## 5. Priorização (Perspectiva Database)

| Ordem | ID | Débito | Justificativa |
|-------|----|--------|---------------|
| 1 | DB-003 | RLS genéricas | **Segurança crítica** - fazer antes de tudo |
| 2 | DB-001 | Schema vazio | Bloqueia qualquer funcionalidade |
| 3 | DB-002 | Migrations | Necessário antes de produção |
| 4 | DB-008 | ERD | Documentação guia desenvolvimento |
| 5 | DB-007 | DR test | Segurança, mas não bloqueia |
| 6 | DB-009 | Pooling | Performance, ajuste quando necessário |
| 7 | DB-010 | Tipo moeda | Detalhe, pode ajustar depois |

---

## 6. Recomendações

### Imediatas (Esta semana)

1. **DB-003:** Revoke `GRANT ALL` e aplicar policies mínimas
2. **DB-001:** Criar tabelas core (clientes, projetos, conteudos)

### Curto Prazo (2 semanas)

3. **DB-002:** Configurar estrutura de migrations
4. **DB-008:** Criar ERD no Mermaid

### Médio Prazo

5. **DB-007:** Testar restore
6. **DB-009:** Configurar pooling
7. **DB-010:** Definir tipos para BRL

---

## 7. Queries Exemplo (para implementação)

### Criar tabelas core:
```sql
-- Clientes
CREATE TABLE clientes (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    ticket_mensal DECIMAL(10,2),
    status TEXT DEFAULT 'ativo',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE clientes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Clientes select authenticated"
    ON clientes FOR SELECT
    TO authenticated
    USING (true);

CREATE POLICY "Clientes insert admin"
    ON clientes FOR INSERT
    TO authenticated
    WITH CHECK (auth.jwt() ->> 'role' = 'admin');
```

---

— Dara, arquiteta de dados 🗄️
