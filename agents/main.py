"""Entrypoint for the agentic layer."""

from .agents import build_graph, AgentState


def run(ticket_id: str, message: str) -> AgentState:
    graph = build_graph()
    state: AgentState = {"ticket_id": ticket_id, "message": message}
    result = graph.invoke(state)
    return result


if __name__ == "__main__":
    print(run("T1", "Please help with my order"))
