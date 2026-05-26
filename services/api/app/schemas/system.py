from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class MissionResponse(BaseModel):
    name: str
    mission: str
    phase: str
