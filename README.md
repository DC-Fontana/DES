# DES (Desktop Executive System)

DES is a voice-first private AI operating system.

## Monorepo layout

- `apps/web` – Next.js cinematic control UI.
- `apps/desktop` – Tauri shell and desktop capabilities.
- `services/api` – FastAPI orchestration + agent runtime.
- `packages/ui` – shared design system.
- `packages/types` – shared TypeScript contracts.
- `docs` – architecture, schemas, wireframes, roadmap.

## Current implementation status

- ✅ Architecture docs completed (`docs/01`-`docs/07`).
- ✅ Phase 1 kickoff scaffold added:
  - Next.js app shell in `apps/web`.
  - FastAPI service with `/health` and `/mission` endpoints.
  - API unit tests in `services/api/tests`.
  - Vercel configuration with root directory pointing to `apps/web`.

## Local development

```bash
npm install
npm run dev:web
```

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r services/api/requirements.txt
PYTHONPATH=services/api pytest services/api/tests -q
```
