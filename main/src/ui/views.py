import click


def list_view(sites):
    print(f"{'Tag':<20} {'Url':<50} {'Description':<50} {'Date':<10}")
    print(
        f"{'-----------------':<20} {'-----------------------------------------------':<50} {'-----------------------------------------------':<50} {'-----------':<10}"
    )
    click.echo()
    for site in sites:
        if site.desc:
            click.echo(
                f"{site.tag:<20} {site.url:<50} {site.desc:<50} {site.date.strftime('%d %b %Y'):<10}"
            )
        else:
            click.echo(
                f"{site.tag:<20} {site.url:<50} {' ':<50} {site.date.strftime('%d %b %Y'):<10}"
            )
    click.echo()


def pretty_view(sites):
    number_hyphen = 0
    for site in sites:
        # adapt the number of hyphens to output length number of hyphen the maximum output length
        number_hyphen = max(
            max(len(site.tag), len(site.url))
            if not site.desc
            else max(len(site.tag), len(site.url), len(site.desc)),
            number_hyphen,
        )
    number_hyphen += 20
    click.echo()
    for site in sites:
        click.echo(f"{'Tag'.upper():<20}", nl=False)
        click.echo(site.tag)
        click.echo(f"{'Url'.upper():<20}", nl=False)
        click.echo(site.url)
        click.echo(f"{'Date'.upper():<20}", nl=False)
        click.echo(site.date.strftime("%d %b %Y"))
        click.echo(f"{'Description'.upper():<20}", nl=False)
        click.echo(site.desc)
        for index in range(0, number_hyphen):
            click.echo("-", nl="")
        click.echo()
        click.echo()


def list_tags_view(sites):
    print(f"{'Tag':<20}")
    print(f"{'------------------':<20}")
    for site in sites:
        click.echo(f"{site.tag:<20}")
    pass
