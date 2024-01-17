from importlib import metadata

import typer


app = typer.Typer()
__version__ = metadata.version(__package__)

def version_callback(value: bool) -> None:
    if value:
        print(__version__)
        raise typer.Exit()

@app.callback()
def callback(
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback)
) -> None:
    """
    Nestpy CLI Application
    """


@app.command('new')
@app.command('n')
def new(
    name: str,
    skip_git: bool = typer.Option(None, '--skip-git', '-g'),
    skip_install: bool = typer.Option(None, '--install', '-g'),
):
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command('generate')
@app.command('g')
def generate():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
