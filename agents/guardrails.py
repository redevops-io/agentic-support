"""Guardrails / human-in-the-loop boundaries."""

import os
from typing import Dict


def should_escalate(state: Dict) -> bool:
    """Return True if human escalation required per guardrails."""
    if state.get("explicit_human_request"):
        return True
    if state.get("financial_liability", 0) > 500:
        return True
    if state.get("legal_or_compliance"):
        return True
    if state.get("failed_attempts", 0) >= 3:
        return True
    if state.get("csat", 5) < 2:
        return True
    if state.get("contains_financial_txn"):
        return True
    return False
