from typer import Exit
from nestpy_cli import __version__


def version_callback(value: bool) -> None:
    if value:
        print(__version__)
        raise Exit()
