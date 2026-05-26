from pydantic import BaseModel, Field

from app.core.models import MemoryRecord, MemoryType


class MemoryCreateRequest(BaseModel):
    memory_type: MemoryType
    summary: str = Field(min_length=3)
    tags: list[str] = Field(default_factory=list)


class MemoryListResponse(BaseModel):
    items: list[MemoryRecord]
