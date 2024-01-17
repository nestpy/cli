from typer import echo, Option


def start(
    name: str,
    path: bool = Option(None, '--path', '-p'),
    config: bool = Option(None, '--config', '-c'),
    watch: bool = Option(None, '--watch', '-w'),
    debug: bool = Option(None, '--debug', '-d'),
    exec: bool = Option(None, '--exec', '-e'),
):
    """
    Shoot the portal gun
    """
    echo("Shooting portal gun")