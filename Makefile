# Variables
COMPOSE_FILE = docker-compose.yaml
SERVICE = # Specify a service if needed (e.g., SERVICE=web)

# Default target
.PHONY: all
all: help

# Start containers
.PHONY: up
up:
	docker-compose -f $(COMPOSE_FILE) up -d

# Stop and remove containers, networks, volumes, and images
.PHONY: down
down:
	docker-compose -f $(COMPOSE_FILE) down -v

# Restart containers
.PHONY: restart
restart: down up

# Show logs (optionally for a specific service)
.PHONY: logs
logs:
	docker-compose -f $(COMPOSE_FILE) logs -f $(SERVICE)

# List running containers
.PHONY: ps
ps:
	docker-compose -f $(COMPOSE_FILE) ps

# Build or rebuild services
.PHONY: build
build:
	docker-compose -f $(COMPOSE_FILE) build

# Stop containers without removing them
.PHONY: stop
stop:
	docker-compose -f $(COMPOSE_FILE) stop

# Show help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  up        Start containers in detached mode"
	@echo "  down      Stop and remove containers, networks, volumes, and images"
	@echo "  restart   Restart containers"
	@echo "  logs      Show logs (use SERVICE=<name> for specific service)"
	@echo "  ps        List running containers"
	@echo "  build     Build or rebuild services"
	@echo "  stop      Stop containers without removing them"
	@echo "  help      Show this help message"
