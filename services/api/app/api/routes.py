from fastapi import APIRouter

from app.schemas.system import HealthResponse, MissionResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/mission", response_model=MissionResponse)
def mission() -> MissionResponse:
    return MissionResponse(
        name="DES",
        mission="Build a private, voice-first AI operating system.",
        phase="phase-1-foundation",
    )
