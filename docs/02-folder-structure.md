# 02 — Folder Structure

```txt
DES/
├── apps/
│   ├── desktop/                 # Tauri desktop shell
│   └── web/                     # Next.js application
├── services/
│   └── api/                     # FastAPI backend and workers
├── packages/
│   ├── config/                  # Shared lint/build/tooling config
│   ├── types/                   # Shared contracts and schemas
│   └── ui/                      # Shared UI primitives and tokens
├── infra/                       # Deployment, database, and observability
├── scripts/                     # Dev automation scripts
└── docs/                        # Architecture and roadmap docs
```

## Planned internal structure highlights

- `services/api/app/agents/*` specialized agent modules.
- `services/api/app/memory/*` memory pipeline and retrieval.
- `apps/web/src/features/*` domain-first frontend modules.
- `apps/desktop/src-tauri/*` OS-level command and permission bridge.
