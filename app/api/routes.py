from fastapi import APIRouter

from langchain_core.messages import HumanMessage

from app.graph.workflow import graph
from app.api.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=request.message)
            ]
        }
    )

    return ChatResponse(
        response=result["messages"][-1].content
    )