# redevops.io

Self-hosted agentic customer support platform.

## The Problem

SME owners wear multiple hats and are drowning in support inquiries. Legacy solutions trap teams in Zendesk/Intercom per-seat lock-in. Chatwoot-style OSS provides a capable base but has no AI agents.

redevops.io delivers the self-hosted agentic platform that closes the gap.

## Value Propositions

- No per-seat pricing, one-time cost
- Self-hosted data ownership & GDPR compliance
- Agentic resolution (not chatbots)
- Built for mid-market teams

## What It Does

redevops.io combines open-source support infrastructure with an autonomous agent layer. It ingests inquiries, routes them through intelligent agents, and resolves issues without constant human intervention while keeping every byte of customer data under your control.

## Architecture

### OSS Core
- Chatwoot
- PostgreSQL
- Redis
- Elasticsearch
- Nginx
- Ollama

### Agent Layer
- LangGraph
- Sidekick orchestrator (see agent-harness)

## Quickstart

1. Clone the repository.
2. Copy `.env.example` to `.env` and configure values.
3. Run `./install.sh` or `docker compose up -d`.

## License

AGPL

