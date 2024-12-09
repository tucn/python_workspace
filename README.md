### `README.md`

```markdown
# Code Generator Project

A versatile Python-based code generation tool that allows you to quickly create skeleton code for various types of projects, including:

- **Services**: Generate foundational service code.
- **API Endpoints**: Create Flask-based API endpoint templates.
- **Games**: Build simple game structures using `pygame`.
- **AI Training**: Kickstart AI training projects with preconfigured datasets and machine learning pipelines.

## Features

- Supports multiple templates using the Jinja2 templating engine.
- Includes a friendly CLI interface powered by `typer` and enhanced with rich text.
- Scaffolds projects with consistent structure and configurable output directories.
- Extendable to include additional templates.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/codegen-project.git
   cd codegen-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

## Usage

### CLI Commands

The project provides a CLI tool to generate code based on templates. Below are the supported commands:

#### Generate a Service Skeleton
```bash
python codegen.py generate-service --service-name <SERVICE_NAME>
```
- Example:
  ```bash
  python codegen.py generate-service --service-name MyService
  ```
  Output: A new folder `MyService` with a file `MyService.py`.

#### Generate an API Endpoint
```bash
python codegen.py generate-api --endpoint-name <ENDPOINT_NAME>
```
- Example:
  ```bash
  python codegen.py generate-api --endpoint-name my_endpoint --service-name MyService
  ```
  Output: `my_endpoint_api.py`.

#### Generate a Gaming Skeleton
```bash
python codegen.py generate-game --game-name <GAME_NAME> --service-name MyService
```
- Example:
  ```bash
  python codegen.py generate-game --game-name SpaceAdventure --service-name MyService
  ```
  Output: `SpaceAdventure_game.py`.

#### Generate an AI Training Skeleton
```bash
python codegen.py generate-ai-training --project-name <PROJECT_NAME>
```
- Example:
  ```bash
  python codegen.py generate-ai-training --project-name MyAIProject
  ```
  Output: `MyAIProject_training.py`.

#### List Available Templates
```bash
python codegen.py list-templates
```
- Displays all available templates in the `templates/` directory.

### Makefile

For convenience, you can use the provided `Makefile`:
1. Generate a Service:
   ```bash
   make generate_service SERVICE_NAME=MyService
   ```

2. Generate an API Endpoint:
   ```bash
   make generate_api ENDPOINT_NAME=my_endpoint SERVICE_NAME=MyService
   ```

3. Generate a Game:
   ```bash
   make generate_game GAME_NAME=SpaceAdventure SERVICE_NAME=MyService
   ```

4. Generate AI Training Code:
   ```bash
   make generate_ai_training PROJECT_NAME=MyAIProject SERVICE_NAME=MyService
   ```

### Running Generated Files

1. For **services** and **API endpoints**, simply run the generated Python script:
   ```bash
   python <service-name>/<generated_file>.py
   ```

2. For **games**, ensure `pygame` is installed and execute the script:
   ```bash
   python <service-name>/<game_file>.py
   ```

3. For **AI training projects**, provide a `dataset.csv` file in the same directory as the script, then run:
   ```bash
   python <service-name>/<ai_training_script>.py
   ```

## Extending the Tool

You can add more templates by placing `.jinja` files in the `templates/` folder and updating `codegen.py` to include a new command.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

---

### Key Features of the README

- **Comprehensive Overview**: Covers all aspects of the project and its capabilities.
- **Installation Instructions**: Step-by-step setup process for the tool.
- **Command Documentation**: Describes all CLI commands and their use cases.
- **Extensibility**: Notes how to add new templates.
- **Contribution Guidelines**: Encourages community contributions.
