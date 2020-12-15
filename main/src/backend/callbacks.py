import click
from sqlalchemy.exc import SQLAlchemyError
from main.src.backend.handlers import session
from main.src.backend.model import Site
from main.src.ui.views import list_view, pretty_view, list_tags_view


def rm_all(ctx, param, value):
    # This code is add to permit the access of subcommands in some cases
    # If not when hit sitemgr add --help it bring's up the first option of the sitemgr command (eg: sitemgr --list).
    if not value or ctx.resilient_parsing:
        return

    try:
        click.confirm(
            click.style("Are you sure you want to delete this site ?", fg="red"),
            abort=True,
        )
        session.execute("DELETE FROM site;")
        session.commit()
    except SQLAlchemyError as e:
        click.echo(e)

    click.echo(click.style("Deleted Successfully!", fg="green"))
    ctx.exit()  # to forbid the evaluation of other options or arguments


def list_all(ctx, param, value):
    # This code is add to permit the access of subcommands in some cases
    # If not when hit sitemgr add --help it bring's up the first option of the sitemgr command (eg: sitemgr --list).
    if not value or ctx.resilient_parsing:
        return

    try:
        sites = session.query(Site).all()
        list_view(sites)
    except SQLAlchemyError as e:
        click.echo(e)

    ctx.exit()


def pretty(ctx, param, value):
    # This code is add to permit the access of subcommands in some cases
    # If not when hit sitemgr add --help it bring's up the first option of the sitemgr command (eg: sitemgr --list).
    if not value or ctx.resilient_parsing:
        return

    try:
        sites = session.query(Site).all()
        pretty_view(sites)
    except SQLAlchemyError as e:
        click.echo(e)
    ctx.exit()


def list_tags(ctx, param, value):
    # This code is add to permit the access of subcommands in some cases
    # If not when hit sitemgr add --help it bring's up the first option of the sitemgr command (eg: sitemgr --list).
    if not value or ctx.resilient_parsing:
        return

    try:
        sites = session.execute("SELECT tag from site;")
        list_tags_view(sites)
    except SQLAlchemyError as e:
        click.echo(e)
    ctx.exit()
