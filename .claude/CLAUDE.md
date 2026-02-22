# CLAUDE.md

Este arquivo fornece orientação para o Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Visão Geral do Projeto

Este é um projeto **Synkra AIOS v4.2.13** - um meta-framework de desenvolvimento full stack orientado por agentes de IA. O AIOS implementa uma metodologia ágil única com dois estágios principais: **Planejamento Agêntico** e **Desenvolvimento Contextualizado por Engenharia**.

### Estrutura Principal

```
.aios-core/
├── constitution.md              # Princípios fundamentais (NON-NEGOTIABLE)
├── core-config.yaml             # Configuração central do projeto
├── user-guide.md                # Guia completo do usuário
├── working-in-the-brownfield.md # Guia para projetos legados
├── core/                        # Módulo runtime central
│   ├── config/                  # Gerenciamento de configuração
│   ├── elicitation/             # Sistema de prompting interativo
│   ├── session/                 # Gerenciamento de contexto de sessão
│   ├── orchestration/           # Orquestração de workflows
│   ├── quality-gates/           # Sistema de 3 camadas de quality gates
│   ├── ids/                     # Sistema Incremental Development
│   ├── synapse/                 # Sistema de conexão entre componentes
│   └── registry/                # Registro de entidades reutilizáveis
├── development/
│   ├── agents/                  # 11 agentes especializados (md)
│   ├── tasks/                   # 200+ tasks executáveis (md)
│   ├── workflows/               # Workflows multi-step (yaml)
│   ├── templates/               # Templates de documentos (yaml/md/hbs)
│   ├── checklists/              # Checklists de validação (md)
│   └── scripts/                 # Scripts utilitários (js/sh)
├── product/
│   ├── templates/               # Templates de produtos e componentes
│   └── checklists/              # Checklists de produto
├── infrastructure/              # Configurações de infraestrutura
├── data/                        # Knowledge base e padrões
└── manifests/                   # Manifestos de componentes
```

---

## Constituição AIOS - Princípios Fundamentais

O arquivo `.aios-core/constitution.md` define os princípios **NON-NEGOTIABLE**:

| Artigo | Princípio | Severidade | Descrição |
|--------|-----------|------------|-----------|
| I | CLI First | NON-NEGOTIABLE | CLI é a fonte da verdade (CLI > Observability > UI) |
| II | Agent Authority | NON-NEGOTIABLE | Cada agente tem autoridades exclusivas |
| III | Story-Driven Development | MUST | Todo desenvolvimento começa com uma story |
| IV | No Invention | MUST | Especificações derivam de requisitos, não inventam |
| V | Quality First | MUST | Múltiplos gates antes de merge |
| VI | Absolute Imports | SHOULD | Preferir imports absolutos `@/` |

### CLI First - Hierarquia de Prioridades

```
CLI (Máxima) → Observability (Secundária) → UI (Terciária)
```

**Regras:**
- MUST: Toda funcionalidade nova DEVE funcionar 100% via CLI antes de qualquer UI
- MUST: Dashboards apenas observam, NUNCA controlam ou tomam decisões
- MUST: A UI NUNCA é requisito para operação do sistema

---

## Sistema de Agentes

### Agentes Principais (11)

| Atalho | Agente | Persona | Responsabilidade |
|--------|--------|---------|------------------|
| `@aios-master` | Orion | Orchestrator | Executor universal, framework dev |
| `@pm` | Bob | Project Manager | PRDs, roadmap, epics |
| `@po` | Pax | Product Owner | Stories, backlog, validação |
| `@sm` | River | Scrum Master | Criação de stories |
| `@architect` | Aria | Architect | Arquitetura e design técnico |
| `@dev` | Dex | Developer | Implementação de código |
| `@qa` | Quinn | QA | Testes e qualidade |
| `@devops` | Gage | DevOps | CI/CD, git push (EXCLUSIVO) |
| `@analyst` | Alex | Analyst | Pesquisa e análise |
| `@data-engineer` | Dara | Data Engineer | Database design |
| `@ux-design-expert` | Uma | UX | Design UI/UX |

### Autoridades Exclusivas (NON-NEGOTIABLE)

