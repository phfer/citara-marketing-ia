# System Architecture - Citara Marketing IA

**Data:** 2026-02-22
**Versão:** 1.0
**Autor:** @architect (Aria)
**Projeto:** Citara Marketing IA - Sistema de Gestão de Agência com AIOS

---

## Executive Summary

O **Citara Marketing IA** é um sistema de gestão para agência de marketing digital que utiliza o framework **AIOS (Synkra AIOS v4.2.13)** para orquestração de agentes de IA. O projeto está em fase inicial de configuração, sem aplicação web propriamente dita - foca na organização de conteúdo para clientes e automação de processos.

**Tipo de Projeto:** Framework-based Management System
**Stack Principal:** AIOS Framework + Node.js + GitHub
**Complexidade:** Baixa a Média
**Maturity:** Configuração Inicial

---

## 1. Stack Tecnológico

### 1.1 Core Framework

| Componente | Versão | Propósito |
|-------------|--------|----------|
| **AIOS Framework** | 4.2.13 | Orquestração de agentes de IA |
| **Node.js** | 24.13.0 | Runtime JavaScript |
| **npm** | 11.6.2 | Gerenciador de pacotes |
| **pnpm** | 10.28.2 | Alternativa rápida (opcional) |

### 1.2 Infraestrutura

| Ferramenta | Versão | Uso |
|------------|--------|-----|
| **Git** | 2.50.1 | Controle de versão |
| **GitHub CLI** | 2.86.0 | Operações GitHub |
| **Docker** | 28.5.1 | Containers (disponível) |
| **Supabase** | 2.75.0 | Database/Backend (configurado) |
| **Railway** | 4.30.3 | Deploy (opcional) |

### 1.3 IDE & Ferramentas

- **Claude Code** - IDE principal para desenvolvimento
- **VS Code** - Edição tradicional (suportado)
- **GitHub** - https://github.com/phfer/citara-marketing-ia

---

## 2. Estrutura de Pastas

```
Cítara Marketing/
├── .aios-core/                    # AIOS Framework v4.2.13
│   ├── constitution.md           # Princípios NON-NEGOTIABLE
│   ├── core/                     # Módulo runtime central
│   ├── development/             # 200+ tasks, workflows, agentes
│   ├── product/                  # Templates e checklists
│   └── infrastructure/           # Configurações de infra
│
├── .claude/                       # Claude Code configs
│   ├── CLAUDE.md                 # Documento principal do projeto
│   ├── CITARA.md                 # Contexto da agência
│   └── rules/                    # Regras específicas (6 arquivos)
│
├── clientes/                     # Área de trabalho dos clientes
│   ├── EMASFI/                   # Serviços Fiscais B2B
│   ├── Tulum Residence/          # Luxury Real Estate
│   └── FIREVON/                  # Consultoria B2B
│
├── .agent/                        # Workflows de agentes
├── .antigravity/                 # Configurações adicionais
├── .codex/                       # Codex configs
├── .aios/                        # Relatórios de ambiente
│   └── environment-report.yaml   # Status das ferramentas
│
├── .env                           # Variáveis de ambiente (não commitado)
├── .env.example                   # Template de variáveis
├── .gitignore                     # Regras de ignore
├── AGENTS.md                      # Documentação de agentes
└── .git/                          # Repositório Git
```

---

## 3. Arquitetura do Sistema

### 3.1 Visão Geral

```
┌─────────────────────────────────────────────────────────────────┐
│                      CLAUDE CODE (IDE)                         │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                   AIOS Framework v4.2.13                   │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │ │
│  │  │   @pm        │  │    @po       │  │    @sm       │    │ │
│  │  │  (Bob)       │  │   (Pax)      │  │  (River)     │    │ │
│  │  │  PRDs, Epics │  │  Stories     │  │  Story Flow  │    │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘    │ │
│  │                                                              │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │ │
│  │  │ @architect  │  │    @dev      │  │     @qa      │    │ │
│  │  │  (Aria)      │  │   (Dex)      │  │  (Quinn)     │    │ │
│  │  │  Architecture │  │  Code        │  │  Quality     │    │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘    │ │
│  │                                                              │ │
│  │  ┌──────────────┐                                          │ │
│  │  │  @devops     │  ← EXCLUSIVE: Git Push, PRs, Releases   │ │
│  │  │  (Gage)      │                                          │ │
│  │  └──────────────┘                                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                   CLI Tools & Infrastructure                │ │
│  │  Git | GitHub | Supabase | Docker | Railway               │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Fluxo de Trabalho AIOS

```
1. @pm (Bob) → Cria PRD e Epic
       ↓
2. @sm (River) → Cria Stories a partir do Epic
       ↓
3. @po (Pax) → Valida stories (checklist 10 pontos)
       ↓
4. @dev (Dex) → Implementa código (YOLO/Interactive/Pre-Flight)
       ↓
5. @qa (Quinn) → Quality Gate (7 checks)
       ↓
