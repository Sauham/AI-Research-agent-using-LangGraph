from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional
from agents.research_agent import ResearcherAgent
from agents.draft_agent import DraftAgent

class ResearchState(TypedDict):
    summaries: List[str]
    query: str
    draft: Optional[str]

def create_workflow():
    researcher = ResearcherAgent()
    drafter = DraftAgent(researcher.llm)
    
    workflow = StateGraph(ResearchState)
    
    # Define nodes
    workflow.add_node("research_node", lambda state: researcher.research(state["query"]))
    workflow.add_node("draft_node", lambda state: {"draft": drafter.draft(state)})
    
    # Set connections
    workflow.set_entry_point("research_node")
    workflow.add_edge("research_node", "draft_node")
    workflow.add_edge("draft_node", END)
    
    # Compile the workflow
    return workflow.compile()