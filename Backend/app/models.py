from pydantic import BaseModel

class AssistanceRequest(BaseModel):
    topic: str
    description: str
    method: str

deparments = ["sales", "pricing", "shipping", "technical assistance", "returns", "events"]