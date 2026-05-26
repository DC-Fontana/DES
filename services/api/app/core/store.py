from collections.abc import Iterable
from uuid import uuid4

from app.core.models import MemoryRecord, MemoryType


class InMemoryStore:
    def __init__(self) -> None:
        self._memories: list[MemoryRecord] = []

    def add_memory(self, memory_type: MemoryType, summary: str, tags: Iterable[str]) -> MemoryRecord:
        record = MemoryRecord(
            id=str(uuid4()),
            memory_type=memory_type,
            summary=summary,
            tags=sorted(set(tags)),
        )
        self._memories.append(record)
        return record

    def list_memories(self, query: str | None = None) -> list[MemoryRecord]:
        if not query:
            return self._memories
        q = query.lower()
        return [m for m in self._memories if q in m.summary.lower() or any(q in t.lower() for t in m.tags)]


store = InMemoryStore()
