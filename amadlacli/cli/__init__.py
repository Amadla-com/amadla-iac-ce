"""
Amadla cli.

(C) 2024 Jean-Nicolas Boulay Desjardins (JNBD)
Released under MIT License

CLI classes.
"""

import click

from amadlacli.app import APP
from amadlacli.cli.entity import entity_cli
from amadlacli.cli.template import template_cli
from amadlacli.cli.schema import schema_cli


@click.group()
@click.version_option(APP().version())
@click.pass_context
def cli(ctx):
    """
    Amadla CLI
    """
    pass


# Register the subgroups
cli.add_command(entity_cli.entity)
cli.add_command(template_cli.template)
cli.add_command(schema_cli.schema)

if __name__ == '__main__':
    cli()
