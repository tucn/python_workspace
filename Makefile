# Variables
SERVICE_NAME ?= ExampleService
ENDPOINT_NAME ?= example_endpoint

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Generate service skeleton
.PHONY: generate_service
generate_service:
	@echo "Generating skeleton code for service: $(SERVICE_NAME)"
	@python3 codegen.py generate-service --service-name $(SERVICE_NAME)
	@echo "Skeleton code saved to folder: $(SERVICE_NAME)"

# Generate API endpoint
.PHONY: generate_api
generate_api:
	@echo "Generating API endpoint for: $(ENDPOINT_NAME)"
	@python3 codegen.py generate-api --endpoint-name $(ENDPOINT_NAME) --service-name $(SERVICE_NAME)
	@echo "API endpoint saved as: $(ENDPOINT_NAME)_api.py"

# Generate gaming skeleton
.PHONY: generate_game
generate_game:
	@echo "Generating gaming skeleton for: $(GAME_NAME)"
	@python3 codegen.py generate-game --game-name $(GAME_NAME) --service-name $(SERVICE_NAME)
	@echo "Gaming skeleton saved as: $(GAME_NAME)_game.py"

# Generate AI training skeleton
.PHONY: generate_ai_training
generate_ai_training:
	@echo "Generating AI training skeleton for: $(PROJECT_NAME)"
	@python3 codegen.py generate-ai-training --project-name $(PROJECT_NAME) --service-name $(SERVICE_NAME)
	@echo "AI training skeleton saved as: $(PROJECT_NAME)_training.py"


# List available templates
.PHONY: templates
templates:
	@python3 codegen.py list-templates

# Clean generated files
.PHONY: clean
clean:
	@echo "Cleaning generated files..."
	@rm -rf $(SERVICE_NAME) $(ENDPOINT_NAME)_api.py
	@echo "All generated files removed."
