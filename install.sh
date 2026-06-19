#!/bin/bash
set -euo pipefail

if [ ! -f .env ]; then
  cp .env.example .env
fi

docker compose pull ollama || true
docker compose run --rm ollama ollama pull ${MODEL:-llama3.1:8b}

docker compose up -d