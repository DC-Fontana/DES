# 03 — Database Schema

## Core PostgreSQL tables

- `users` (id, display_name, locale, timezone, created_at)
- `devices` (id, user_id, os, hostname, trust_level, created_at)
- `sessions` (id, user_id, started_at, ended_at, channel)
- `messages` (id, session_id, role, content, token_count, created_at)
- `projects` (id, user_id, name, status, metadata, updated_at)
- `tasks` (id, project_id, title, priority, state, due_at)
- `memories` (id, user_id, memory_type, summary, source_ref, created_at)
- `memory_chunks` (id, memory_id, chunk_text, embedding_id, ordinal)
- `entities` (id, user_id, type, name, confidence)
- `relationships` (id, from_entity_id, to_entity_id, relation_type, weight)
- `permissions` (id, user_id, capability, scope, granted, updated_at)
- `integrations` (id, user_id, provider, status, encrypted_credentials)
- `activity_events` (id, session_id, event_type, payload, created_at)

## Vector store collections

- `memory_embeddings` keyed by `memory_chunk_id`.
- `project_embeddings` keyed by `project_id` and `task_id`.

## Indexes

- GIN full-text on `messages.content` and `memories.summary`.
- Composite index: `(user_id, created_at DESC)` for sessions and memories.
- Graph traversal indexes on `relationships.from_entity_id`, `to_entity_id`.
