from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp import Tool


class AgentTwo:
    def __init__(self, name: str = "agent2") -> None:
        self.name = name

    def build_graph(self):
        graph = StateGraph(dict)
        graph.add_node("ingest", self.ingest)
        graph.add_node("classify", self.classify)
        graph.add_edge("ingest", "classify")
        graph.add_edge("classify", END)
        return graph.compile()

    def ingest(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "ingested": True, "source": "mock-stream"}

    def classify(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "label": "demo-category"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "mode": "dummy", "result": payload}


def make_tool() -> Tool:
    return Tool(name="agent2_tool", description="placeholder mcp tool")
