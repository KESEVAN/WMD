from .ai import ask_ai
from .search import search_web

def anthropic_multiagent_research(query: str):
    """
    Simple implementation of Anthropic's multi-agent approach:
    1. Lead agent plans and delegates
    2. Specialized subagents work in parallel
    3. Lead agent synthesizes results
    """
    print(f"🤖 Anthropic Multi-Agent Research: {query}")
    print("-" * 50)

    # Step 1: Lead Agent - Task Decomposition & Delegation
    print("👨‍💼 LEAD AGENT: Planning and delegating...")

    delegation_prompt = f"""You are a Lead Research Agent. Break down this complex query into 3 specialized subtasks for parallel execution: "{query}""

    For each subtask, provide:
    - Clear objective
    - Specific search focus
    - Expected output

    SUBTASK 1: [Core/foundational aspects]
    SUBTASK 2: [Recent developments/trends]
    SUBTASK 3: [Applications/implications]

    Make each subtask distinct to avoid overlap."""

    plan = ask_ai(delegation_prompt)
    print("  ✓ Subtasks defined and delegated")

    # Step 2: Simulate Parallel Subagents (simplified for demo)
    print("\n🔍 SUBAGENTS: Working in parallel...")

    # Extract subtasks and create targeted searches
    subtask_searches = [
        f"{query} fundamentals principles",  # Core aspects
        f"{query} latest developments",  # Recent trends
        f"{query} applications real world"    # Implementation
    ]

    subagent_results = []
    for i, search_term in enumerate(subtask_searches, 1):
        print(f"  🤖 Subagent {i}: Researching {search_term}")
        results = search_web(search_term, 2)

        sources = []
        for result in results:
            if result.text and len(result.text) > 200:
                sources.append({
                    "title": result.title,
                    "content": result.text[:300]
                })

        subagent_results.append({
            "subtask": i,
            "search_focus": search_term,
            "sources": sources
        })

    total_sources = sum(len(r["sources"]) for r in subagent_results)
    print(f"  📊 Combined: {total_sources} sources from {len(subagent_results)} agents")

    # Step 3: Lead Agent - Synthesis
    print("\n👨‍💼 LEAD AGENT: Synthesizing parallel findings...")

    # Combine all subagent findings
    synthesis_context = f"ORIGINAL QUERY: {query}\n\nSUBAGENT FINDINGS:\n"
    for result in subagent_results:
        synthesis_context += f"\nSubagent {result['subtask']} ({result['search_focus']}):\n"
        for source in result['sources'][:2]:  # Limit for brevity
            synthesis_context += f"- {source['title']}: {source['content']}...\n"

    synthesis_prompt = f"""{synthesis_context}\n
    As the Lead Agent, synthesize these parallel findings into a list of news titles with their sources and a one-liner description.\n
    Format the output as follows:\n
    **News Title 1**\n
    *Source: [Source URL or Name]*\n
    > [One-liner description]\n
    **News Title 2**\n
    *Source: [Source URL or Name]*\n
    > [One-liner description]\n
    ...\n
    """

    final_synthesis = ask_ai(synthesis_prompt)

    print("\n" + "=" * 50)
    print("🎯 MULTI-AGENT RESEARCH COMPLETE")
    print("=" * 50)
    print(final_synthesis)

    return {
        "query": query,
        "subagents": len(subagent_results),
        "total_sources": total_sources,
        "synthesis": final_synthesis
    }
