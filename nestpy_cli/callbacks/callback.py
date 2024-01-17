from nestpy_cli.callbacks import version_callback
from typer import Option

def callback(
    version: bool = Option(None, "--version", "-v", callback=version_callback)
) -> None:
    """
    Nestpy CLI Application
    """