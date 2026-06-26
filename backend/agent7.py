from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dummy-agent-7")


class AgentSeven:
    def __init__(self, name: str = "agent7") -> None:
        self.name = name

    def build_graph(self):
        workflow = StateGraph(dict)
        workflow.add_node("audit", self.audit)
        workflow.add_node("report", self.report)
        workflow.add_edge("audit", "report")
        workflow.add_edge("report", END)
        return workflow.compile()

    def audit(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "audit": "sample audit trail"}

    def report(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "report": "dummy report content"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "status": "dummy", "payload": payload}


@mcp.tool()
def audit_tool() -> Dict[str, Any]:
    return {"tool": "agent7", "note": "placeholder mcp tool"}
