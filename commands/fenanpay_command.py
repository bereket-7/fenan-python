import click


@click.command()
@click.argument('args', nargs=-1)
def fenanpay_command(args):
    """My command"""
    click.echo('All done')


if __name__ == '__main__':
    fenanpay_command()
