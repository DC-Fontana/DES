from fastapi import APIRouter, Query

from app.core.models import AgentRole
from app.core.store import store
from app.schemas.agent import AgentPlanItem, AgentPlanRequest, AgentPlanResponse
from app.schemas.memory import MemoryCreateRequest, MemoryListResponse
from app.schemas.system import HealthResponse, MissionResponse

router = APIRouter()


@router.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status='ok')


@router.get('/mission', response_model=MissionResponse)
def mission() -> MissionResponse:
    return MissionResponse(
        name='DES',
        mission='Build a private, voice-first AI operating system.',
        phase='phase-1-foundation',
    )


@router.post('/memory', response_model=dict)
def create_memory(payload: MemoryCreateRequest) -> dict:
    record = store.add_memory(payload.memory_type, payload.summary, payload.tags)
    return {'id': record.id}


@router.get('/memory', response_model=MemoryListResponse)
def list_memory(query: str | None = Query(default=None)) -> MemoryListResponse:
    return MemoryListResponse(items=store.list_memories(query))


@router.post('/agent/plan', response_model=AgentPlanResponse)
def agent_plan(payload: AgentPlanRequest) -> AgentPlanResponse:
    plan = [
        AgentPlanItem(role=AgentRole.architect, objective='Assess architecture impact and constraints.'),
        AgentPlanItem(role=AgentRole.engineer, objective='Propose implementation steps and risk controls.'),
        AgentPlanItem(role=AgentRole.planner, objective='Order work into phase-aligned tasks.'),
        AgentPlanItem(role=AgentRole.memory_manager, objective='Capture durable project memory updates.'),
    ]
    summary = f"DES analyzed request: {payload.message[:80]}"
    return AgentPlanResponse(summary=summary, plan=plan)
