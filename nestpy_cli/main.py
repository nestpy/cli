from nestpy_cli.callbacks import callback
from nestpy_cli.commands import new, generate, build, start, add, info

import typer


app = typer.Typer()

app.callback()(callback)
app.command('new')(new)
app.command('generate')(generate)
app.command('build')(build)
app.command('start')(start)
app.command('add')(add)
app.command('info')(info)