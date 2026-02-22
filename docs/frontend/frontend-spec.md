# Frontend Spec - Citara Marketing IA

**Projeto:** Citara Marketing IA
**Data:** 2026-02-22
**Autor:** @ux-design-expert (Uma)
**Status:** ⏭️ N/A - CLI-Only Project

---

## Decisão Arquitetural

### Nenhum Frontend Web Tradicional

Este projeto segue o princípio **CLI First** do AIOS Framework (Constitution, Artigo I).

```
CLI (Máxima) → Observability (Secundária) → UI (Terciária)
```

### Interface Atual

| Componente | Tecnologia | Uso |
|------------|------------|-----|
| **CLI** | Claude Code + Terminal | Interface principal |
| **Documentos** | Markdown | Especificação e docs |
| **Database** | Supabase Dashboard | Admin pontual |

---

## Débitos Identificados (Frontend)

| ID | Débito | Severidade | Esforço | Observação |
|----|--------|------------|---------|------------|
| **UX-001** | Sem UI para gestão visual | Médio | Alto | Por design (CLI First) |
| **UX-002** | Sem dashboard de clientes | Baixo | Alto | Futuro (Observability) |
| **UX-003** | Sem interface para conteúdo | Baixo | Médio | Futuro |

---

## Recomendações

### Fase Atual (CLI-Only)
- ✅ Continuar focando em CLI
- ✅ Documentar comandos e workflows
- ✅ Criar templates de Markdown

### Fase Futura (Observability)
- 📊 Dashboard simples (React/Vite)
- 📈 Visualização de dados de clientes
- 📋 Gerenciador de conteúdo visual

---

## Princípios UI (quando implementado)

| Princípio | Descrição |
|-----------|-----------|
| **CLI First** | TUDO funciona via CLI antes de UI |
| **Non-Bloqueante** | UI nunca bloqueia operações |
| **Read-Only** | UI observa, CLI controla |
| **Progressivo** | UI é camada opcional |

---

*Fim da FASE 3 - Frontend/UX*

⏭️ **PULADO** - Projeto segue CLI First

— Uma, designer de experiência 🎨
