import click

from main.src.backend.exceptions import TakenTagError, TagNotFoundError
from main.src.backend.handlers import add_handler, rm_handler
from main.src.ui.types import Url, Tag, DateTime


@click.group()
@click.help_option("--help", "-h")
@click.option(
    "--list",
    "-l",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="List all available sites.",
    # callback=
)
@click.option(
    "--pretty",
    "-p",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="Beautify the output.",
)
# callback=pretty,)
@click.option(
    "--tags",
    "-t",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="List site's tag only.",
    # callback=list_tags,)
)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="Show the version.",
    # callaback=print_version,
)
def site_manager():
    """A Ligthweight in-console bookmarking tool for a standalone use."""
    pass


@site_manager.command()
@click.help_option("--help", "-h")
@click.option("--date", "-D", help="Add site's Visiting Date.", type=DateTime)
@click.option(
    "--description",
    "-d",
    help="Add a short description of the site purpose.",
    type=click.types.STRING,
)
@click.argument("url", type=Url)
@click.option("--tag", "-t", help="Tag the site.", type=Tag)
def add(tag, description, date, url):
    """Add  a new site."""
    try:
        add_handler(tag, description, url, date)
    except TakenTagError as e:
        click.echo(f"{e.message}")


@site_manager.command()
@click.option(
    "--all",
    "-a",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="Delete all available sites.",
    # callback =
)
@click.help_option("--help", "-h")
@click.argument("tag", type=Tag)
def rm(tag):
    """Remove a site."""
    click.confirm("Do want to continue deleting the site ?", abort=True)
    try:
        rm_handler(tag)
    except TagNotFoundError as e:
        click.echo(f"{e.message}")


@site_manager.command()
@click.help_option("--help", "-h")
@click.option(
    "--date", "-D", help="Add an updated site's Visiting Date.", type=DateTime
)
@click.option(
    "--description",
    "-d",
    help="Add an updated description of the site purpose.",
    type=click.types.STRING,
)
@click.option("--new-tag", "-t", help=" Add an updated tag of the site.", type=Tag)
@click.option("--url", "-u", help="Add an updated site url.", type=Url)
@click.argument("tag", type=Tag)
def update():
    """Update a site."""
    pass
