# Variables
SERVICE_NAME ?= ExampleService
OUTPUT_FILE ?= $(SERVICE_NAME).py

# Install dependencies
.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Generate service skeleton
.PHONY: generate
generate:
	@echo "Generating skeleton code for service: $(SERVICE_NAME)"
	@python3 codegen.py generate --service-name $(SERVICE_NAME) --output-file $(OUTPUT_FILE)
	@echo "Skeleton code saved to $(OUTPUT_FILE)"

# List available templates
.PHONY: templates
list-templates:
	@python3 codegen.py list-templates