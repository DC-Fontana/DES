from pydantic import BaseModel, Field

from app.core.models import AgentRole


class AgentPlanRequest(BaseModel):
    message: str = Field(min_length=5)


class AgentPlanItem(BaseModel):
    role: AgentRole
    objective: str


class AgentPlanResponse(BaseModel):
    summary: str
    plan: list[AgentPlanItem]
