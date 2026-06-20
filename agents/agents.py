"""Three agents (Triage, Resolution, Escalation) + LangGraph wiring."""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

from . import llm, tools, guardrails


class AgentState(TypedDict, total=False):
    ticket_id: str
    message: str
    category: str
    draft: str
    escalated: bool
    explicit_human_request: bool
    financial_liability: int
    legal_or_compliance: bool
    failed_attempts: int
    csat: int
    contains_financial_txn: bool


def triage_node(state: AgentState) -> AgentState:
    # simplistic categorization
    msg = state.get("message", "").lower()
    if "refund" in msg or "payment" in msg:
        state["category"] = "billing"
    else:
        state["category"] = "general"
    return state


def resolution_node(state: AgentState) -> AgentState:
    tid = state.get("ticket_id", "unknown")
    kb = tools.kb_search(state.get("message", ""))
    draft = tools.draft_reply(tid, f"Resolution based on {len(kb['results'])} KB results")
    state["draft"] = draft["draft"]
    return state


def escalation_node(state: AgentState) -> AgentState:
    tid = state.get("ticket_id", "unknown")
    esc = tools.create_escalation(tid, "complex issue")
    state["escalated"] = esc["escalated"]
    return state


def router(state: AgentState) -> Literal["escalation", "resolution"]:
    if guardrails.should_escalate(state):
        return "escalation"
    # Billing and general tickets both get a resolution attempt; tickets that
    # need a human are handled by the escalation branch above. This avoids
    # silently dropping "general" tickets to __end__ with no reply or handoff.
    return "resolution"


def build_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("triage", triage_node)
    workflow.add_node("resolution", resolution_node)
    workflow.add_node("escalation", escalation_node)
    workflow.set_entry_point("triage")
    workflow.add_conditional_edges("triage", router, {
        "escalation": "escalation",
        "resolution": "resolution",
    })
    workflow.add_edge("resolution", END)
    workflow.add_edge("escalation", END)
    return workflow.compile()
