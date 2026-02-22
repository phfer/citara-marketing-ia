# Citara Marketing IA - Contexto da Agência

## Sobre a Citara Marketing

Agência de Marketing Digital especializada em **tráfego pago, social media e conteúdo estratégico**.

- **MRR:** ~R$ 62.720
- **Lovable Project:** https://lovable.dev/projects/20354370-4ae0-4f2a-8263-2f4df35324da
- **Database:** Supabase (https://uzphwscfdjjiniicjgan.supabase.co)

## Clientes Ativos (Top Tickets)

| Cliente | Ticket | Perfis | Observação |
|---------|--------|--------|------------|
| **GRUPO BAUEN** | R$ 25.000 | 7 perfis | FULL |
| **EMASFI** | R$ 8.000 | 5 perfis | Serviços fiscais B2B |
| **PRX** | R$ 5.000 | 5 perfis | - |
| Instituto Pamplona | R$ 2.500 | - | Social + Tráfego |
| Nacional | R$ 2.000 | - | Social + Offline |
| Tulum Residence | - | - | Luxury Real Estate |

## Clientes INATIVOS (NUNCA trabalhar)

- ~~Clube do Enriquecer~~ - FOI EMBORA
- ~~Dani Sarturi~~ - FOI EMBORA
- ~~Liana~~ - EXCLUÍDA
- ~~Giovana (Marca D)~~ - EXCLUÍDA

## Status Especiais

| Cliente | Status | Detalhes |
|---------|--------|---------|
| Rodrigo (PSICO) | Permuta | Sem ticket financeiro |

## Estrutura de Trabalho

```
clientes/
├── EMASFI/
│   └── .claude/EMASFI.md    # Contexto específico do cliente
├── Tulum Residence/
│   └── .claude/TULUM.md     # Contexto específico do cliente
└── FIREVON/
    └── (a criar)
```

## MCP Helper Script

```bash
./mcp-citara-helper.py [comando]
```

**Comandos disponíveis:**
- `equipe` - Listar colaboradores ativos
- `clientes` - Listar todos os clientes
- `projetos` - Listar todos os projetos
- `tarefas` - Listar tarefas
- `faturas` - Listar faturas

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `SUPABASE_URL` | Supabase backend |
| `CITARA_MCP_TOKEN` | MCP server auth |
| `CITARA_MCP_URL` | MCP server endpoint |
| `CLICKUP_API_KEY` | ClickUp integration |
| `CLICKUP_TEAM_ID` | `31081847` (Citara Marketing) |
| `ANTHROPIC_API_KEY` | Claude AI |
| `OPENAI_API_KEY` | GPT models |

## Regra de Ouro: NUNCA Repetir Conteúdo

```
┌─────────────────────────────────────────────────────────────┐
│  PASSO 1: Qual cliente está ativo?                          │
├─────────────────────────────────────────────────────────────┤
│  PASSO 2: LEIA o que já foi criado                          │
│           → ls clientes/[cliente]/                          │
├─────────────────────────────────────────────────────────────┤
│  PASSO 3: LISTE o que existe                                │
│           → Evite duplicatas                                │
├─────────────────────────────────────────────────────────────┤
│  PASSO 4: CRIE apenas NOVO conteúdo                         │
│           → Nunca repita                                    │
└─────────────────────────────────────────────────────────────┘
```

## Registro de Conteúdo

Todo conteúdo criado DEVE ser registrado no `session.json` do cliente:

```json
{
  "content_created": {
    "instagram_posts": ["post-01.md"],
    "linkedin_posts": ["post-li-01.md"],
    "landing_pages": ["lp.html"],
    "emails": ["welcome.md"]
  }
}
```

---

*Citara Marketing IA + AIOS Framework v4.2.13*
