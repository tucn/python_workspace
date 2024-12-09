import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import typer
from rich.console import Console

console = Console()

app = typer.Typer()

# Setup Jinja2 environment
TEMPLATES_DIR = "templates"
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def generate_code(template_name: str, output_path: Path, context: dict):
    """Generate code from a specified template."""
    # Load the chosen template
    template = env.get_template(template_name)

    # Render the template with the provided context
    code = template.render(**context)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the generated code to the output file
    with open(output_path, "w") as f:
        f.write(code)

    console.print(f"[green]Generated '{template_name}' at '{output_path}'[/]")


@app.command()
def generate_service(
    service_name: str = typer.Option(..., help="Name of the service endpoint."),
    output_dir: Path = typer.Option(Path.cwd(), help="Directory for generated API code."),
):
    """Generate a service skeleton."""
    output_path = output_dir / service_name / f"{service_name}.py"
    context = {"service_name": service_name}
    generate_code("service_template.jinja", output_path, context)


@app.command()
def generate_api(
    endpoint_name: str = typer.Option(..., help="Name of the API endpoint."),
    service_name: str = typer.Option(..., help="Name of the service endpoint."),
    output_dir: Path = typer.Option(Path.cwd(), help="Directory for generated API code."),
):
    """Generate an API endpoint."""
    output_path = output_dir / service_name / f"{endpoint_name}_api.py"
    context = {"endpoint_name": endpoint_name}
    generate_code("api_endpoint_template.jinja", output_path, context)

@app.command()
def generate_game(
    game_name: str = typer.Option(..., help="Name of the game."),
    service_name: str = typer.Option(..., help="Name of the service endpoint."),
    output_dir: Path = typer.Option(Path.cwd(), help="Directory for generated game code."),
):
    """Generate a gaming template."""
    output_path = output_dir / service_name/ f"{game_name}_game.py"
    context = {"game_name": game_name}
    generate_code("gaming_template.jinja", output_path, context)

@app.command()
def generate_ai_training(
    project_name: str = typer.Option(..., help="Name of the AI training project."),
    service_name: str = typer.Option(..., help="Name of the service endpoint."),
    output_dir: Path = typer.Option(Path.cwd(), help="Directory for generated project code."),
):
    """Generate an AI training template."""
    output_path = output_dir / service_name/ f"{project_name}_training.py"
    context = {"project_name": project_name}
    generate_code("ai_training_template.jinja", output_path, context)



@app.command()
def list_templates():
    """List available templates."""
    templates = os.listdir(TEMPLATES_DIR)
    console.print("[cyan]Available templates:[/]")
    for template in templates:
        console.print(f"  - {template}")


if __name__ == "__main__":
    app()
