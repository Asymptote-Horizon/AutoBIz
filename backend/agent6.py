from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dummy-agent-6")


class AgentSix:
    def __init__(self, name: str = "agent6") -> None:
        self.name = name

    def build_graph(self):
        workflow = StateGraph(dict)
        workflow.add_node("prepare", self.prepare)
        workflow.add_node("finalize", self.finalize)
        workflow.add_edge("prepare", "finalize")
        workflow.add_edge("finalize", END)
        return workflow.compile()

    def prepare(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "prepared": True, "phase": "draft"}

    def finalize(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "finalized": True, "phase": "complete"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "result": "mock-final", "payload": payload}


@mcp.tool()
def finalize_stub() -> str:
    return "agent6 placeholder complete"
