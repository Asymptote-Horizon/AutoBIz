from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dummy-agent-5")


class AgentFive:
    def __init__(self, name: str = "agent5") -> None:
        self.name = name

    def build_graph(self):
        workflow = StateGraph(dict)
        workflow.add_node("fetch", self.fetch)
        workflow.add_node("score", self.score)
        workflow.add_edge("fetch", "score")
        workflow.add_edge("score", END)
        return workflow.compile()

    def fetch(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "fetched": True, "value": "sample-data"}

    def score(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "score": 99, "confidence": "high"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "tags": ["demo", "dummy"], "payload": payload}


@mcp.tool()
def score_metric() -> str:
    return "agent5 scoring stub"
