import os 
from typer import echo, Option

from nestpy_cli.templates.create_template import create_template
from nestpy_cli.templates.main_file import main_file
from nestpy_cli.templates.module_file import module_file
from nestpy_cli.templates.controller_file import controller_file


def new(
    name: str,
    dry_run: bool = Option(None, '--dry_run', '-d'),
    skip_git: bool = Option(None, '--skip-git', '-g'),
    skip_install: bool = Option(None, '--skip-install', '-s'),
    package_manager: bool = Option(None, '--package-manager', '-p'),
    collection: bool = Option(None, '--collection', '-c'),
):
    base_path = f'./{name}/src'

    # NestPy Structure
    os.makedirs(base_path)
    create_template(f'{base_path}/main.py', main_file())
    create_template(f'{base_path}/app_module.py', module_file('App'))
    create_template(f'{base_path}/app_controller.py', controller_file('App'))

    # Git Structure

    # Package Manager

    # Install