#### @devops (Gage) — EXCLUSIVE Authority

| Operation | Exclusive? | Other Agents |
|-----------|-----------|--------------|
| `git push` / `git push --force` | YES | BLOCKED |
| `gh pr create` / `gh pr merge` | YES | BLOCKED |
| MCP add/remove/configure | YES | BLOCKED |
| CI/CD pipeline management | YES | BLOCKED |
| Release management | YES | BLOCKED |

#### Outras Autoridades

| Agente | Operação Exclusiva |
|--------|-------------------|
| @pm | `*execute-epic`, `*create-epic`, EPIC execution |
| @po | `*validate-story-draft`, Story context tracking |
| @sm | `*draft` / `*create-story`, Story template selection |
| @architect | System architecture decisions, Technology selection |
| @data-engineer | Schema design (detailed DDL), Query optimization |
| @qa | Quality verdicts, Gate decisions |

### Cross-Agent Delegation Patterns

```
Git Push: ANY agent → @devops *push
Schema Design: @architect (decides) → @data-engineer (implements DDL)
Story Flow: @sm *draft → @po *validate → @dev *develop → @qa *qa-gate → @devops *push
Epic Flow: @pm *create-epic → @pm *execute-epic → @sm *draft (per story)
```

### Escalation Rules

1. Agent cannot complete task → Escalate to @aios-master
2. Quality gate fails → Return to @dev with specific feedback
3. Constitutional violation detected → BLOCK, require fix before proceed
4. Agent boundary conflict → @aios-master mediates

---

## Workflows Principais

**Princípio: Workflows são compostos por tasks conectadas, não por agentes conectados.** Cada task define seus inputs, outputs, pre/post-conditions e execution modes.

### 1. Story Development Cycle (SDC) — PRIMARY

Full 4-phase workflow para todo desenvolvimento:

```
Phase 1: Create (@sm) → Phase 2: Validate (@po) → Phase 3: Implement (@dev) → Phase 4: QA Gate (@qa)
```

#### Phase 1: Create (@sm)
- **Task:** `create-next-story.md`
- **Inputs:** PRD sharded, epic context
- **Output:** `{epicNum}.{storyNum}.story.md`
- **Status:** Draft

#### Phase 2: Validate (@po)
- **Task:** `validate-next-story.md`
- **10-point checklist** (ver Story Lifecycle abaixo)
- **Decision:** GO (>=7) or NO-GO (<7)

#### Phase 3: Implement (@dev)
- **Task:** `dev-develop-story.md`
- **Modes:** Interactive / YOLO / Pre-Flight
- **CodeRabbit:** Self-healing max 2 iterations
- **Status:** Ready → InProgress

#### Phase 4: QA Gate (@qa)
- **Task:** `qa-gate.md`
- **7 quality checks** (ver Story Lifecycle abaixo)
- **Decision:** PASS / CONCERNS / FAIL / WAIVED
- **Status:** InProgress → InReview → Done

### 2. QA Loop — ITERATIVE REVIEW

Ciclo iterativo de review-fix após QA gate inicial:

```
@qa review → verdict → @dev fixes → re-review (max 5 iterations)
```

**Commands:**
- `*qa-loop {storyId}` — Start loop
- `*qa-loop-review` — Resume from review
- `*qa-loop-fix` — Resume from fix
- `*stop-qa-loop` — Pause, save state
- `*resume-qa-loop` — Resume from state
- `*escalate-qa-loop` — Force manual escalation

**Verdicts:**
- APPROVE → Complete, mark Done
- REJECT → @dev fixes, re-review
- BLOCKED → Escalate immediately

### 3. Spec Pipeline — PRE-IMPLEMENTATION

Transforma requisitos informais em especificação executável:

| Phase | Agent | Output | Skip If |
|-------|-------|--------|---------|
| 1. Gather | @pm | `requirements.json` | Never |
| 2. Assess | @architect | `complexity.json` | source=simple |
| 3. Research | @analyst | `research.json` | SIMPLE class |
| 4. Write Spec | @pm | `spec.md` | Never |
| 5. Critique | @qa | `critique.json` | Never |
| 6. Plan | @architect | `implementation.yaml` | If APPROVED |

