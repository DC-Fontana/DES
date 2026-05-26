from enum import StrEnum
from pydantic import BaseModel, Field


class AgentRole(StrEnum):
    architect = "architect"
    engineer = "engineer"
    researcher = "researcher"
    creative_director = "creative_director"
    business_analyst = "business_analyst"
    planner = "planner"
    memory_manager = "memory_manager"


class MemoryType(StrEnum):
    personal = "personal"
    project = "project"
    conversation = "conversation"


class PermissionAction(StrEnum):
    file_read = "file_read"
    file_write = "file_write"
    execute_command = "execute_command"
    browser_automation = "browser_automation"


class MemoryRecord(BaseModel):
    id: str
    memory_type: MemoryType
    summary: str = Field(min_length=3)
    tags: list[str] = Field(default_factory=list)
