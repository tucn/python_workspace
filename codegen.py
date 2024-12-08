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


def generate_service(service_name: str, output_file: Path):
    """Generate service skeleton code using a template."""
    # Load template
    template = env.get_template("service_template.jinja")

    # Render template with provided service name
    code = template.render(service_name=service_name)

    output_folder = Path(service_name)
    output_file = output_folder / f"{output_file}.py"

    # Write generated code to the output file
    output_folder.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        f.write(code)

    console.print(f"[green]Generated service skeleton for '{service_name}' in '{output_file}'[/]")


@app.command()
def generate(
    service_name: str = typer.Option(..., help="The name of the service to generate."),
    output_file: Path = typer.Option(
        ..., help="The output file to save the generated service skeleton."
    ),
):
    """Generate a service skeleton."""
    generate_service(service_name, output_file)


@app.command()
def list_templates():
    """List available templates."""
    templates = os.listdir(TEMPLATES_DIR)
    console.print("[cyan]Available templates:[/]")
    for template in templates:
        console.print(f"  - {template}")


if __name__ == "__main__":
    app()
