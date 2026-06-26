from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("agent")


class AgentOne:
    def __init__(self, name: str = "agent1") -> None:
        self.name = name

    def build_graph(self):
        workflow = StateGraph(dict)
        workflow.add_node("collect", self.collect)
        workflow.add_node("summarize", self.summarize)
        workflow.add_edge("collect", "summarize")
        workflow.add_edge("summarize", END)
        return workflow.compile()

    def collect(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "collected": True, "note": "dummy collection step"}

    def summarize(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "summary": "placeholder insight from agent1"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "status": "dummy", "payload": payload}


@mcp.tool()
def ping_agent_one() -> str:
    return "agent1 ready"
