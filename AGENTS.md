# redevops.io Agentic Business OS — module build brief
This repo is an AGPL-3.0, self-hostable, AGENTIC module. The market+product research is in
./_brief.md (READ IT FIRST — source of truth: pain->legacy->redevops positioning, the
open-source core stack, value props, ICP, pricing). Do NOT commit _brief.md (gitignored).

Deliverables (build a credible open-source project, consistent with the brief's stack):
1. README.md — positioning (pain->legacy->redevops triplet + 3-5 value props from the brief),
   what it does, architecture (OSS core + agent layer), and a quickstart.
2. One-command install: docker-compose.yml or install.sh standing up the OSS core named in the
   brief PLUS an agent service.
3. agents/ — the agentic layer (Python; talks to an OpenAI-compatible LLM endpoint via env
   OPENAI_BASE_URL/OPENAI_API_KEY/MODEL; tools + guardrails) referencing the shared lib
   github.com/redevops-io/agent-harness.
4. docs/ (architecture.md, configuration.md), .env.example, Makefile or justfile.
Constraints: keep the AGPL LICENSE; no invented benchmarks/metrics; do not run git push.
