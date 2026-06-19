.PHONY: install up down logs test model-pull

install:
	./install.sh

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	python -m pytest tests/ -q

model-pull:
	ollama pull $(MODEL)
