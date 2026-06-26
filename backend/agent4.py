from typing import Any, Dict
from langgraph.graph import StateGraph, END
from mcp import ClientSession


class AgentFour:
    def __init__(self, name: str = "agent4") -> None:
        self.name = name

    def build_graph(self):
        graph = StateGraph(dict)
        graph.add_node("observe", self.observe)
        graph.add_node("reply", self.reply)
        graph.add_edge("observe", "reply")
        graph.add_edge("reply", END)
        return graph.compile()

    def observe(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "observed": "sample observation"}

    def reply(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {**state, "reply": "dummy response from agent4"}

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"agent": self.name, "output": "mock-output", "payload": payload}


async def connect_mcp() -> ClientSession:
    return ClientSession(None)  # dummy placeholder
