from fastapi import FastAPI
from dotenv import load_dotenv
from .models import ResearchRequest, ResearchResponse
from .research import anthropic_multiagent_research

load_dotenv()

app = FastAPI()

@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    """Run the multi-agent research process."""
    result = anthropic_multiagent_research(request.query)
    return result
