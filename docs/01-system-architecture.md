# 01 — Complete System Architecture

## High-level architecture

DES uses a local-first hybrid model with clear boundaries:

1. **Presentation Layer**
   - Next.js + React + Tailwind + Framer Motion UI.
   - Voice-first interaction components.
   - Desktop shell via Tauri.

2. **Orchestration Layer (FastAPI)**
   - Session manager.
   - Multi-agent coordinator.
   - Policy and permissions engine.
   - Streaming transport for speech + token updates.

3. **Capability Layer**
   - Computer control adapters (filesystem, apps, browser automation).
   - Vision services (OCR, screenshot parsing, screen context).
   - Integration adapters (GitHub, Slack, etc.).

4. **Intelligence Layer**
   - Provider abstraction (OpenAI, Anthropic, local models).
   - Agent role runtime and tool router.
   - Planning and execution engine.

5. **Memory & Data Layer**
   - PostgreSQL for relational state.
   - Vector store for semantic retrieval.
   - Knowledge graph for entities and relationships.
   - Encrypted local vault for secrets and sensitive logs.

## Runtime topology

- **Desktop Process (Tauri):** native permissions, wake word, push-to-talk, local automation bridge.
- **UI Process (Next.js):** cinematic interface, activity timeline, memory center.
- **API Process (FastAPI):** business logic and orchestration.
- **Workers:** async jobs for embedding, indexing, OCR, external integrations.

## Security model

- Default deny permissions.
- User consent prompts for sensitive actions.
- Capability-scoped API keys and token vault.
- Local encryption at rest for memory and credentials.
- Action audit log with immutable event IDs.
