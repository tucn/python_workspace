# python_workspace
My idea designed workspace for Python Project 

## Project Structure
```
.
├── services/
│   ├── __init__.py
│   ├── service1.py             # Service code, generated from template with codegen
├── foundation/
│   ├── __init__.py
│   ├── foundation.py           # Foundation code
├── templates/
│   └── service_template.jinja  # Template for service code
├── codegen.py                  # Codegen script with TUI
├── requirements.txt            # Dependencies
├── Makefile                    # Makefile for invoking codegen
```

## How to use
1. Install dependencies:
```
make install
```
2. Run codegen:
```
make generate SERVICE_NAME=example OUTPUT_FILE=main.py
```
3. List available templates:
```
make list-templates
```