**Complexity Classes:**
- SIMPLE (<=8): gather → spec → critique (3 fases)
- STANDARD (9-15): All 6 phases
- COMPLEX (>=16): 6 phases + revision cycle

**5 Complexity Dimensions (scored 1-5):**
- Scope, Integration, Infrastructure, Knowledge, Risk

**Constitutional Gate (Article IV — No Invention):**
Every statement in spec.md MUST trace to FR-*, NFR-*, CON-*, or research finding. NO invented features.

### 4. Brownfield Discovery — LEGACY ASSESSMENT

Avaliação de 10 fases para código legado existente:

**Data Collection (Phases 1-3):**
- Phase 1: @architect → `system-architecture.md`
- Phase 2: @data-engineer → `SCHEMA.md` + `DB-AUDIT.md`
- Phase 3: @ux-design-expert → `frontend-spec.md`

**Draft & Validation (Phases 4-7):**
- Phase 4: @architect → `technical-debt-DRAFT.md`
- Phase 5: @data-engineer → `db-specialist-review.md`
- Phase 6: @ux-design-expert → `ux-specialist-review.md`
- Phase 7: @qa → `qa-review.md` (QA Gate: APPROVED | NEEDS WORK)

**Finalization (Phases 8-10):**
- Phase 8: @architect → `technical-debt-assessment.md` (final)
- Phase 9: @analyst → `TECHNICAL-DEBT-REPORT.md` (executive)
- Phase 10: @pm → Epic + stories ready for development

---

## Story Lifecycle — Detalhado

### Status Progression

```
Draft → Ready → InProgress → InReview → Done
```

| Status | Trigger | Agent | Action |
|--------|---------|-------|--------|
| Draft | @sm creates story | @sm | Story file created |
| Ready | @po validates (GO) | @po | **MUST update status field Draft → Ready** |
| InProgress | @dev starts implementation | @dev | Update status field |
| InReview | @dev completes, @qa reviews | @qa | Update status field |
| Done | @qa PASS, @devops pushes | @devops | Update status field |

**CRITICAL:** The `Draft → Ready` transition is the responsibility of @po during `*validate-story-draft`. When verdict is GO, @po MUST update the story's Status field to `Ready` and log the transition in the Change Log.

### 10-Point Validation Checklist (@po)

1. Clear and objective title
2. Complete description (problem/need explained)
3. Testable acceptance criteria (Given/When/Then preferred)
4. Well-defined scope (IN and OUT clearly listed)
5. Dependencies mapped (prerequisite stories/resources)
6. Complexity estimate (points or T-shirt sizing)
7. Business value (benefit to user/business clear)
8. Risks documented (potential problems identified)
9. Criteria of Done (clear definition of complete)
10. Alignment with PRD/Epic (consistency with source docs)

### Execution Modes (@dev)

**YOLO (autonomous):**
- 0-1 prompts
- Decisions logged in `decision-log-{story-id}.md`
- Best for: simple, deterministic tasks

**Interactive (default):**
- 5-10 prompts with educational checkpoints
- Confirmations at key decision points
- Best for: learning, complex decisions

**Pre-Flight (plan-first):**
- All questions upfront (10-15 prompts)
- Generates execution plan
- Then zero-ambiguity execution
- Best for: ambiguous requirements, critical work

### 7 Quality Checks (@qa)

1. **Code review** — patterns, readability, maintainability
2. **Unit tests** — adequate coverage, all passing
3. **Acceptance criteria** — all met per story AC
4. **No regressions** — existing functionality preserved
5. **Performance** — within acceptable limits
6. **Security** — OWASP basics verified
7. **Documentation** — updated if necessary

### Gate Decisions (@qa)

| Decision | Score | Action |
|----------|-------|--------|
| PASS | All checks OK | Approve, proceed to @devops push |
| CONCERNS | Minor issues | Approve with observations documented |
| FAIL | HIGH/CRITICAL issues | Return to @dev with feedback |
| WAIVED | Issues accepted | Approve with waiver documented (rare) |

