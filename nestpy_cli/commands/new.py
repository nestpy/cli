from typer import echo, Option


def new(
    name: str,
    dry_run: bool = Option(None, '--dry_run', '-d'),
    skip_git: bool = Option(None, '--skip-git', '-g'),
    skip_install: bool = Option(None, '--skip-install', '-s'),
    package_manager: bool = Option(None, '--package-manager', '-p'),
    collection: bool = Option(None, '--collection', '-c'),
):
    """
    Shoot the portal gun
    """
    echo("Shooting portal gun")