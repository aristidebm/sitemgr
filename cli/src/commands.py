import click
from cli.src.callbacks import list_all
from cli.src.callbacks import pretty
from cli.src.callbacks import print_version
from cli.src.callbacks import rm_all
from cli.src.callbacks import list_tags
from cli.src.handlers import add


@click.group()
@click.help_option("--help", "-h")
@click.option(
    "--list",
    "-l",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="list all available sites",
    callback=list_all,
)
@click.option(
    "--tags",
    "-t",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="list site's tag only",
    callback=list_tags,
)
@click.option(
    "--pretty",
    "-p",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="beautify the output",
    callback=pretty,
)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="Show the version",
    callaback=print_version,
)
def cli():
    pass


@cli.command()
def add():
    pass


@cli.command()
@click.option(
    "--all",
    "-a",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="remove all available sites.",
    callback=rm_all,
)
def rm():
    pass


@cli.command()
def update():
    pass