### Story File Update Rules

| Section | Who Can Edit |
|---------|-------------|
| Title, Description, AC, Scope | @po only |
| File List, Dev Notes, checkboxes | @dev |
| QA Results | @qa only |
| Change Log | Any agent (append only) |

---

## Sistema de Quality Gates (3 Camadas)

Configuração em `.aios-core/core/quality-gates/quality-gate-config.yaml`

### Layer 1: Pre-commit (local)
- `npm run lint` - ESLint
- `npm run typecheck` - TypeScript
- `npm test` - Testes unitários
- Cobertura mínima: 80%

### Layer 2: PR Automation
- CodeRabbit (auto-fix CRITICAL/HIGH)
- Quinn (@qa) auto-review

### Layer 3: Human Review
- Revisão estratégica obrigatória
- Checklist de aprovação
- Sign-off exigido

---

## CodeRabbit Integration

### Dev Phase (@dev — Story Development Cycle Phase 3)

```yaml
mode: light
max_iterations: 2
timeout_minutes: 30
severity_filter: [CRITICAL, HIGH]
behavior:
  CRITICAL: auto_fix
  HIGH: auto_fix (iteration < 2) else document_as_debt
  MEDIUM: document_as_debt
  LOW: ignore
```

**Flow:**
```
RUN CodeRabbit → CRITICAL found?
  YES → auto-fix (iteration < 2) → Re-run
  NO → Document HIGH as debt, proceed
After 2 iterations with CRITICAL → HALT, manual intervention
```

### QA Phase (@qa — QA Loop Pre-Review)

```yaml
mode: full
max_iterations: 3
timeout_minutes: 30
severity_filter: [CRITICAL, HIGH]
behavior:
  CRITICAL: auto_fix
  HIGH: auto_fix
  MEDIUM: document_as_debt
  LOW: ignore
```

### Severity Handling Summary

| Severity | Dev Phase | QA Phase |
|----------|-----------|----------|
| CRITICAL | auto_fix, block if persists | auto_fix, block if persists |
| HIGH | auto_fix, document if fails | auto_fix, document if fails |
| MEDIUM | document_as_tech_debt | document_as_tech_debt |
| LOW | ignore | ignore |

---

## Sistema IDS (Incremental Development)

Decisões hierárquicas: **REUSE > ADAPT > CREATE**

### REUSE (Relevance >= 90%)
- Use existing artifact directly without modification
- Import/reference existing entity
- No justification needed beyond confirming match

### ADAPT (Relevance 60-89%)
- Adaptability score >= 0.6
- Changes MUST NOT exceed 30% of original artifact
- Changes MUST NOT break existing consumers (check usedBy list)
- Document changes in artifact's change log
- Update registry relationships
- Impact analysis required

### CREATE (No suitable match)
Required justification:
- `evaluated_patterns`: Existing entities you considered
- `rejection_reasons`: Why each was rejected (technical reasons)
- `new_capability`: What unique capability this provides
- Register in Entity Registry within 24 hours
- Establish relationships with existing entities
- Define adaptability constraints for future reuse

### Verification Gates G1-G6

| Gate | Agente | Tipo | Propósito | Blocking |
|------|--------|------|-----------|----------|
| G1 | @pm | Advisory | Verifica entidades reutilizáveis antes de criar epic | No |
| G2 | @sm | Advisory | Verifica tasks/templates ao criar story | No |
| G3 | @po | Soft Block | Verifica duplicação ao validar story | Soft |
| G4 | @dev | Info | Mostra patterns ao iniciar desenvolvimento | No |
| G5 | @qa | Blocks Merge | Verifica se artefato poderia reutilizar existente | YES |
| G6 | @devops | Blocks Merge | Verifica integridade do registry | YES CRITICAL |

### Override Policy

**Command:** `--override-ids --override-reason "explanation"`

**Permitted when:**
- Time-critical fix requires immediate creation
- Adaptation would introduce unacceptable risk
- Existing artifact is deprecated/frozen

**Requirements:**
- Logged for audit trail
- Reviewed within 7 days
- Include override reason in gate verification log

### Graceful Degradation

