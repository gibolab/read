from fastapi import APIRouter
from app.schemas.ai_schema import AIRequest, AIResponse
from app.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.post("/generate", response_model=AIResponse)
def generate_paragraph(request: AIRequest):

    output = llm_service.generate(
        category=request.category,
        variables={"topic": request.topic}
    )

    return AIResponse(content=output)