6. @devops (Gage) → Push para GitHub, cria PR
```

---

## 4. Database & Backend

### 4.1 Supabase Configurado

- **URL:** `uzphwscfdjjiniicjgan.supabase.co`
- **Projetos:** 6 projetos configurados
- **Principal:** Citara Marketing (fotizvfbsyllvycswwuh)

### 4.2 Projetos Supabase Identificados

| Projeto | ID | Região | Propósito |
|---------|----|--------|----------|
| Citara Marketing | fotizvfbsyllvycswwuh | São Paulo | Principal |
| aios-cs | zksduwmxcalbszjbulkw | São Paulo | AIOS Code |
| Agente N8N | abenkhuryommierafegx | São Paulo | Automação |
| N8N | qldfjllfsqroahrghrwv | Oregon | Automação |
| Solo Levelling | vkaosiscjathevmhiqpc | São Paulo | Cliente |
| t3phfe@gmail.com | qphppyddgcwshrjaqarx | São Paulo | Pessoal |

---

## 5. Cliente Context

### 5.1 Clientes Ativos

| Cliente | Ticket | Perfis | Status |
|---------|--------|--------|--------|
| GRUPO BAUEN | R$ 25.000 | 7 perfis | Ativo |
| EMASFI | R$ 8.000 | 5 perfis | Ativo |
| PRX | R$ 5.000 | 5 perfis | Ativo |
| Instituto Pamplona | R$ 2.500 | - | Ativo |
| Nacional | R$ 2.000 | - | Ativo |
| Tulum Residence | - | - | Ativo |

### 5.2 Contexto por Cliente

Cada cliente possui pasta própria em `clientes/` com:
- Documentos estratégicos
- Materiais de marketing
- Configuração específica (`.claude/CLIENTE.md`)
- Histórico de conversas

---

## 6. Dependências e Integrações

### 6.1 Dependências Principais

```json
{
  "AIOS Framework": "4.2.13",
  "Node.js": "24.13.0",
  "GitHub": "phfer/citara-marketing-ia",
  "Supabase": "2.75.0"
}
```

### 6.2 Integrações Externas

- **ClickUp:** Gestão de tarefas (API token configurado)
- **GitHub:** Controle de versão e colaboração
- **Supabase:** Database e backend services
- **Claude API:** Agente de IA principal

---

## 7. Débitos Identificados (Nível Sistema)

### 7.1 Críticos

| ID | Débito | Impacto | Esforço |
|----|--------|--------|---------|
| S-001 | Sem aplicação web - trabalho apenas via CLI | Alto | Médio |
| S-002 | Sem interface para gestão de clientes | Alto | Alto |
| S-003 | Configuração manual de ambiente necessária | Médio | Baixo |

### 7.2 Médios

| ID | Débito | Impacto | Esforço |
|----|--------|--------|---------|
| S-004 | Falta de CI/CD configurado | Médio | Médio |
| S-005 | Sem testes automatizados | Médio | Médio |
| S-006 | Documentação dispersa | Baixo | Baixo |

### 7.3 Baixos

| ID | Débito | Impacto | Esforço |
|----|--------|--------|---------|
| S-007 | .gitignore pode ser otimizado | Baixo | Baixo |
| S-008 | Variáveis de ambiente não documentadas | Baixo | Baixo |

---

## 8. Padrões de Código

### 8.1 Convenções Estabelecidas

- **Nome de arquivos:** `kebab-case`
- **Nome de componentes:** `PascalCase`
- **Constants:** `SCREAMING_SNAKE_CASE`
- **Imports:** Preferir `@/` (absolute imports)

### 8.2 Princípios AIOS (Constitution)

| Artigo | Princípio | Status |
|--------|-----------|--------|
| I | CLI First | ✅ Seguido |
| II | Agent Authority | ✅ Seguido |
| III | Story-Driven Development | ✅ Seguido |
| IV | No Invention | ✅ Seguido |
| V | Quality First | ⚠️ Parcial |
| VI | Absolute Imports | ⚠️ Parcial |

---

## 9. Performance & Escalabilidade

### 9.1 Estado Atual

- **Performance:** N/A (sem app web)
- **Escalabilidade:** Limitada a uso local/CLI
- **Monitoring:** Não configurado

### 9.2 Recursos Disponíveis

- **Database:** Supabase (escala automática)
- **Hosting:** Pode usar Railway (CLI configurado)
- **CDN:** Não configurado

---

## 10. Segurança

### 10.1 Medidas Atuais

| Medida | Status | Observação |
|--------|--------|------------|
| Variáveis de ambiente | ✅ | .gitignore configurado |
| Segredos no repo | ❌ | Verificar se há secrets |
| RLS policies | ⚠️ | Depende de análise Supabase |
| Autenticação GitHub | ✅ | Token configurado |

### 10.2 Riscos Identificados

- **R1:** `.env` expõe estrutura - pode conter secrets reais
- **R2:** Tokens de API não rotacionados
- **R3:** Sem política de commits assinados

---

## 11. Próximos Passos (Recomendações)

### 11.1 Imediatos (Quick Wins)

1. **Verificar secrets no repo** - Scan por tokens expostos
2. **Configurar CI básico** - GitHub Actions para lint/test
3. **Documentar variáveis de ambiente** - Criar guide de setup

### 11.2 Curto Prazo (1-2 semanas)

1. **Implementar aplicação web** - Interface de gestão
2. **Configurar testes automatizados** - Vitest/Jest
3. **Setup CI/CD completo** - Quality gates

### 11.3 Médio Prazo (2-4 semanas)

1. **Dashboard de clientes** - Visualização de dados
2. **Automação de workflows** - N8N integration
3. **Monitoring e alertas** - Sentry/Grafana

---

## 12. Anexos

### 12.1 Links Importantes

- **Repo:** https://github.com/phfer/citara-marketing-ia
- **Supabase:** https://supabase.com/dashboard/project/fotizvfbsyllvycswwuh
- **AIOS Docs:** `.aios-core/user-guide.md`
- **Constitution:** `.aios-core/constitution.md`

### 12.2 Comandos Úteis

```bash
# Ver status do ambiente
cat .aios/environment-report.yaml

# Listar clientes
ls clientes/

# Ver configuração AIOS
cat .aios-core/core-config.yaml

# Ver projects Supabase
supabase projects list
```

---

**Fim da FASE 1 - Análise do Sistema**

*Próxima fase:* @data-engineer para análise de Database (se aplicável)

— Aria, arquitetando o futuro 🏗️
