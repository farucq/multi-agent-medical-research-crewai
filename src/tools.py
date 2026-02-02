from crewai.tools import tool
from ddgs import DDGS

@tool("Medical literature search")
def medical_search(query: str) -> str:
    """Search recent medical and clinical trial information"""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(f"- {r['title']}: {r['body']}")
    return "\n".join(results)
