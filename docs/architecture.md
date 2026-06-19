# Architecture

Omnichannel ingest -> Chatwoot core -> Sidekick/LangGraph orchestrator (Triage/Resolution/Escalation agents) -> Ollama local LLM -> PostgreSQL/Redis/Elasticsearch, with human-in-the-loop dashboard.