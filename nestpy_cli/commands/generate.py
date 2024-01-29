from typer import echo, Option


def generate(
    schematic: str,
    name: str,
    *,
    dry_run: bool = Option(None, '--dry_run', '-d'),
    project: bool = Option(None, '--project', '-p'),
    flat: bool = Option(),
    collection: bool = Option(None, '--collection', '-c'),
    spec: bool = Option()
):
    """
    Shoot the portal gun
    """
    echo("Shooting portal gun")