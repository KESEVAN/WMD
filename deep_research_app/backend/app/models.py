from pydantic import BaseModel
from typing import List, Dict, Any

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    query: str
    subagents: int
    total_sources: int
    synthesis: str
