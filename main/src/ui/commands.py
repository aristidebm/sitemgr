import click

from main.src.backend.exceptions import TakenTagError, TagNotFoundError
from main.src.backend.handlers import add_handler, rm_handler
from main.src.ui.types import Url, Tag, DateTime
from main.src.backend.callbacks import rm_all, list_all, list_tags, pretty


@click.group()
@click.help_option("--help", "-h")
@click.option(
    "--list",
    "-l",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="List all available sites.",
    callback=list_all,
)
@click.option(
    "--pretty",
    "-p",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="Beautify the output.",
    callback=pretty,
)
@click.option(
    "--tags",
    "-t",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    help="List site's tag only.",
    callback=list_tags,
)
@click.version_option(version="1.0.0")
def site_manager():
    """A Lightweight in-console bookmarking tool for a personal use."""
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
        click.echo(click.style("Successfully added!", fg="green"))
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
    callback=rm_all,
)
@click.help_option("--help", "-h")
@click.argument("tag", type=Tag)
def rm(tag):
    """Remove a site."""
    click.confirm("Are you sure you want to delete this site ?", abort=True)
    try:
        rm_handler(tag)
        click.echo(click.style("Deleted Successfully!", fg="red"))
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
