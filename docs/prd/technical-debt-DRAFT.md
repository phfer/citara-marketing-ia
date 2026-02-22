# Technical Debt Assessment - DRAFT

**Projeto:** Citara Marketing IA
**Data:** 2026-02-22
**Status:** PARA REVISÃO DOS ESPECIALISTAS
**Autor:** @architect (Aria)

---

## Executive Summary

Este documento consolida todos os débitos técnicos identificados no projeto Citara Marketing IA.

**Total de Débitos:** 11
- **Críticos:** 4
- **Altos:** 4
- **Médios:** 2
- **Baixos:** 1

---

## 1. Débitos de Sistema

Validado por: @architect (Aria)

| ID | Débito | Impacto | Esforço | Prioridade |
|----|--------|--------|---------|------------|
| **S-001** | Sem aplicação web - trabalho apenas via CLI | Alto | Médio | P1 |
| **S-002** | Sem interface para gestão de clientes | Alto | Alto | P2 |
| **S-003** | Configuração manual de ambiente necessária | Médio | Baixo | P2 |
| **S-004** | Falta de CI/CD configurado | Médio | Médio | P1 |
| **S-005** | Sem testes automatizados | Médio | Médio | P1 |
| **S-006** | Documentação dispersa | Baixo | Baixo | P3 |
| **S-007** | .gitignore pode ser otimizado | Baixo | Baixo | P3 |
| **S-008** | Variáveis de ambiente não documentadas | Baixo | Baixo | P3 |

**Subtotal:** 8 débitos (2 críticos, 3 altos, 3 médios/baixos)

---

## 2. Débitos de Database

Validado por: @data-engineer (Dara)
⚠️ **PENDENTE: Revisão do especialista**

| ID | Débito | Severidade | Esforço | Prioridade |
|----|--------|------------|---------|------------|
| **DB-001** | Schema vazio - nenhuma tabela criada | Crítico | Alto | **P0** |
| **DB-002** | Sem migrations versionadas | Alto | Médio | P1 |
| **DB-003** | RLS policies genéricas (todas permissões) | Crítico | Alto | **P0** |
| **DB-006** | Configurar RLS policies específicas | Alto | Médio | P1 |
| **DB-007** | Testar disaster recovery | Médio | Baixo | P2 |
| **DB-008** | Documentar modelo ERD | Médio | Baixo | P2 |

**Subtotal:** 6 débitos (2 críticos, 2 altos, 2 médios)

---

## 3. Débitos de Frontend/UX

Validado por: @ux-design-expert (Uma)
⚠️ **PENDENTE: Revisão do especialista**

| ID | Débito | Severidade | Esforço | Prioridade |
|----|--------|------------|---------|------------|
| **UX-001** | Sem UI para gestão visual | Médio | Alto | P2 |
| **UX-002** | Sem dashboard de clientes | Baixo | Alto | P3 |
| **UX-003** | Sem interface para conteúdo | Baixo | Médio | P3 |

**Nota:** Débitos de UX são **por design** (CLI First). Não são bloqueadores.

**Subtotal:** 3 débitos (todos baixos/médios - não críticos)

---

## 4. Matriz Preliminar de Priorização

| ID | Débito | Área | Impacto | Esforço | Prioridade |
|----|--------|------|---------|---------|------------|
| DB-001 | Schema vazio | DB | Crítico | Alto | **P0** |
| DB-003 | RLS genéricas | DB | Crítico | Alto | **P0** |
| S-001 | CLI-only | Sistema | Alto | Médio | P1 |
| DB-002 | Sem migrations | DB | Alto | Médio | P1 |
| DB-006 | RLS policies | DB | Alto | Médio | P1 |
| S-004 | Sem CI/CD | Sistema | Médio | Médio | P1 |
| S-005 | Sem testes | Sistema | Médio | Médio | P1 |
| S-002 | Sem gestão clientes | Sistema | Alto | Alto | P2 |
| S-003 | Config manual | Sistema | Médio | Baixo | P2 |
| DB-007 | DR não testado | DB | Médio | Baixo | P2 |
| DB-008 | Sem ERD | DB | Médio | Baixo | P2 |

---

## 5. Perguntas para Especialistas

### Para @data-engineer

1. **DB-001:** Qual a estrutura mínima de tabelas necessária para MVP?
2. **DB-002:** Qual ferramenta de migrations usar? Supabase CLI ou alternativa?
3. **DB-003:** Confirmar se grants genéricos são realmente críticos ou se é padrão Supabase seguro.
4. **DB-006:** Quantas policies RLS são necessárias para MVP?

### Para @ux-design-expert

1. **UX-001:** Confirmar que ausência de UI é aceitável (CLI First).
2. **UX-002/003:** Dashboard deve ser prioridade P2 ou pode ser P3?

---

## 6. Estimativas de Esforço

| Área | Débitos | Horas Estimadas | Custo (R$150/h) |
|------|---------|-----------------|-----------------|
| **Sistema** | 8 | 32h | R$ 4.800 |
| **Database** | 6 | 40h | R$ 6.000 |
| **Frontend** | 3 | 0h* | R$ 0 |
| **TOTAL** | 17 | **72h** | **R$ 10.800** |

*\* Débitos de frontend são por design (CLI First)*

---

## 7. Timeline Recomendada

### Sprint 1: Foundation (2 semanas)
- DB-001: Criar estrutura de tabelas
- DB-003: Configurar RLS policies
- DB-002: Implementar migrations

### Sprint 2: Quality (1 semana)
- S-004: Configurar CI/CD
- S-005: Implementar testes
- S-007/S-008: Documentação

### Sprint 3: Enhancement (1 semana)
- S-002/S-003: Melhorias de sistema
- DB-006/DB-007/DB-008: Database ops

---

*Fim do DRAFT - Aguardando revisão dos especialistas*

— Aria, arquitetando o futuro 🏗️
