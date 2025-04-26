from agents.research_agent import ResearcherAgent

def test_research():
    try:
        agent = ResearcherAgent()
        result = agent.research("test query")
        
        print("✅ Research successful!")
        print("Query:", result["query"])
        print("Summaries:", result["summaries"])
        print("First raw result:", result["raw_results"]["results"][0]["url"])
        
    except Exception as e:
        print("❌ Research failed:", str(e))
        raise  # Re-raise to see full traceback

if __name__ == "__main__":
    test_research()