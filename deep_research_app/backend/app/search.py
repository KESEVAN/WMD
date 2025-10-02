from exa_py import Exa
import os

exa = Exa(api_key=os.getenv("EXA_API_KEY"))

def search_web(query: str, num_results: int = 5):
    """Performs a web search using Exa API."""
    res = exa.search_and_contents(
        query,
        type="auto",
        num_results=num_results,
        text={"max_characters": 1000}
    )
    return res.results