All gates implement circuit breaker:
- **Timeout:** 2s default
- **On timeout:** warn-and-proceed
- **On error:** log-and-proceed
- **Key principle:** Development NEVER blocked by IDS failures

Implementado em `.aios-core/core/ids/`

---

## Sistema de Elicitation

Workflows interativos em `.aios-core/elicitation/`:
- `agent-elicitation.js` - Criação de agentes
- `task-elicitation.js` - Criação de tasks
- `workflow-elicitation.js` - Criação de workflows

**CRITICAL:** Tasks com `elicit: true` requerem interação humana obrigatória. NUNCA skip elicitation para eficiência.

---

## Comandos de Desenvolvimento

### Comandos NPM

```bash
# Instalação do AIOS
npx @synkra/aios-core@latest install

# Upgrade do AIOS
npx @synkra/aios-core@latest install --force-upgrade

# Testes e qualidade
npm test                    # Rodar todos os testes
npm run lint                # ESLint
npm run typecheck           # Verificação de tipos TypeScript
npm run build               # Build produção

# Sincronização IDE
npm run sync:ide            # Sincronizar configurações do IDE
npm run sync:skills:codex   # Sincronizar skills do Codex CLI
npm run validate:structure  # Validar estrutura do projeto
npm run validate:agents     # Validar configurações de agentes
```

---

## Configuração de Ambiente

### Variáveis de Ambiente (ver `.env.example`)

```bash
# LLM Providers
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
OPENROUTER_API_KEY=

# Search & Research
EXA_API_KEY=
CONTEXT7_API_KEY=

# Database
SUPABASE_URL=
SUPABASE_ANON_KEY=

# Version Control
GITHUB_TOKEN=

# Project Management
CLICKUP_API_KEY=
```

### Arquivos de Configuração

- `.aios-core/core-config.yaml` - Configuração central do projeto
- `.env` - Variáveis de ambiente (não commitado)
- `.env.example` - Template de variáveis de ambiente

---

## Templates e Documentos

### Localização

- Templates: `.aios-core/product/templates/`
- Checklists: `.aios-core/product/checklists/`
- Tasks: `.aios-core/development/tasks/`
- Workflows: `.aios-core/development/workflows/`

### Templates Principais

- `story.hbs` / `story-tmpl.yaml` - Template de story
- `epic.hbs` - Template de epic
- `prd.hbs` / `prd-tmpl.yaml` - Template de PRD
- `architecture-tmpl.yaml` - Template de arquitetura

---

## Padrões de Código

### Imports (Absolute Imports) - Article VI

```typescript
// CORRETO
import { useStore } from '@/stores/feature/store'

// INCORRETO
import { useStore } from '../../../stores/feature/store'
```

### Convenções de Nomenclatura

| Tipo | Convenção | Exemplo |
|------|-----------|---------|
| Componentes | PascalCase | `WorkflowList` |
| Hooks | prefixo `use` | `useWorkflowOperations` |
| Arquivos | kebab-case | `workflow-list.tsx` |
| Constantes | SCREAMING_SNAKE_CASE | `MAX_RETRIES` |

---

## Ferramentas de Orquestração

### Synapse System

Localizado em `.aios-core/core/synapse/` - gerencia conexões entre componentes.

### Registry System

Localizado em `.aios-core/core/registry/` - sistema de reutilização de entidades.

---

## Debug e Diagnostics

```bash
# Habilitar debug
export AIOS_DEBUG=true

# Ver logs
tail -f .aios/logs/agent.log

# Trace workflow
npm run trace -- workflow-name
```

---

## Links Importantes

- Constitution: `.aios-core/constitution.md`
- User Guide: `.aios-core/user-guide.md`
- Brownfield Guide: `.aios-core/working-in-the-brownfield.md`
- Core README: `.aios-core/core/README.md`
- Development README: `.aios-core/development/README.md`
- Rules detalhadas: `.claude/rules/` (agent-authority, story-lifecycle, workflow-execution, ids-principles, coderabbit-integration, mcp-usage)

---

*Synkra AIOS v4.2.13 | CLI First | Agent-Driven | Quality First*
