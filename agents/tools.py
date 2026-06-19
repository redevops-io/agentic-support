"""Agent tools: ticket lookup, KB search, draft reply, create escalation."""

from typing import Dict, Any


def ticket_lookup(ticket_id: str) -> Dict[str, Any]:
    return {"ticket_id": ticket_id, "status": "open", "issue": "unknown"}


def kb_search(query: str) -> Dict[str, Any]:
    return {"query": query, "results": []}


def draft_reply(ticket_id: str, content: str) -> Dict[str, Any]:
    return {"ticket_id": ticket_id, "draft": content}


def create_escalation(ticket_id: str, reason: str) -> Dict[str, Any]:
    return {"ticket_id": ticket_id, "escalated": True, "reason": reason}
