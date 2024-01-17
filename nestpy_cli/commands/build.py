from typer import echo, Option


def build(
    name: str,
    path: bool = Option(None, '--path', '-p'),
    config: bool = Option(None, '--config', '-c'),
    watch: bool = Option(None, '--watch', '-w'),
):
    """
    Shoot the portal gun
    """
    echo("Shooting portal gun")