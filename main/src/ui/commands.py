import click


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
@click.option("--date", "-D", help="Add site's Visiting Date.", type=click.types.STRING)
@click.option(
    "--description",
    "-d",
    help="Add a short description of the site purpose.",
    type=click.types.STRING,
)
@click.option("--tag", "-t", help="Tag the site.", type=click.types.STRING)
@click.argument("url", type=click.types.STRING)
def add():
    """Add  a new site."""
    pass


@site_manager.command()
@click.option("--all", "-a", help="Delete all available sites.")
@click.help_option("--help", "-h")
@click.argument("tag", type=click.types.STRING)
def rm():
    """Remove a site."""
    pass


@site_manager.command()
@click.help_option("--help", "-h")
@click.option(
    "--date", "-D", help="Add an updated site's Visiting Date.", type=click.types.STRING
)
@click.option(
    "--description",
    "-d",
    help="Add an updated description of the site purpose.",
    type=click.types.STRING,
)
@click.option(
    "--new-tag", "-t", help=" Add an updated tag of the site.", type=click.types.STRING
)
@click.option("--url", "-u", help="Add an updated site url.", type=click.types.STRING)
@click.argument("tag", type=click.types.STRING)
def update():
    """Update a site."""
    pass
